from .errors import SemanticError

class Symbol:
    def __init__(self, name, type_, scope, line, is_constant=False, initialized=False):
        self.name = name
        self.type_ = type_
        self.scope = scope
        self.line = line
        self.initialized = initialized
        self.used = False
        self.is_constant = is_constant

    def __repr__(self):
        return f"Symbol({self.name}: {self.type_} @ {self.scope}, line {self.line}, const={self.is_constant}, init={self.initialized})"


class SymbolTable:
    def __init__(self):
        # { scope_id -> { var_name -> Symbol } }
        self._table: dict[int, dict[str, Symbol]] = {0: {}}
        self._scope_stack: list[int] = [0]
        self._scope_count = 0

    @property
    def current_scope(self) -> int:
        return self._scope_stack[-1]

    def enter_scope(self):
        self._scope_count += 1
        self._scope_stack.append(self._scope_count)
        self._table[self._scope_count] = {}

    def exit_scope(self):
        self._scope_stack.pop()

    def declare(self, name: str, type_: str, line: int, is_constant: bool = False, initialized: bool = False) -> Symbol:
        scope = self.current_scope
        if name in self._table[scope]:
            raise SemanticError(
                f"Variable '{name}' ya declarada en el ámbito actual", line)
        sym = Symbol(name, type_, scope, line, is_constant, initialized)
        self._table[scope][name] = sym
        return sym

    def lookup(self, name: str) -> Symbol | None:
        for scope in reversed(self._scope_stack):
            if name in self._table.get(scope, {}):
                return self._table[scope][name]
        return None

    def unused_warnings(self) -> list[str]:
        warns = []
        for scope_syms in self._table.values():
            for sym in scope_syms.values():
                if not sym.used:
                    warns.append(
                    f"[Advertencia, línea {sym.line}] La variable '{sym.name}' nunca fue usada")
        return warns
