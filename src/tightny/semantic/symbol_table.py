from .errors import SemanticError


class Symbol:
    def __init__(self, name, kind, line, initialized=False):
        self.name = name
        self.kind = kind  # 'var' o 'pin'
        self.line = line
        self.initialized = initialized
        self.used = False
        self.pin_mode = None  # solo para pines: 'in', 'out', 'pullup'
        self.pin_number = None

    def __repr__(self):
        return f"Symbol({self.name}, {self.kind}, line {self.line})"


class SymbolTable:
    def __init__(self):
        self.symbols = {}  # name -> Symbol
        self.errors = []

    def declare_var(self, name, line, initialized=False):
        if name in self.symbols:
            raise SemanticError(f"Variable '{name}' ya declarada", line)
        sym = Symbol(name, "var", line, initialized)
        self.symbols[name] = sym
        return sym

    def declare_pin(self, name, mode, number, line):
        if name in self.symbols:
            raise SemanticError(f"Pin '{name}' ya declarado", line)
        sym = Symbol(
            name, "pin", line, initialized=True
        )  # el pin se considera inicializado
        sym.pin_mode = mode
        sym.pin_number = number
        self.symbols[name] = sym
        return sym

    def lookup(self, name):
        return self.symbols.get(name)

    def mark_used(self, name, line):
        sym = self.lookup(name)
        if sym:
            sym.used = True
        else:
            raise SemanticError(f"'{name}' no declarado", line)
        return sym

    def unused_warnings(self):
        warns = []
        for sym in self.symbols.values():
            if not sym.used and sym.kind == "var":
                warns.append(
                    f"[Advertencia, línea {sym.line}] La variable '{sym.name}' nunca fue usada"
                )
        return warns
