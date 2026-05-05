# Tightny (.ty)

**Tightny** es un lenguaje de programación moderno diseñado específicamente para sistemas embebidos. Inspirado en la simplicidad sintáctica de **Lua** y la robustez y control de **Zig**, Tightny busca modernizar y agilizar el desarrollo en el ecosistema Arduino.

Al compilar directamente a código de Arduino, Tightny ofrece una alternativa limpia y segura a C++, permitiendo a los desarrolladores escribir lógica de hardware con una sintaxis expresiva, fuertemente tipada y altamente modular, sin sacrificar rendimiento.

## 🗝️ Palabras Reservadas (Keywords)
Tightny mantiene un diseño minimalista para facilitar el aprendizaje y la implementación del compilador.

**Lista de Keywords (22):**
`var`, `const`, `fun`, `if`, `then`, `elif`, `else`, `end`, `while`, `do`, `for`, `next`, `break`, `continue`, `switch`, `case`, `return`, `struct`, `enum`, `and`, `or`, `not`.

**Comparativa de Complejidad (Número de Keywords):**

| Lenguaje | Total Keywords | Filosofía |
| :--- | :---: | :--- |
| **Tightny** | **22** | **Minimalismo 80/20** |
| Lua | 22 | Simplicidad y Scripting |
| C (C89) | 32 | Cercanía al Hardware |
| Zig | 36 | Seguridad y Modernidad |

