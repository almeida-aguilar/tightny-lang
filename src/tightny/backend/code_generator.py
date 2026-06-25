from tightny.grammar.gen.tightnyParser import tightnyParser
from tightny.grammar.gen.tightnyVisitor import tightnyVisitor


class CodeGenerator(tightnyVisitor):
    def __init__(self):
        self.pin_decls = []  # (nombre, numero, modo)
        self.var_decls = []  # (nombre, valor_inicial)
        self.lines = []  # líneas de statements (con indentación)
        self.indent = 0

    def _emit(self, line):
        """Añade una línea con la indentación actual a self.lines."""
        self.lines.append("    " * self.indent + line)

    def get_code(self):
        # Este método se llamará después de visitProgram
        return "\n".join(self._build_code())

    def _build_code(self):
        """Construye el código final en el orden correcto."""
        final = []
        # 1. Cabecera
        final.append("#include <stdint.h>")
        final.append("")

        # 2. Declaraciones globales de pines
        for name, num, _ in self.pin_decls:
            final.append(f"const int32_t {name} = {num};")
        # 3. Declaraciones globales de variables
        for name, init in self.var_decls:
            final.append(f"int32_t {name} = {init};")
        if self.pin_decls or self.var_decls:
            final.append("")

        # 4. setup()
        final.append("void setup() {")
        for name, num, mode in self.pin_decls:
            if mode == "out":
                modo = "OUTPUT"
            elif mode == "in":
                modo = "INPUT"
            else:  # pullup
                modo = "INPUT_PULLUP"
            final.append(f"    pinMode({name}, {modo});")
        final.append("}")
        final.append("")

        # 5. loop()
        final.append("void loop() {")
        # Agregamos las líneas de los statements (ya indentadas)
        # Si no hay statements, al menos un comentario o vacío
        if self.lines:
            final.extend(self.lines)
        else:
            final.append("    // nothing to do")
        final.append("}")
        return final

    # ---- visitProgram ----
    def visitProgram(self, ctx):
        # Visitamos todos los hijos: declaraciones y statements
        self.visitChildren(ctx)
        # Nota: después de visitChildren, self.lines contiene los statements emitidos
        # y self.pin_decls/var_decls contienen las declaraciones
        # No hacemos nada más, get_code construirá el código final

    # ---- Declaraciones ----
    def visitPinDecl(self, ctx):
        name = ctx.ID().getText()
        mode = ctx.pinMode().getText()
        number = ctx.INT_LIT().getText()
        self.pin_decls.append((name, number, mode))

    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        init_expr = self.visit(ctx.expression())
        self.var_decls.append((name, init_expr))

    # ---- Statements ----
    def visitStatement(self, ctx):
        # statement : assignment statement | ifStmt statement | ... | assignment | ...
        # Usamos visitChildren para recorrer los hijos, pero debemos evitar visitar statement de forma recursiva?
        # Mejor: iteramos manualmente como antes, para no duplicar.
        # Pero con visitChildren, se visitarán todos los nodos, incluyendo los statement anidados.
        # Sin embargo, si un statement contiene otro statement (como en la regla recursiva), visitChildren los visitará en orden.
        # Eso es correcto.
        # Pero hay que tener cuidado con la indentación: los bloques (if, while) manejan su propia indentación.
        # Si usamos visitChildren, el método visitIfStmt se llamará, y dentro de él se llamará a visitStatement para el cuerpo.
        # Todo funciona bien.
        # Simplemente delegamos en visitChildren para que visite los hijos.
        self.visitChildren(ctx)

    # También podríamos mantener los métodos específicos para cada tipo de statement,
    # pero como ya los tenemos, no es necesario sobrescribir visitStatement;
    # podemos dejar que los nodos específicos sean visitados directamente.
    # Pero el problema es que en la gramática, la regla statement es un nodo intermedio,
    # y los hijos son los nodos concretos (assignment, ifStmt, etc.).
    # Si no sobrescribimos visitStatement, el visitor por defecto visitará los hijos,
    # lo cual es exactamente lo que queremos.
    # Sin embargo, la regla statement tiene recursión: "assignment statement" significa que tiene dos hijos: assignment y statement.
    # Si usamos visitChildren, visitará ambos, y el segundo statement también se visitará.
    # Eso es correcto. Pero también podríamos sobrescribir visitStatement para manejar la recursión explícitamente y evitar visitar dos veces.
    # En la práctica, no pasa nada si visitamos el segundo statement como un hijo, porque su contenido se emitirá en orden.
    # Así que podemos simplemente no sobrescribir visitStatement y dejar que el visitante por defecto haga visitChildren.
    # Por lo tanto, eliminamos el método visitStatement personalizado y confiamos en el comportamiento por defecto.
    # Pero necesitamos que los statements se emitan con indentación. Los métodos específicos (visitIfStmt, visitAssignment, etc.) ya usan _emit.
    # Por lo tanto, no necesitamos visitStatement.

    # ---- Métodos específicos para cada nodo de statement ----
    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression())
        self._emit(f"{name} = {expr};")

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expression())
        self._emit(f"if ({cond}) {{")
        self.indent += 1
        # El cuerpo es un statement (puede ser secuencia)
        if ctx.statement():
            self.visit(ctx.statement())
        self.indent -= 1
        self._emit("}")

        # elseIfChain
        if ctx.elseIfChain():
            self.visitElseIfChain(ctx.elseIfChain())

        # elseClause
        if ctx.elseClause():
            self.visitElseClause(ctx.elseClause())

    def visitElseIfChain(self, ctx):
        if ctx.getChildCount() > 0:
            cond = self.visit(ctx.expression())
            self._emit(f"else if ({cond}) {{")
            self.indent += 1
            if ctx.statement():
                self.visit(ctx.statement())
            self.indent -= 1
            self._emit("}")
            if ctx.elseIfChain():
                self.visitElseIfChain(ctx.elseIfChain())

    def visitElseClause(self, ctx):
        if ctx.getChildCount() > 0:
            self._emit("else {")
            self.indent += 1
            if ctx.statement():
                self.visit(ctx.statement())
            self.indent -= 1
            self._emit("}")

    def visitWhileStmt(self, ctx):
        cond = self.visit(ctx.expression())
        self._emit(f"while ({cond}) {{")
        self.indent += 1
        if ctx.statement():
            self.visit(ctx.statement())
        self.indent -= 1
        self._emit("}")

    def visitWriteCall(self, ctx):
        pin = self.visit(ctx.expression(0))
        val = self.visit(ctx.expression(1))
        self._emit(f"digitalWrite({pin}, {val});")

    def visitWaitCall(self, ctx):
        ms = self.visit(ctx.expression())
        self._emit(f"delay({ms});")

    # ---- readCall (expresión) ----
    def visitReadCall(self, ctx):
        pin = self.visit(ctx.expression())
        return f"digitalRead({pin})"

    # ---- Expresiones ----
    # (los mismos métodos de antes)
    def visitExpression(self, ctx):
        if ctx.OR():
            left = self.visit(ctx.expression())
            right = self.visit(ctx.andExpr())
            return f"({left} || {right})"
        else:
            return self.visit(ctx.andExpr())

    def visitAndExpr(self, ctx):
        if ctx.AND():
            left = self.visit(ctx.andExpr())
            right = self.visit(ctx.notExpr())
            return f"({left} && {right})"
        else:
            return self.visit(ctx.notExpr())

    def visitNotExpr(self, ctx):
        if ctx.NOT():
            inner = self.visit(ctx.notExpr())
            return f"!({inner})"
        else:
            return self.visit(ctx.cmpExpr())

    def visitCmpExpr(self, ctx):
        if ctx.cmpOp():
            left = self.visit(ctx.addExpr(0))
            op = ctx.cmpOp().getText()
            right = self.visit(ctx.addExpr(1))
            return f"({left} {op} {right})"
        else:
            return self.visit(ctx.addExpr(0))

    def visitAddExpr(self, ctx):
        if ctx.addOp():
            left = self.visit(ctx.addExpr())
            op = ctx.addOp().getText()
            right = self.visit(ctx.mulExpr())
            return f"({left} {op} {right})"
        else:
            return self.visit(ctx.mulExpr())

    def visitMulExpr(self, ctx):
        if ctx.mulOp():
            left = self.visit(ctx.mulExpr())
            op = ctx.mulOp().getText()
            right = self.visit(ctx.unaryExpr())
            return f"({left} {op} {right})"
        else:
            return self.visit(ctx.unaryExpr())

    def visitUnaryExpr(self, ctx):
        if ctx.MINUS():
            inner = self.visit(ctx.unaryExpr())
            return f"-{inner}"
        else:
            return self.visit(ctx.primary())

    def visitPrimary(self, ctx):
        if ctx.INT_LIT():
            return ctx.INT_LIT().getText()
        elif ctx.ONE():
            return "HIGH"
        elif ctx.ZERO():
            return "LOW"
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.readCall():
            return self.visitReadCall(ctx.readCall())
        elif ctx.LPAREN():
            return f"({self.visit(ctx.expression())})"
        else:
            return ""
