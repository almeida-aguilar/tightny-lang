from gen.tightnyVisitor import tightnyVisitor
from .symbol_table import SymbolTable
from .errors import SemanticError

class SemanticVisitor(tightnyVisitor):
    def __init__(self):
        self.symtab = SymbolTable()
        self.errors: list[SemanticError] = []

    def _error(self, msg, ctx):
        e = SemanticError(msg, ctx.start.line)
        self.errors.append(e)
        return 'error'

    # --- Declaraciones ---

    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        type_spec = ctx.typeSpec().getText()
        has_assign = ctx.ASSIGN() is not None

        sym = None
        try:
            sym = self.symtab.declare(name, type_spec, ctx.start.line, is_constant=False, initialized=False)
        except SemanticError as e:
            self.errors.append(e)
            sym = self.symtab.lookup(name)

        if has_assign:
            self.visit(ctx.expression())
            if sym:
                sym.initialized = True

        return None

    def visitConstDecl(self, ctx):
        name = ctx.ID().getText()
        type_spec = ctx.typeSpec().getText()

        sym = None
        try:
            sym = self.symtab.declare(name, type_spec, ctx.start.line, is_constant=True, initialized=False)
        except SemanticError as e:
            self.errors.append(e)
            sym = self.symtab.lookup(name)

        self.visit(ctx.expression())
        if sym:
            sym.initialized = True
        return None
    # --- Asignación ---

    def _get_id(self, ctx):
        """Intenta extraer un ID simple de una expresión o primary."""
        if hasattr(ctx, 'expression') and callable(ctx.expression) and not ctx.expression(): # es un primary
            pass

        # Si es una expresión que solo contiene un primary
        if hasattr(ctx, 'primary') and callable(ctx.primary) and ctx.primary():
            return self._get_id(ctx.primary())

        # Si es un primary que es solo un ID
        if hasattr(ctx, 'ID') and callable(ctx.ID) and ctx.ID():
            # Verificar que no sea un acceso a array o campo
            if hasattr(ctx, 'LBRACKET') and callable(ctx.LBRACKET) and ctx.LBRACKET():
                return None
            if hasattr(ctx, 'DOT') and callable(ctx.DOT) and ctx.DOT():
                return None
            return ctx.ID().getText()

        return None

    def visitAssignment(self, ctx):
        lhs_ctx = ctx.expression(0)
        rhs_ctx = ctx.expression(1)

        # Visitamos el lado derecho
        self.visit(rhs_ctx)

        target_name = self._get_id(lhs_ctx)

        if target_name:
            sym = self.symtab.lookup(target_name)
            if sym is None:
                self._error(f"Asignación a variable '{target_name}' no declarada", ctx)
            elif sym.is_constant:
                self._error(f"No se puede asignar a la constante '{target_name}'", ctx)
            else:
                sym.initialized = True
        else:
            # Si no es un ID simple, podría ser arr[i] o obj.field
            self.visit(lhs_ctx)

        return None
    # --- Uso de variables (Primary) ---

    def visitPrimary(self, ctx):
        if ctx.ID() and not ctx.DOT(): # ID simple
            name = ctx.ID().getText()
            sym = self.symtab.lookup(name)
            if sym is None:
                self._error(f"Variable '{name}' no declarada", ctx)
                return 'error'

            if not sym.initialized:
                self._error(f"Uso de variable '{name}' no inicializada", ctx)

            sym.used = True
            return sym.type_

        # Otros casos de primary (literales, llamadas, etc.)
        return self.visitChildren(ctx)

    # --- Ámbitos ---

    def visitBlock(self, ctx):
        # El bloque en sí no debería entrar en scope si es llamado desde una función/if/etc.
        # Pero si es un bloque anónimo (si existiera), sí.
        # En tightny, block es usado en funDecl, ifStmt, whileStmt, forStmt, switchStmt.
        # Cada uno de estos debería manejar su propio scope.
        return self.visitChildren(ctx)

    def visitFunDecl(self, ctx):
        # 1. Declarar la función en el ámbito actual (si quisiéramos)
        # 2. Entrar a nuevo ámbito para parámetros y cuerpo
        self.symtab.enter_scope()

        if ctx.paramList():
            self.visit(ctx.paramList())

        self.visit(ctx.block())

        self.symtab.exit_scope()
        return None

    def visitParameter(self, ctx):
        name = ctx.ID().getText()
        type_spec = ctx.typeSpec().getText()
        is_const = ctx.CONST() is not None
        # Parámetros se consideran inicializados
        try:
            self.symtab.declare(name, type_spec, ctx.start.line, is_constant=is_const, initialized=True)
        except SemanticError as e:
            self.errors.append(e)
        return None

    def visitIfStmt(self, ctx):
        self.visit(ctx.expression(0)) # IF condition

        blocks = ctx.block()
        expressions = ctx.expression() # expressions[0] es la del IF, expressions[1:] son de ELIFs

        # block[0] es para IF
        self.symtab.enter_scope()
        self.visit(blocks[0])
        self.symtab.exit_scope()

        # ELIFs
        for i in range(1, len(expressions)):
             self.visit(expressions[i])
             self.symtab.enter_scope()
             self.visit(blocks[i])
             self.symtab.exit_scope()

        # ELSE (si existe)
        if len(blocks) > len(expressions):
            self.symtab.enter_scope()
            self.visit(blocks[-1])
            self.symtab.exit_scope()

        return None
    def visitWhileStmt(self, ctx):
        self.visit(ctx.expression())
        self.symtab.enter_scope()
        self.visit(ctx.block())
        self.symtab.exit_scope()
        return None

    def visitForStmt(self, ctx):
        # for varDecl WHILE expression NEXT assignment DO block END
        self.symtab.enter_scope()
        self.visit(ctx.varDecl())
        self.visit(ctx.expression())
        self.visit(ctx.assignment())
        self.visit(ctx.block())
        self.symtab.exit_scope()
        return None

    def visitSwitchStmt(self, ctx):
        self.visit(ctx.expression())
        # Cada caseStmt y el ELSE block
        for case in ctx.caseStmt():
            self.visit(case)
        if ctx.block():
            self.symtab.enter_scope()
            self.visit(ctx.block())
            self.symtab.exit_scope()
        return None

    def visitCaseStmt(self, ctx):
        self.visit(ctx.expression())
        self.symtab.enter_scope()
        self.visit(ctx.block())
        self.symtab.exit_scope()
        return None
