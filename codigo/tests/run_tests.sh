#!/bin/bash

# Directorio de tests
TEST_DIR="."
PARSER_SCRIPT="../main.py"
DEBUG_FLAG=""
PATTERN="[ox]_*.ty"

# Procesar argumentos
for arg in "$@"; do
    case "$arg" in
        o)
            PATTERN="o_*.ty"
            echo "=== Filtrando tests que deben pasar (o_*.ty) ==="
            ;;
        x)
            PATTERN="x_*.ty"
            echo "=== Filtrando tests que deben fallar (x_*.ty) ==="
            ;;
        --debug)
            DEBUG_FLAG="--debug"
            echo "=== Modo DEBUG activado ==="
            ;;
    esac
done

if [ "$PATTERN" == "[ox]_*.ty" ]; then
    echo "=== Ejecutando todos los tests (o_*.ty y x_*.ty) ==="
fi

# Iterar sobre los archivos encontrados
for f in $TEST_DIR/$PATTERN; do
    [ -e "$f" ] || continue
    echo "------------------------------------------------------------"
    echo "ARCHIVO: $f"
    python3 "$PARSER_SCRIPT" "$f" $DEBUG_FLAG
    echo "------------------------------------------------------------"
    echo ""
done
