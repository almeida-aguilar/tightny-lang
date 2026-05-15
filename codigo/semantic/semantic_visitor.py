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

    def _use_type(self, ctx):
        """Marca un tipo como usado si es un ID (struct/enum)."""
        if not ctx:
            return
        if hasattr(ctx, 'ID') and callable(ctx.ID) and ctx.ID():
            name = ctx.ID().getText()
            sym = self.symtab.lookup(name)
            if sym:
                sym.used = True
        if hasattr(ctx, 'typeSpec') and callable(ctx.typeSpec) and ctx.typeSpec():
            self._use_type(ctx.typeSpec())

    # --- Declaraciones ---

    def visitVarDecl(self, ctx):
        if not ctx.ID() or not ctx.typeSpec():
            return None
        name = ctx.ID().getText()
        type_spec = ctx.typeSpec().getText()
        has_assign = ctx.ASSIGN() is not None

        self._use_type(ctx.typeSpec())

        sym = None
        try:
            sym = self.symtab.declare(name, type_spec, ctx.start.line, is_constant=False, initialized=False)
        except SemanticError as e:
            self.errors.append(e)
            sym = self.symtab.lookup(name)

        if has_assign and ctx.expression():
            self.visit(ctx.expression())
            if sym:
                sym.initialized = True

        return None

    def visitConstDecl(self, ctx):
        if not ctx.ID() or not ctx.typeSpec() or not ctx.expression():
            return None
        name = ctx.ID().getText()
        type_spec = ctx.typeSpec().getText()

        self._use_type(ctx.typeSpec())

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
        # Si es una expresión que consiste solo de un primary
        if hasattr(ctx, 'primary') and callable(ctx.primary) and ctx.primary():
            return self._get_id(ctx.primary())

        # Si es un primary que es solo un ID
        if hasattr(ctx, 'ID') and callable(ctx.ID) and ctx.ID():
            # Si tiene primary base, o DOT, o LBRACKET, no es un ID simple
            has_primary = hasattr(ctx, 'primary') and callable(ctx.primary) and ctx.primary()
            has_dot = hasattr(ctx, 'DOT') and callable(ctx.DOT) and ctx.DOT()
            has_bracket = hasattr(ctx, 'LBRACKET') and callable(ctx.LBRACKET) and ctx.LBRACKET()

            if has_primary or has_dot or has_bracket:
                return None
            return ctx.ID().getText()

        return None

    def visitAssignment(self, ctx):
        lhs_ctx = ctx.expression(0)
        rhs_ctx = ctx.expression(1)
        # Es una asignación simple (=) si el token ASSIGN existe
        is_simple_assign = ctx.ASSIGN() is not None

        # Visitamos el lado derecho
        self.visit(rhs_ctx)

        # Si es una asignación compuesta (+=, -=, etc.), el lado izquierdo
        # actúa como un uso de la variable, por lo que debemos visitarlo.
        if not is_simple_assign:
            self.visit(lhs_ctx)

        target_name = self._get_id(lhs_ctx)

        if target_name:
            sym = self.symtab.lookup(target_name)
            if sym:
                if sym.is_constant:
                    self._error(f"No se puede asignar a la constante '{target_name}'", ctx)
                else:
                    sym.initialized = True
            else:
                # Si no existe y es asignación simple, lanzamos error aquí.
                # Si es compuesta, visit(lhs_ctx) ya lanzó el error de "no declarada".
                if is_simple_assign:
                    self._error(f"Asignación a variable '{target_name}' no declarada", ctx)
        else:
            # Si no es un ID simple (ej: arr[i]) y es asignación simple,
            # visitamos el LHS para que se validen sus componentes (índices, etc.)
            # y se verifique que la base esté inicializada.
            if is_simple_assign:
                self.visit(lhs_ctx)

        return None
    # --- Uso de variables (Primary) ---

    def visitPrimary(self, ctx):
        # ID simple (no es un acceso a campo ni tiene primary base)
        if ctx.ID() and not ctx.primary() and not ctx.DOT() and not ctx.LBRACKET() and not ctx.LPAREN():
            name = ctx.ID().getText()
            sym = self.symtab.lookup(name)
            if sym is None:
                self._error(f"Variable '{name}' no declarada", ctx)
                return 'error'

            if not sym.initialized:
                self._error(f"Uso de variable '{name}' no inicializada", ctx)

            sym.used = True
            return sym.type_

        # AT_ID simple
        if ctx.AT_ID() and not ctx.primary():
            return 'directive'

        # Otros casos de primary (literales, llamadas, etc.)
        return self.visitChildren(ctx)

    # --- Ámbitos ---

    def visitBlock(self, ctx):
        if ctx.ELLIPSIS():
            return None
        return self.visitChildren(ctx)

    def visitFunDecl(self, ctx):
        if not ctx.ID() and not ctx.AT_ID():
            return None
        name = ctx.ID().getText() if ctx.ID() else ctx.AT_ID().getText()

        if ctx.typeSpec():
            self._use_type(ctx.typeSpec())

        try:
            # Registramos la función en el ámbito actual
            self.symtab.declare(name, 'function', ctx.start.line, is_constant=True, initialized=True)
        except SemanticError as e:
            self.errors.append(e)

        self.symtab.enter_scope()
        if ctx.paramList():
            self.visit(ctx.paramList())
        if ctx.block():
            self.visit(ctx.block())
        self.symtab.exit_scope()
        return None

    def visitStructDecl(self, ctx):
        if not ctx.ID():
            return None
        name = ctx.ID().getText()
        try:
            self.symtab.declare(name, 'struct', ctx.start.line, is_constant=True, initialized=True)
        except SemanticError as e:
            self.errors.append(e)

        # Visitamos el cuerpo para procesar var/const declarations dentro del struct
        self.symtab.enter_scope()
        res = self.visitChildren(ctx)
        self.symtab.exit_scope()
        return res

    def visitEnumDecl(self, ctx):
        if not ctx.ID():
            return None
        enum_name = ctx.ID(0).getText()
        try:
            self.symtab.declare(enum_name, 'enum', ctx.start.line, is_constant=True, initialized=True)
        except SemanticError as e:
            self.errors.append(e)

        # Declaramos los miembros del enum como constantes en el ámbito actual
        # En tightny, parece que los miembros de enum son accesibles directamente (ej: Color = RED)
        for i in range(1, len(ctx.ID())):
            member_name = ctx.ID(i).getText()
            try:
                self.symtab.declare(member_name, enum_name, ctx.start.line, is_constant=True, initialized=True)
            except SemanticError as e:
                self.errors.append(e)
        return None

    def visitParameter(self, ctx):
        if not ctx.ID() or not ctx.typeSpec():
            return None
        name = ctx.ID().getText()
        type_spec = ctx.typeSpec().getText()
        is_const = ctx.CONST() is not None

        self._use_type(ctx.typeSpec())

        # Parámetros se consideran inicializados
        try:
            self.symtab.declare(name, type_spec, ctx.start.line, is_constant=is_const, initialized=True)
        except SemanticError as e:
            self.errors.append(e)
        return None
    def visitIfStmt(self, ctx):
        if not ctx.expression():
            return None
        self.visit(ctx.expression(0)) # IF condition

        blocks = ctx.block()
        expressions = ctx.expression() # expressions[0] es la del IF, expressions[1:] son de ELIFs

        if not blocks:
            return None

        # block[0] es para IF
        self.symtab.enter_scope()
        self.visit(blocks[0])
        self.symtab.exit_scope()

        # ELIFs
        for i in range(1, len(expressions)):
             if i < len(blocks):
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
        if not ctx.expression() or not ctx.block():
            return None
        self.visit(ctx.expression())
        self.symtab.enter_scope()
        self.visit(ctx.block())
        self.symtab.exit_scope()
        return None

    def visitForStmt(self, ctx):
        # for varDecl WHILE expression NEXT assignment DO block END
        self.symtab.enter_scope()
        if ctx.varDecl():
            self.visit(ctx.varDecl())
        if ctx.expression():
            self.visit(ctx.expression())  # condition, solo hay una
        if ctx.assignment():
            self.visit(ctx.assignment())  # step
        if ctx.block():
            self.visit(ctx.block())
        self.symtab.exit_scope()
        return None

    def visitSwitchStmt(self, ctx):
        if ctx.expression():
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
        if ctx.expression():
            self.visit(ctx.expression())
        if ctx.block():
            self.symtab.enter_scope()
            self.visit(ctx.block())
            self.symtab.exit_scope()
        return None
    def visitReturnStmt(self, ctx):
        return self.visitChildren(ctx)

    def visitBreakStmt(self, ctx):
        return None

    def visitContinueStmt(self, ctx):
        return None

    def visitDirectiveCall(self, ctx):
        return self.visitChildren(ctx)