## 📋 Índice
- [Características Principales](#-características-principales)
- [Modularidad con @add](#-modularidad-con-add)
- [Guía de Sintaxis](#-guía-de-sintaxis)
  - [Variables y Constantes](#variables-y-constantes)
  - [Tipos de Datos](#tipos-de-datos)
  - [Conversión de Tipos (Casting)](#-conversión-de-tipos-casting)
  - [Operadores](#-operadores)
  - [Estructuras de Control](#estructuras-de-control)
  - [Funciones y Pasaje de Parámetros](#funciones-y-pasaje-de-parámetros)
  - [Bloques sin implementar (...)](#-bloques-sin-implementar-)
  - [Arrays (Arreglos Estáticos)](#️-arrays-arreglos-estáticos)
  - [Enums (Enumeraciones)](#-enums-enumeraciones)
  - [Structs (Estructuras de Datos)](#-structs-estructuras-de-datos)
  - [Directivas del Sistema (@)](#️-directivas-del-sistema-)
  - [Salida por Serial](#️-salida-por-serial)
- [Ejemplos](#-ejemplos)

---

## ✨ Características Principales
* **Sintaxis amigable:** Basado en Lua, elimina el exceso de símbolos para una lectura clara.
* **Tipos explícitos:** Optimiza la memoria de tu microcontrolador usando tipos precisos (`u8`, `u16`, `b1`).
* **Modularidad integrada:** Organiza tu proyecto fácilmente con directivas como `@add`.
* **Cero sobrecarga:** Compila a Arduino nativo para garantizar el máximo rendimiento.

---

## 📂 Modularidad con @add
`@add` copia el contenido del archivo indicado en el punto exacto donde aparece la directiva, antes de compilar. No existe separación de namespaces ni resolución de dependencias: el orden de los `@add` es el orden del código final.

**`esp32_pins.ty`**
```ty
-- Pines digitales
const D2  : u8 = 2
const D4  : u8 = 4
const D5  : u8 = 5
const D14 : u8 = 14
const D18 : u8 = 18
const D19 : u8 = 19
const D21 : u8 = 21
const D22 : u8 = 22

-- Pines analógicos
const A0 : u8 = 36
const A3 : u8 = 39
const A6 : u8 = 34
const A7 : u8 = 35

-- Alimentación (referencia, no usables como GPIO)
const V33  : u8 = 0   -- 3.3V
const GND  : u8 = 0
const VUSB : u8 = 0   -- 5V desde USB
```

**`main.ty`**
```ty
@add(esp32_pins.ty)   -- D2, A0, etc. ya están disponibles aquí

fun @setup() =
  @pin_mode(D2,  OUTPUT)
  @pin_mode(D14, INPUT_PULLUP)
  @pin_mode(A0,  INPUT)
end
```

> `@add` no protege contra redefiniciones. Si dos archivos declaran la misma constante, el compilador lanzará un error. El orden de los `@add` importa.

---

## 📝 Guía de Sintaxis

### Reglas del Lenguaje
*   **Sensibilidad a Mayúsculas:** Tightny es **case-sensitive**. `Variable` y `variable` son distintas. Todas las palabras clave (`if`, `while`, `fun`, etc.) deben escribirse en minúsculas.
*   **Identificadores:** Deben comenzar con una letra o guion bajo (`_`), seguidos de letras, números o guiones bajos. Los nombres que comienzan con `@` están reservados para directivas del sistema.
*   **Comentarios:**
    *   Una línea: `-- comentario`
    *   Multilínea: `--[[ comentario largo ]]`

### Variables y Constantes
Tightny utiliza una sintaxis clara para la declaración de datos. Por defecto, la asignación de variables crea una **copia** del valor, no una referencia.

```ty
const PIN_SENSOR_TEMP : u8  = A0   -- Sensor NTC en pin analógico
const UMBRAL_ALTO     : u16 = 800  -- Valor ADC (~75°C) que activa alarma
const UMBRAL_BAJO     : u16 = 400  -- Valor ADC (~30°C) que la desactiva

var alarma_activa : b1  = 0
var ultimo_valor  : u16 = 0

var umbral : u16 = UMBRAL_ALTO   -- copia independiente, ajustable en runtime
umbral = umbral - 50       -- no afecta a UMBRAL_ALTO
```

### Tipos de Datos
Soporta tipos con tamaño explícito para un control total de la memoria. Además de los decimales, puedes usar literales **binarios** y **hexadecimales**, ideales para manipular registros y máscaras de bits:

| Tipo | Descripción | Rango / Ejemplo |
| :--- | :--- | :--- |
| `b1` | Booleano / Bit | 0 a 1 |
| `u8`, `u16`, `u32` | Enteros sin signo | `0xAF`, `0b1010`, `'A'` |
| `i8`, `i16`, `i32` | Enteros con signo | 8, 16, 32 bits |

*   **Caracteres (`' '`):** Los literales de un solo carácter se tratan como un tipo `u8` (valor ASCII). Útiles para protocolos Serial y comandos de hardware (ej. `'A'`, `'\n'`).
*   **Binarios (`0b`):** Útiles para ver la posición exacta de los bits (ej. `0b10100000`).
*   **Hexadecimales (`0x`):** Estándar para direcciones de memoria y colores (ej. `0xFF0000`).

### 🔄 Conversión de Tipos (Casting)
Tightny es estrictamente tipado. Para convertir valores entre diferentes tamaños de bits, se utiliza la directiva `@as`, garantizando que cada conversión sea explícita e intencional.

```ty
-- El ADC devuelve u16 (0-1023). Para calcular porcentaje necesitamos
-- operar en u32 para evitar overflow antes de truncar el resultado.
var raw       : u16 = @analog_read(A0)
var porcentaje : u8 = @as(u8, (@as(u32, raw) * 100) / 1023)
```

### 🔢 Operadores
Tightny ofrece un conjunto completo de operadores optimizados para legibilidad y manipulación de hardware.

*   **Aritméticos:** `+`, `-`, `*`, `/`, `%` (módulo). La división `/` entre enteros siempre trunca hacia abajo (floor).
*   **Asignación Compuesta:** `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.
*   **Lógicos (Estilo Lua):** `and`, `or`, `not`. Evitan la confusión de símbolos y mejoran la lectura.
*   **Comparación:** `==`, `!=`, `<`, `>`, `<=`, `>=`.
*   **Bitwise (Hardware):** `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (L-Shift), `>>` (R-Shift).

### Estructuras de Control
Inspiradas en Lua para mayor legibilidad, eliminando la necesidad de paréntesis en las condiciones.

```ty
-- Condicionales: activar ventilador según temperatura
var temp : u16 = @analog_read(A0)

if temp > 800 then
  @analog_write(PIN_FAN, 255)    -- velocidad máxima
  @digital_write(PIN_LED_ROJO, HIGH)
elif temp > 600 then
  @analog_write(PIN_FAN, 180)    -- velocidad media
  @digital_write(PIN_LED_ROJO, LOW)
else
  @analog_write(PIN_FAN, 0)
  @digital_write(PIN_LED_ROJO, LOW)
end

-- Bucle: esperar hasta que el sensor esté listo o timeout
var inicio : u32 = @millis()
while @digital_read(PIN_SENSOR_RDY) == LOW do
  if (@millis() - inicio) > 1000 then
    break    -- salir por timeout
  end
  @delay(10)
end

-- Bucle for: tomar 8 lecturas para promedio de ruido ADC
var suma : u32 = 0
for var i : u8 = 0 while i < 8 next i = i + 1 do
  var lectura : u16 = @analog_read(A0)
  if lectura == 0 then
    continue  -- ignorar lecturas nulas
  end
  suma += @as(u32, lectura)
end
var promedio : u16 = @as(u16, suma / 8)

-- Switch: máquina de estados de un sistema de riego
switch estado_riego do
  case 0 then                              -- IDLE
    if humedad < UMBRAL_SECO then
      estado_riego = 1
    end
  case 1 then                              -- REGANDO
    @digital_write(PIN_BOMBA, HIGH)
    if humedad >= UMBRAL_HUMEDO then
      estado_riego = 2
    end
  case 2 then                              -- ENFRIAMIENTO
    @digital_write(PIN_BOMBA, LOW)
    if (@millis() - tick_enfriamiento) > 5000 then
      estado_riego = 0
    end
  else
    @digital_write(PIN_BOMBA, LOW)         -- falla segura
    estado_riego = 0
end
```

### Funciones y Pasaje de Parámetros
Las funciones pueden devolver valores o ser `void` (si no se especifica tipo de retorno). El manejo de argumentos es explícito:

*   **Por copia (default):** El valor se copia. Los cambios internos no afectan al original.
*   **`var` (Lectura/Escritura):** Puntero que permite modificar la variable original.
*   **`const` (Solo Lectura):** Puntero optimizado que garantiza que el original no será modificado.

```ty
-- Escalar velocidad de ventilador según temperatura (var: modifica el duty cycle original)
fun ajustar_velocidad(var duty : u8, const temp : u16) =
  if temp > 800 then
    duty = 255
  elif temp > 600 then
    duty = 180
  else
    duty = 80
  end
end

-- Leer promedio de N muestras ADC (const: solo lectura del pin)
fun leer_promedio(const pin : u8, const muestras : u8): u16 =
  var suma : u32 = 0
  for var i : u8 = 0 while i < muestras next i = i + 1 do
    suma = suma + @as(u32, @analog_read(pin))
  end
  return @as(u16, suma / @as(u32, muestras))
end
```

### ⋯ Bloques sin implementar (`...`)
Tightny no permite bloques vacíos. Todo bloque debe contener al menos un statement o el token `...`, que marca explícitamente que el cuerpo está pendiente de implementación. El compilador acepta `...` pero emite un warning en tiempo de compilación.

```ty
-- OK: compila con warning "on_collision no implementado"
fun on_collision() =
  ...
end

-- OK: rama pendiente explícita
switch estado do
  case 0 then
    @digital_write(D2, HIGH)
  case 1 then
    ...   -- pendiente
end

-- Error: bloque vacío no permitido
fun on_collision() =
end
```

> Un bloque vacío es siempre un error. `...` es la única forma válida de dejarlo pendiente intencionalmente.

### 🗄️ Arrays (Arreglos Estáticos)
Colecciones de tamaño fijo conocidas en tiempo de compilación. Usan una sintaxis limpia inspirada en Zig. Puedes obtener la cantidad de elementos usando la directiva `@len`.

```ty
-- Buffer circular para suavizar lecturas de un sensor ultrasónico (HC-SR04)
var distancias : [8]u16 = [0, 0, 0, 0, 0, 0, 0, 0]

for var i : u8 = 0 while i < @len(distancias) next i = i + 1 do
  distancias[i] = @analog_read(PIN_ECHO)
  @delay(10)
end

-- Calcular promedio del buffer
var suma : u32 = 0
for var i : u8 = 0 while i < @len(distancias) next i = i + 1 do
  suma = suma + @as(u32, distancias[i])
end
var distancia_cm : u16 = @as(u16, suma / @len(distancias))
```

### 🏷️ Enums (Enumeraciones)
Los `enum` permiten definir un conjunto de constantes relacionadas de forma limpia, ideales para máquinas de estados. Internamente, el compilador asigna valores autoincrementales empezando desde `0`.

```ty
enum EstadoRiego =
  IDLE,
  REGANDO,
  ENFRIAMIENTO,
  ERROR
end

var estado_actual : EstadoRiego = EstadoRiego.IDLE

fun actualizar_sistema() =
  switch estado_actual do
    case EstadoRiego.IDLE then
      ...
    case EstadoRiego.REGANDO then
      ...
  end
end
```

### 📦 Structs (Estructuras de Datos)
Para agrupar datos relacionados. En Tightny, los structs son contenedores puros (estilo C) sin métodos internos, lo que mantiene el lenguaje ligero y predecible.

```ty
struct Motor =
  var pin_pwm   : u8
  var pin_dir_a : u8
  var pin_dir_b : u8
  var velocidad : u8   -- 0-255
end
```

**Inicialización:** Si se declara una variable de tipo struct sin valor explícito, todos sus campos se inicializan en `0` automáticamente (zero-init). Esto garantiza que no existan campos con valores indeterminados en memoria.

```ty
-- Zero-init implícita: motor detenido, pines en 0
var motor_izquierdo : Motor

-- Literal de struct: configuración completa al declarar
var motor_derecho : Motor = { pin_pwm: 5, pin_dir_a: 6, pin_dir_b: 7, velocidad: 0 }
```

```ty
fun iniciar_motor(var m : Motor, pwm : u8, dir_a : u8, dir_b : u8) =
  m.pin_pwm   = pwm
  m.pin_dir_a = dir_a
  m.pin_dir_b = dir_b
  @pin_mode(m.pin_pwm,   OUTPUT)
  @pin_mode(m.pin_dir_a, OUTPUT)
  @pin_mode(m.pin_dir_b, OUTPUT)
end

fun mover_motor(const m : Motor, vel : u8, adelante : b1) =
  @digital_write(m.pin_dir_a, adelante)
  @digital_write(m.pin_dir_b, not adelante)
  @analog_write(m.pin_pwm, vel)
end

iniciar_motor(motor_izquierdo, 3, 4, 5)
mover_motor(motor_izquierdo, 200, 1)
```

### 🕹️ Directivas del Sistema (@)
Las funciones nativas de Arduino se acceden mediante el prefijo `@` y usan `snake_case`.

| Tightny | Equivalente C++ |
| :--- | :--- |
| `@pin_mode(pin, mode)` | `pinMode()` |
| `@digital_write(pin, val)` | `digitalWrite()` |
| `@digital_read(pin)` | `digitalRead()` |
| `@analog_read(pin)` | `analogRead()` |
| `@analog_write(pin, val)` | `analogWrite()` |
| `@delay(ms)` | `delay()` |
| `@millis()` | `millis()` |
| `@as(tipo, val)` | Cast explícito |
| `@len(array)` | Longitud de array |
| `@map(val, in_min, in_max, out_min, out_max)` | Escalamiento de enteros (i32) |
| `@div_ceil(a, b)` | División con redondeo hacia arriba |
| `@div_round(a, b)` | División con redondeo al más cercano |

### 🖨️ Salida por Serial
Tightny no implementa un tipo `string` dinámico para evitar el uso de memoria heap. Los literales de texto son válidos **únicamente** como argumentos de las directivas de salida serial.

Para imprimir múltiples valores o "concatenar" información, las directivas `@print` y `@println` son **variádicas**, permitiendo pasar múltiples argumentos de cualquier tipo separados por comas. El compilador se encarga de llamar secuencialmente a las funciones de impresión.

```ty
-- Válido: múltiples argumentos en una sola línea
var temp : u16 = 25
@print("Lectura del sensor: ", temp, " grados Celsius")
@println() -- Salto de línea vacío

-- Válido: uso de expresiones dentro del print
@println("El doble de la temperatura es: ", temp * 2)

-- Inválido: no existe el tipo string ni la concatenación con '+'
var msg : string = "hola"       -- error de compilación
@print("Valor: " + temp)        -- error de compilación
```

> **Nota:** Los literales de texto se almacenan en la memoria Flash (PROGMEM) en tiempo de compilación para ahorrar RAM.

---

## 🚀 Ejemplos

Aquí puedes ver cómo se estructura un proyecto básico en Tightny.

### Definiendo Constantes y Módulos
Puedes estructurar las definiciones de tu hardware en archivos separados.

**`boolean.ty`**
```ty
const FALSE 0
const TRUE  1
```

**`pin_mode.ty`**
```ty
const INPUT 0
const OUTPUT 1 
const INPUT_PULLUP 2
const INPUT_PULLDOWN 3
```

**`state.ty`**
```ty
const LOW 0
const HIGH 1
```

### El Archivo Principal
Un ejemplo completo de cómo declarar pines, usar funciones nativas del sistema (`@`) y manejar lógica de tiempo sin bloquear el procesador (equivalente a `millis()` en Arduino).

**`main.ty`**
```ty
@add(boolean.ty)
@add(state.ty)
@add(pin_mode.ty)

const LED_AZUL  : u8 = 2
const LED_VERDE : u8 = 18
const LED_ROJA  : u8 = 5
const BUZZER    : u8 = 4
const BUTTON    : u8 = 15

var ultimoTick   : u32 = 0
var intervalo    : u16 = 300
var estadoBuzzer : b1   = FALSE

fun @setup() =
  @pin_mode(LED_AZUL,  OUTPUT)
  @pin_mode(LED_VERDE, OUTPUT)
  @pin_mode(LED_ROJA,  OUTPUT)
  @pin_mode(BUZZER,    OUTPUT)
  @pin_mode(BUTTON,    INPUT_PULLUP)
end

fun @loop() =
  if @digital_read(BUTTON) == LOW then
    @digital_write(LED_AZUL,  HIGH)
    @digital_write(LED_VERDE, HIGH)
    @digital_write(LED_ROJA,  LOW)
    if (@millis() - ultimoTick >= intervalo) then
      ultimoTick = @millis()
      estadoBuzzer = not estadoBuzzer -- alterna on/off
      @digital_write(BUZZER, estadoBuzzer)
    end
  else
    @digital_write(LED_AZUL,  LOW)
    @digital_write(LED_VERDE, LOW)
    @digital_write(LED_ROJA,  HIGH)
    @digital_write(BUZZER, LOW)
    estadoBuzzer = FALSE
  end
end
```
