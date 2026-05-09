import sys
from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ErrorListener
from gen.tightnyLexer import tightnyLexer
from gen.tightnyParser import tightnyParser

class TightnyErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f'línea {line}:{column} → {msg}')

def main():
    if len(sys.argv) < 2:
        print(f'Uso: python {sys.argv[0]} <archivo_entrada>')
        return

    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding='utf-8')

    error_listener = TightnyErrorListener()

    lexer = tightnyLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)
    stream.fill()

    # --- DEBUG: tokens ---
    print('=== TOKENS ===')
    for token in stream.tokens:
        if token.type != -1:
            print(f'  línea {token.line}:{token.column} → [{token.text}]')
    print()

    parser = tightnyParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    parser.program()

    # --- DEBUG: errores ---
    print('=== ERRORES ===')
    if error_listener.errors:
        for e in error_listener.errors:
            print(f'  {e}')
        print(f'\n{len(error_listener.errors)} error(es) encontrado(s).')
    else:
        print('  Análisis sintáctico completado con éxito.')

if __name__ == '__main__':
    main()
