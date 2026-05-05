# Ejemplos de código en Tightny

Aquí puedes ver cómo se estructura un proyecto básico en Tightny.

## Definiendo Constantes y Módulos
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

## El Archivo Principal
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
