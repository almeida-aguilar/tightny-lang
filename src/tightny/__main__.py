import argparse
import sys
import time

from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ErrorListener

from tightny.backend.code_generator import CodeGenerator
from tightny.grammar.gen.tightnyLexer import tightnyLexer
from tightny.grammar.gen.tightnyParser import tightnyParser
from tightny.semantic.semantic_visitor import SemanticVisitor


# ==================== UTILIDADES DE FORMATO ====================
class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"


def header(text: str, char: str = "=", width: int = 80):
    print(f"\n{Style.BOLD}{text}{Style.RESET}")
    print(Style.GRAY + char * width + Style.RESET)


def table_row(*cols, widths=None, sep=" │ "):
    if widths is None:
        widths = [max(len(str(c)), 10) for c in cols]
    cells = []
    for i, col in enumerate(cols):
        cells.append(str(col).ljust(widths[i]))
    return sep.join(cells)


def table_sep(widths: list, sep="┼", line="─"):
    parts = []
    for w in widths:
        parts.append(line * (w + 2))  # +2 por los espacios laterales
    return "─" + sep.join(parts) + "─"


# ==================== LISTENER DE ERRORES ====================
class TightnyErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"línea {line}:{column} → {msg}")


# ==================== CONTADOR DE ESTRUCTURAS (VISITOR) ====================
class StatsVisitor(SemanticVisitor):
    def __init__(self):
        super().__init__()
        self.if_count = 0
        self.while_count = 0
        self.write_count = 0
        self.read_count = 0
        self.wait_count = 0

    def visitIfStmt(self, ctx):
        self.if_count += 1
        super().visitIfStmt(ctx)

    def visitWhileStmt(self, ctx):
        self.while_count += 1
        super().visitWhileStmt(ctx)

    def visitWriteCall(self, ctx):
        self.write_count += 1
        super().visitWriteCall(ctx)

    def visitReadCall(self, ctx):
        self.read_count += 1
        super().visitReadCall(ctx)

    def visitWaitCall(self, ctx):
        self.wait_count += 1
        super().visitWaitCall(ctx)


# ==================== MAIN ====================
def main():
    parser = argparse.ArgumentParser(description="Compilador Tightny")
    parser.add_argument("archivo", help="Archivo de entrada .ty")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Mostrar información de depuración (tokens)",
    )
    args = parser.parse_args()

    archivo = args.archivo
    start_time = time.time()

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            line_count = sum(1 for _ in f)
    except FileNotFoundError:
        print(f"{Style.RED}Error: No se encuentra el archivo '{archivo}'{Style.RESET}")
        sys.exit(1)

    input_stream = FileStream(archivo, encoding="utf-8")
    error_listener = TightnyErrorListener()

    # Lexer
    lexer = tightnyLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = [t for t in stream.tokens if t.type != -1]
    token_count = len(tokens)

    if args.debug:
        header("TOKENS", "─")
        # Cabecera de tabla
        col_widths = [6, 8, 20]
        print(table_row("Línea", "Columna", "Texto", widths=col_widths))
        print(table_sep(col_widths))
        for token in tokens:
            print(
                table_row(token.line, token.column, repr(token.text), widths=col_widths)
            )
        print()

    # Parser
    parser_obj = tightnyParser(stream)
    parser_obj.removeErrorListeners()
    parser_obj.addErrorListener(error_listener)
    tree = parser_obj.program()

    # Análisis sintáctico
    header("ANÁLISIS SINTÁCTICO")
    if error_listener.errors:
        print(
            f"  {Style.RED}✗ Se encontraron {len(error_listener.errors)} error(es){Style.RESET}"
        )
        for err in error_listener.errors[:10]:
            print(f"    • {err}")
        if len(error_listener.errors) > 10:
            print(f"    ... y {len(error_listener.errors) - 10} más")
        print(
            f"\n{Style.RED}Compilación abortada debido a errores sintácticos.{Style.RESET}"
        )
        sys.exit(1)
    else:
        print(f"  {Style.GREEN}✓ Sintaxis correcta{Style.RESET}")

    # Análisis semántico y estadísticas
    visitor = StatsVisitor()
    visitor.visit(tree)

    sem_errors = visitor.errors
    warnings = visitor.symtab.unused_warnings()

    header("ANÁLISIS SEMÁNTICO")
    if sem_errors:
        print(f"  {Style.RED}✗ {len(sem_errors)} error(es) semántico(s){Style.RESET}")
        for e in sem_errors[:10]:
            print(f"    • {e}")
        if len(sem_errors) > 10:
            print(f"    ... y {len(sem_errors) - 10} más")
        sys.exit(1)
    else:
        print(f"  {Style.GREEN}✓ Semántica correcta{Style.RESET}")
        if warnings:
            print(f"  {Style.YELLOW}⚠ {len(warnings)} advertencia(s){Style.RESET}")
            for w in warnings[:5]:
                print(f"    • {w}")
            if len(warnings) > 5:
                print(f"    ... y {len(warnings) - 5} más")

    # Estadísticas
    header("ESTADÍSTICAS DE COMPILACIÓN")
    elapsed = time.time() - start_time

    stats_data = [
        ("Archivo", archivo),
        ("Líneas", line_count),
        ("Tokens", token_count),
        ("Tiempo", f"{elapsed * 1000:.2f} ms"),
        ("Pines", visitor.symtab.pin_count),
        ("Variables", visitor.symtab.var_count),
        ("if", visitor.if_count),
        ("while", visitor.while_count),
        ("write()", visitor.write_count),
        ("read()", visitor.read_count),
        ("wait()", visitor.wait_count),
    ]

    # Anchos máximos de cada columna (sin padding)
    max_key = max(len(k) for k, _ in stats_data)
    max_val = max(len(str(v)) for _, v in stats_data)

    # Añadimos 2 espacios de padding a cada columna (uno a cada lado)
    col_key_w = max_key + 2
    col_val_w = max_val + 2

    # Formato de cada fila
    row_format = f"│ {{:<{col_key_w}}} │ {{:<{col_val_w}}} │"

    # Calculamos la longitud total de una fila (ejemplo con espacios)
    sample_row = row_format.format(" " * col_key_w, " " * col_val_w)
    total_len = len(sample_row)  # incluye los pipes y espacios

    # Borde superior: el interior son total_len - 2 guiones
    print("┌" + "─" * (total_len - 2) + "┐")
    for key, val in stats_data:
        print(row_format.format(key, str(val)))
    print("└" + "─" * (total_len - 2) + "┘")

    print(f"\n{Style.GREEN}Compilación exitosa.{Style.RESET}")

    # 5. Generación de código C++
    generator = CodeGenerator()
    generator.visit(tree)

    # Guardar el código generado
    output_file = archivo.replace(".ty", ".cpp")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(generator.get_code())

    print(f"\n{Style.GREEN}Código C++ generado en: {output_file}{Style.RESET}")
