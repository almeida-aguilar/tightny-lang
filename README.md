# Tightny (.ty)

**Tightny** es un lenguaje de dominio específico (DSL) diseñado para simplificar la programación de proyectos introductorios con el framework **Arduino**. Inspirado en la claridad sintáctica de **Lua** y la estructura de **Pascal**, Tightny elimina la verbosidad del C++ de Arduino para que el foco esté en la lógica del proyecto, no en la sintaxis.

Tightny es un **transpiler**: el código `.ty` se traduce directamente a código C++ compatible con el Arduino IDE y el framework Arduino, sin modificar el entorno de desarrollo que ya conoces.

## 🗝️ Palabras Reservadas (Keywords)

Tightny mantiene un vocabulario mínimo e intencional.

**Lista de Keywords (13):**
`pin`, `var`, `if`, `then`, `else`, `end`, `while`, `do`, `and`, `or`, `not`, `in`, `out`, `pullup`

**Comparativa de Complejidad (Número de Keywords):**

| Lenguaje | Total Keywords | Filosofía |
| :--- | :---: | :--- |
| **Tightny** | **14** | **Minimalismo para principiantes** |
| Lua | 22 | Simplicidad y Scripting |
| Arduino (C++) | 32+ | Cercanía al Hardware |
| C (C89) | 32 | Control total |

---

## 📋 Índice

