#!/usr/bin/env python3
import shutil
import subprocess
import sys
from pathlib import Path

ANTLR_JAR = Path("/usr/local/lib/antlr-4.13.1-complete.jar")
GRAMMAR = Path("src/tightny/grammar/tightny.g4")
OUTPUT_DIR = Path("src/tightny/grammar/gen")


def flatten_directory(dir_path: Path):
    """Mueve recursivamente todos los archivos desde cualquier subcarpeta a la raíz de dir_path."""
    # Seguir aplanando hasta que no queden subdirectorios (excepto __pycache__)
    while True:
        subdirs = [
            d for d in dir_path.iterdir() if d.is_dir() and d.name != "__pycache__"
        ]
        if not subdirs:
            break
        for subdir in subdirs:
            # Mover todos los contenidos del subdirectorio a la raíz
            for item in subdir.iterdir():
                shutil.move(str(item), str(dir_path))
            subdir.rmdir()
            print(f"   Aplanado: {subdir.name}")


def main():
    if not ANTLR_JAR.exists():
        print(f"❌ No se encuentra ANTLR JAR en {ANTLR_JAR}", file=sys.stderr)
        sys.exit(1)

    if not GRAMMAR.exists():
        print(f"❌ No se encuentra la gramática en {GRAMMAR}", file=sys.stderr)
        sys.exit(1)

    # Limpiar salida anterior
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        "java",
        "-jar",
        str(ANTLR_JAR),
        "-Dlanguage=Python3",
        "-visitor",
        "-no-listener",
        str(GRAMMAR),
        "-o",
        str(OUTPUT_DIR),
    ]

    print(f"🔄 Generando parser desde {GRAMMAR} ...")
    try:
        subprocess.run(cmd, check=True, cwd=Path.cwd())
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al generar: {e}", file=sys.stderr)
        sys.exit(1)

    # Aplanar todas las subcarpetas generadas
    flatten_directory(OUTPUT_DIR)

    # Asegurar __init__.py
    (OUTPUT_DIR / "__init__.py").touch()
    print(f"✅ Generación completada en {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
