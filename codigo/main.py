import sys
from antlr4 import CommonTokenStream, FileStream
from gen.tightnyLexer import tightnyLexer
from gen.tightnyParser import tightnyParser

def main():
    if len(sys.argv) < 2:
        print(f'Uso: python {sys.argv[0]} <archivo_entrada>')
        return

    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding='utf-8')
    lexer  = tightnyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = tightnyParser(stream)
    tree   = parser.program()      # regla inicial: program

    if parser.getNumberOfSyntaxErrors() > 0:
        print('Errores sintácticos encontrados.')
    else:
        print('Análisis sintáctico completado con éxito.')

if __name__ == '__main__':
    main()
