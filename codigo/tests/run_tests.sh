#!/bin/bash

# Directorio de tests
TEST_DIR="."
PARSER_SCRIPT="../main.py"

if [ "$1" != "o" ] && [ "$1" != "x" ]; then
    echo "Uso: $0 [o|x]"
    echo "  o: Ejecuta tests que deben pasar (o_*.ty)"
    echo "  x: Ejecuta tests que deben fallar (x_*.ty)"
    exit 1
fi

PREFIX=$1
FAILED=0
TOTAL=0

echo "=== Ejecutando tests '$PREFIX' ==="

for f in $TEST_DIR/${PREFIX}_*.ty; do
    [ -e "$f" ] || continue
    ((TOTAL++))
    echo -n "Probando $f... "

    # Ejecutamos el parser y capturamos la salida
    OUTPUT=$(python3 $PARSER_SCRIPT "$f" 2>&1)

    if [ "$PREFIX" == "o" ]; then
        if echo "$OUTPUT" | grep -q "Análisis sintáctico completado con éxito"; then
            echo "PASÓ"
        else
            echo "FALLÓ (se esperaba éxito)"
            echo "$OUTPUT" | grep -A 10 "=== ERRORES ==="
            ((FAILED++))
        fi
    else
        if echo "$OUTPUT" | grep -q "error(es) encontrado(s)"; then
            echo "PASÓ (error detectado como se esperaba)"
        else
            echo "FALLÓ (se esperaba un error sintáctico)"
            ((FAILED++))
        fi
    fi
done

echo ""
echo "Resumen: $((TOTAL - FAILED))/$TOTAL tests pasaron."

if [ $FAILED -ne 0 ]; then
    exit 1
fi
