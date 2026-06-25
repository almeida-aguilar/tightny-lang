#!/usr/bin/env python3
import shutil
import subprocess
import sys
import time
from pathlib import Path


# ==================== ESTILOS Y FORMATO ====================
class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"


def header(text: str, char: str = "=", width: int = 80):
    """Imprime un encabezado con subrayado decorativo"""
    print(f"\n{Style.BOLD}{text}{Style.RESET}")
    print(Style.GRAY + char * width + Style.RESET)


def table_row(*cols, widths=None, sep=" │ "):
    """Genera una fila de tabla con columnas alineadas"""
    if widths is None:
        widths = [max(len(str(c)), 10) for c in cols]
    cells = []
    for i, col in enumerate(cols):
        cells.append(str(col).ljust(widths[i]))
    return sep.join(cells)


def table_sep(widths: list, sep="┼", line="─"):
    """Genera un separador de tabla con bordes Unicode"""
    parts = []
    for w in widths:
        parts.append(line * (w + 2))
    return "─" + sep.join(parts) + "─"


def table_box(data: list, title: str = None):
    """Imprime una tabla con bordes Unicode estilo ┌─┐ │ └─┘"""
    if not data:
        return

    max_key = max(len(str(k)) for k, _ in data)
    max_val = max(len(str(v)) for _, v in data)
    col_key_w = max_key + 2
    col_val_w = max_val + 2

    row_format = f"│ {{:<{col_key_w}}} │ {{:<{col_val_w}}} │"
    sample_row = row_format.format(" " * col_key_w, " " * col_val_w)
    total_len = len(sample_row)

    if title:
        print(f"\n  {Style.BOLD}{title}{Style.RESET}")

    print("  ┌" + "─" * (total_len - 2) + "┐")
    for key, val in data:
        print("  " + row_format.format(str(key), str(val)))
    print("  └" + "─" * (total_len - 2) + "┘")


# ==================== BÚSQUEDA DE LA RAÍZ DEL PROYECTO ====================
def find_project_root() -> Path:
    """Busca el directorio raíz del proyecto que contiene pyproject.toml"""
    current = Path(__file__).parent
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent
    raise FileNotFoundError(
        f"{Style.RED}No se encontró pyproject.toml; "
        "asegúrate de ejecutar desde el proyecto.{Style.RESET}"
    )


# ==================== CONFIGURACIÓN ====================
PROJECT_ROOT = find_project_root()
LIBS_DIR = PROJECT_ROOT / "libs"
GRAMMAR = PROJECT_ROOT / "src/tightny/grammar/tightny.g4"
OUTPUT_DIR = PROJECT_ROOT / "src/tightny/grammar/gen"


# ==================== FUNCIÓN DE APLANAMIENTO ====================
def flatten_directory(dir_path: Path):
    """Mueve recursivamente todos los archivos desde cualquier subcarpeta a la raíz de dir_path."""
    flattened_count = 0
    while True:
        subdirs = [
            d for d in dir_path.iterdir() if d.is_dir() and d.name != "__pycache__"
        ]
        if not subdirs:
            break
        for subdir in subdirs:
            for item in subdir.iterdir():
                shutil.move(str(item), str(dir_path))
            subdir.rmdir()
            flattened_count += 1
    return flattened_count


# ==================== MAIN ====================
def main():
    start_time = time.time()

    # --- Encabezado ---
    header("GENERADOR DE PARSER ANTLR", "─")

    # --- 1. Validar JAR ---
    jar_matches = list(LIBS_DIR.glob("antlr-*-complete.jar"))
    if not jar_matches:
        print(f"\n  {Style.RED}✗ No se encuentra el JAR en {LIBS_DIR}{Style.RESET}")
        print(f"    Asegúrate de tener antlr-*-complete.jar en libs/")
        sys.exit(1)

    antlr_jar = jar_matches[0]
    version = antlr_jar.stem.replace("antlr-", "").replace("-complete", "")
    print(
        f"\n  {Style.CYAN}📦{Style.RESET} JAR encontrado: {Style.BOLD}{antlr_jar.name}{Style.RESET}"
    )
    print(f"    Versión: {Style.GRAY}{version}{Style.RESET}")
    print(f"    Ruta: {Style.GRAY}{antlr_jar.parent}{Style.RESET}")

    # --- 2. Validar gramática ---
    if not GRAMMAR.exists():
        print(f"\n  {Style.RED}✗ No se encuentra la gramática en:{Style.RESET}")
        print(f"    {GRAMMAR}")
        sys.exit(1)

    print(
        f"\n  {Style.GREEN}✓{Style.RESET} Gramática: {Style.BOLD}{GRAMMAR.name}{Style.RESET}"
    )
    print(f"    Ruta: {Style.GRAY}{GRAMMAR.parent}{Style.RESET}")

    # --- 3. Limpiar salida anterior ---
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
        print(f"\n  {Style.YELLOW}⚠{Style.RESET} Salida anterior eliminada")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # --- 4. Ejecutar ANTLR ---
    cmd = [
        "java",
        "-jar",
        str(antlr_jar),
        "-Dlanguage=Python3",
        "-visitor",
        "-no-listener",
        str(GRAMMAR),
        "-o",
        str(OUTPUT_DIR),
    ]

    print(f"\n  {Style.CYAN}🔄{Style.RESET} Generando parser...")
    print(f"    Comando: {Style.GRAY}{' '.join(cmd)}{Style.RESET}")

    try:
        subprocess.run(cmd, check=True, cwd=PROJECT_ROOT)
    except subprocess.CalledProcessError as e:
        print(f"\n  {Style.RED}✗ Error al generar: {e}{Style.RESET}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"\n  {Style.RED}✗ No se encuentra 'java' en el PATH{Style.RESET}")
        print(f"    Asegúrate de tener Java instalado:")
        print(f"    {Style.GRAY}sudo dnf install java-25-openjdk-headless{Style.RESET}")
        sys.exit(1)

    # --- 5. Aplanar directorios ---
    print(f"\n  {Style.CYAN}📁{Style.RESET} Aplanando subdirectorios generados...")
    flattened = flatten_directory(OUTPUT_DIR)
    if flattened > 0:
        print(f"    {Style.GREEN}✓{Style.RESET} {flattened} subdirectorios aplanados")

    # --- 6. Crear __init__.py ---
    init_file = OUTPUT_DIR / "__init__.py"
    init_file.touch()
    print(f"    {Style.GREEN}✓{Style.RESET} Creado {init_file.name}")

    # --- 7. Estadísticas ---
    elapsed = time.time() - start_time

    # Contar archivos generados
    generated_files = [f for f in OUTPUT_DIR.glob("*.py") if f.name != "__init__.py"]
    file_count = len(generated_files)

    header("ESTADÍSTICAS DE GENERACIÓN")

    stats_data = [
        ("JAR", antlr_jar.name),
        ("Gramática", GRAMMAR.name),
        ("Archivos generados", file_count),
        ("Subdirectorios aplanados", flattened),
        ("Tiempo", f"{elapsed * 1000:.2f} ms"),
    ]

    table_box(stats_data, title="Resumen")

    # --- 8. Listado de archivos generados ---
    if file_count > 0:
        print(f"\n  {Style.CYAN}📄{Style.RESET} Archivos generados:")
        for f in sorted(generated_files):
            print(f"    • {Style.GRAY}{f.name}{Style.RESET}")

    # --- 9. Éxito final ---
    print(f"\n{Style.GREEN}✅ Generación completada en {OUTPUT_DIR}{Style.RESET}")


if __name__ == "__main__":
    main()
