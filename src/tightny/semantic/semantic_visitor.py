from tightny.grammar.gen.tightnyVisitor import tightnyVisitor

from .errors import SemanticError
from .symbol_table import SymbolTable


class SemanticVisitor(tightnyVisitor):
    def __init__(self):
        self.symtab = SymbolTable()
        self.errors = []

    def _error(self, msg, ctx):
        line = ctx.start.line if ctx else 0
        e = SemanticError(msg, line)
        self.errors.append(e)
        return "error"

    # ---- Declaraciones ----
    def visitPinDecl(self, ctx):
        name = ctx.ID().getText()
        mode_text = ctx.pinMode().getText()
        number = int(ctx.INT_LIT().getText())
        line = ctx.start.line
        try:
            self.symtab.declare_pin(name, mode_text, number, line)
        except SemanticError as e:
            self.errors.append(e)
        return None

    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        line = ctx.start.line
        # La variable se inicializa si tiene expresión de asignación
        initialized = ctx.expression() is not None
        try:
            self.symtab.declare_var(name, line, initialized)
        except SemanticError as e:
            self.errors.append(e)
        # Visitar la expresión de inicialización (si existe) para detectar usos de otras variables
        if ctx.expression():
            self.visit(ctx.expression())
        return None

    # ---- Asignación ----
    def visitAssignment(self, ctx):
        # assignment : ID ASSIGN expression
        var_name = ctx.ID().getText()
        line = ctx.start.line
        sym = self.symtab.lookup(var_name)
        if sym is None:
            self._error(f"Variable '{var_name}' no declarada", ctx)
        elif sym.kind != "var":
            self._error(f"No se puede asignar a un pin ('{var_name}')", ctx)
        else:
            sym.initialized = True
        # Visitar la expresión del lado derecho
        self.visit(ctx.expression())
        return None

    # ---- Llamadas built-in ----
    def visitWriteCall(self, ctx):
        # writeCall : WRITE LPAREN expression COMMA expression RPAREN
        # Primer argumento debe ser un pin (o expresión que devuelva un pin? solo ID)
        pin_expr = ctx.expression(0)
        if pin_expr.getText().isidentifier():
            pin_name = pin_expr.getText()
            sym = self.symtab.lookup(pin_name)
            if sym is None:
                self._error(f"Pin '{pin_name}' no declarado", ctx)
            elif sym.kind != "pin":
                self._error(f"'{pin_name}' no es un pin", ctx)
            else:
                sym.used = True
        else:
            self._error(
                "El primer argumento de write debe ser un identificador de pin", ctx
            )
        # Segundo argumento: expresión cualquiera
        self.visit(ctx.expression(1))
        return None

    def visitReadCall(self, ctx):
        # readCall : READ LPAREN expression RPAREN
        arg = ctx.expression()
        if arg.getText().isidentifier():
            pin_name = arg.getText()
            sym = self.symtab.lookup(pin_name)
            if sym is None:
                self._error(f"Pin '{pin_name}' no declarado", ctx)
            elif sym.kind != "pin":
                self._error(f"'{pin_name}' no es un pin", ctx)
            else:
                sym.used = True
        else:
            self._error("El argumento de read debe ser un identificador de pin", ctx)
        self.visit(arg)
        return None

    def visitWaitCall(self, ctx):
        # waitCall : WAIT LPAREN expression RPAREN
        self.visit(ctx.expression())
        return None

    # ---- Uso de variables en expresiones ----
    def visitPrimary(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            sym = self.symtab.lookup(name)
            if sym is None:
                self._error(f"Variable '{name}' no declarada", ctx)
            else:
                sym.used = True
                if not sym.initialized and sym.kind == "var":
                    self._error(f"Uso de variable '{name}' no inicializada", ctx)
        # Para literales, nada que hacer
        return self.visitChildren(ctx)

    # ---- Condicionales y bucles (solo para propagar ámbitos) ----
    # Tightny no tiene ámbitos anidados, todas las variables son globales.
    # Pero los bloques de if/while no crean nuevo ámbito.
    # Por lo tanto, simplemente visitamos los hijos.
    def visitIfStmt(self, ctx):
        self.visit(ctx.expression())
        # El statement dentro puede ser una lista de statements
        if ctx.statement():
            self.visit(ctx.statement())
        # Manejar elseIfChain y elseClause
        # En la gramática, elseIfChain y elseClause ya están integrados en ifStmt.
        # En nuestro visitor, la estructura visitará automáticamente los hijos.
        # Por simplicidad, llamamos a visitChildren
        return self.visitChildren(ctx)

    def visitWhileStmt(self, ctx):
        self.visit(ctx.expression())
        self.visit(ctx.statement())
        return None

    # Método genérico para cualquier otro nodo
    def visitChildren(self, ctx):
        # Por defecto, visitar todos los hijos
        for child in ctx.getChildren():
            if hasattr(child, "accept"):
                child.accept(self)
        return None