- [Características Principales](#-características-principales)
- [Guía de Sintaxis](#-guía-de-sintaxis)
  - [Reglas del Lenguaje](#reglas-del-lenguaje)
  - [Declaración de Pines](#declaración-de-pines)
  - [Variables](#variables)
  - [Operadores](#-operadores)
  - [Estructuras de Control](#estructuras-de-control)
  - [Funciones Predefinidas](#-funciones-predefinidas)
- [Equivalencias con Arduino](#-equivalencias-con-arduino)
- [Ejemplo Completo](#-ejemplo-completo)

---

## ✨ Características Principales

- **Sintaxis amigable:** Elimina llaves, puntos y coma, y palabras clave en inglés técnico. Un estudiante puede leer código Tightny sin haber programado antes.
- **Modelo de hardware explícito:** Los pines se declaran con su modo antes de usarse, reforzando buenas prácticas desde el inicio.
- **Sin tipos:** Todas las variables son enteros. El objetivo es aprender lógica y control de hardware, no gestión de memoria.
- **Variables globales:** Modelo de memoria simple y predecible, adecuado para proyectos de microcontrolador de alcance reducido.
- **Transpila a Arduino C++:** Genera código limpio y legible, no código máquina. El estudiante puede inspeccionar la salida y entender la correspondencia.

---

## 📝 Guía de Sintaxis

### Reglas del Lenguaje

- **Case-sensitive:** `Led` y `led` son identificadores distintos. Las keywords van siempre en minúsculas.
- **Identificadores:** Deben comenzar con una letra o guion bajo (`_`), seguidos de letras, números o guiones bajos.
- **Comentarios:** Una línea, usando `#`.
  ```ty
  # Esto es un comentario
  ```
- **Sin delimitadores de sentencia:** No se usan punto y coma ni saltos de línea obligatorios. El parser distingue cada sentencia por su estructura de tokens (`if`, `while`, `write`, etc.).
- **Sin llaves:** Los bloques se delimitan con keywords (`then`/`do` ... `end`).

---

### Declaración de Pines

Los pines se declaran en la sección global, antes de cualquier lógica. La sintaxis hace explícito el número de pin físico y su dirección.

```ty
pin led    : out    = 13   # Pin 13, salida digital
pin boton  : in     = 2    # Pin 2,  entrada digital
pin sensor : pullup = 7    # Pin 7,  entrada con resistencia pull-up interna
```

Los tres modos disponibles son:

| Modo | Descripción | Equivalente Arduino |
| :--- | :--- | :--- |
| `out` | Salida digital | `OUTPUT` |
| `in` | Entrada digital | `INPUT` |
| `pullup` | Entrada con pull-up | `INPUT_PULLUP` |

---

### Variables

Todas las variables son globales, enteras y deben inicializarse al declararse.

```ty
var contador = 0
var limite   = 10
var estado   = 1
```

La asignación posterior usa el mismo operador `=`:

```ty
contador = contador + 1
estado   = 0
```

---

### 🔢 Operadores

**Aritméticos:** `+`, `-`, `*`, `/`

**Comparación:** `==`, `!=`, `<`, `>`, `<=`, `>=`

**Lógicos:** `and`, `or`, `not`

**Constantes de valor lógico:**

| Tightny | Significado | Valor |
| :--- | :--- | :--- |
| `high` / `true` | Nivel alto / verdadero | 1 |
| `low` / `false` | Nivel bajo / falso | 0 |

```ty
write(led, high)              # enciende el LED
write(led, read(boton))       # copia el estado del botón al LED
var activo = true
```

---

### Estructuras de Control

**Condicional:**

```ty
if read(boton) == low then
    write(led, high)
    wait(500)
else if contador > limite then
    write(led, low)
else
    write(led, high)
end
```

El bloque `else if` puede encadenarse todas las veces que sea necesario. El bloque `else` es opcional. Todo condicional cierra con `end`.

**Bucle:**

```ty
while contador < limite do
    write(led, high)
    wait(200)
    write(led, low)
    wait(200)
    contador = contador + 1
end
```

El cuerpo del `while` acepta múltiples sentencias. Cierra con `end`.

---

### 🔧 Funciones Predefinidas

Tightny expone tres funciones de hardware. No se pueden definir funciones propias; la lógica se organiza con el flujo de control del programa.

#### `write(pin, valor)`

Escribe un valor digital en un pin de salida.

```ty
write(led, high)    # enciende
write(led, low)     # apaga
write(led, 1)       # equivalente a high
```

Equivale a `digitalWrite(pin, valor)` en Arduino.

#### `read(pin)`

Lee el valor digital de un pin de entrada. Devuelve `high` (1) o `low` (0). Se usa como expresión dentro de condiciones o asignaciones.

```ty
var estado = read(boton)

if read(sensor) == low then
    write(led, high)
end
```

Equivale a `digitalRead(pin)` en Arduino.

#### `wait(ms)`

Pausa la ejecución durante `ms` milisegundos.

```ty
wait(1000)          # espera 1 segundo
wait(intervalo)     # espera el valor de la variable
```

Equivale a `delay(ms)` en Arduino.

---

## 🔄 Equivalencias con Arduino

| Tightny | Arduino C++ |
| :--- | :--- |
| `pin led : out = 13` | `pinMode(13, OUTPUT)` en `setup()` |
| `pin boton : pullup = 2` | `pinMode(2, INPUT_PULLUP)` en `setup()` |
| `write(led, high)` | `digitalWrite(13, HIGH)` |
| `write(led, low)` | `digitalWrite(13, LOW)` |
| `read(boton)` | `digitalRead(2)` |
| `wait(500)` | `delay(500)` |
| `var x = 0` | `int x = 0;` (variable global) |
| `# comentario` | `// comentario` |
| `and` / `or` / `not` | `&&` / `\|\|` / `!` |
| `high` / `true` | `HIGH` / `true` |
| `low` / `false` | `LOW` / `false` |

---

## 🚀 Ejemplo Completo

El siguiente programa hace parpadear un LED mientras un botón esté presionado, y detiene el parpadeo en cuanto se suelta.

```ty
# Hardware
pin led   : out    = 13
pin boton : pullup = 2

# Estado
var encendido = false
var ciclos    = 0

if read(boton) == low then
    # Botón presionado: parpadeo
    write(led, high)
    wait(300)
    write(led, low)
    wait(300)
    ciclos = ciclos + 1
else
    # Botón suelto: LED apagado
    write(led, low)
    ciclos = 0
end
```

**Código Arduino generado:**

```cpp
// Generado por el transpiler Tightny
#include <stdint.h>

const int32_t led   = 13;
const int32_t boton = 2;
int32_t encendido = 0;
int32_t ciclos    = 0;

void setup() {
    pinMode(led,   OUTPUT);
    pinMode(boton, INPUT_PULLUP);
}

void loop() {
    if (digitalRead(boton) == LOW) {
        digitalWrite(led, HIGH);
        delay(300);
        digitalWrite(led, LOW);
        delay(300);
        ciclos = ciclos + 1;
    } else {
        digitalWrite(led, LOW);
        ciclos = 0;
    }
}
```
