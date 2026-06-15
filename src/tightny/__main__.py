import argparse
import sys

from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ErrorListener

from tightny.grammar.gen.tightnyLexer import tightnyLexer
from tightny.grammar.gen.tightnyParser import tightnyParser
from tightny.semantic.semantic_visitor import SemanticVisitor


class TightnyErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"línea {line}:{column} → {msg}")


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
    input_stream = FileStream(archivo, encoding="utf-8")

    error_listener = TightnyErrorListener()

    lexer = tightnyLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)
    stream.fill()

    # --- DEBUG: tokens ---
    if args.debug:
        print("=== TOKENS ===")
        for token in stream.tokens:
            if token.type != -1:
                print(f"  línea {token.line}:{token.column} → [{token.text}]")
        print()

    parser = tightnyParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    # --- Análisis Sintácticos ---
    print("=== ANÁLISIS SINTÁCTICOS ===")
    if error_listener.errors:
        for e in error_listener.errors:
            print(f"  {e}")
        print(f"\n{len(error_listener.errors)} error(es) sintáctico(s) encontrado(s).")
    else:
        print("  Análisis sintáctico completado con éxito.")

    # --- Análisis Semántico ---
    print("\n=== ANÁLISIS SEMÁNTICO ===")
    visitor = SemanticVisitor()
    visitor.visit(tree)

    # Imprimir errores semánticos
    for e in visitor.errors:
        print(f"  {e}")

    # Imprimir advertencias (variables no usadas) en el mismo estilo que los errores
    warnings = visitor.symtab.unused_warnings()
    for w in warnings:
        print(f"  {w}")

    total_errors = len(visitor.errors)
    if total_errors > 0:
        print(f"\n{total_errors} error(es) semántico(s) encontrado(s).")
        sys.exit(1)
    else:
        print("  Análisis semántico completado con éxito.")


if __name__ == "__main__":
    main()
