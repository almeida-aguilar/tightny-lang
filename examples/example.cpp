#include <stdint.h>

const int32_t led = 13;
const int32_t boton = 2;
int32_t contador = 0;
int32_t limite = 10;

void setup() {
    pinMode(led, OUTPUT);
    pinMode(boton, INPUT_PULLUP);
}

void loop() {
if ((digitalRead(boton) == LOW)) {
    digitalWrite(led, HIGH);
    delay(300);
    digitalWrite(led, LOW);
    delay(300);
    contador = (contador + 1);
}
else {
    digitalWrite(led, LOW);
    contador = 0;
}
}