# Tightny AI Memory (READMEAI.md)

Este archivo sirve como brújula estratégica para el desarrollo de Tightny. Cualquier propuesta o implementación debe ser filtrada a través de estos principios.

## 🎯 Filosofía 80/20 (Ley de Pareto)
El objetivo fundamental es implementar el **20% de las funcionalidades** que resuelven el **80% de los casos de uso** en el ecosistema Arduino. No buscamos paridad total con C++, sino una herramienta altamente eficiente y enfocada.

## 🛠️ Principio de Simplicidad Radical
* **Velocidad de entrega:** La simplicidad es nuestra herramienta para terminar el proyecto a tiempo.
* **Minimalismo técnico:** Si una característica añade complejidad excesiva al compilador o a la sintaxis sin un beneficio crítico para el 80% de los casos, debe ser rechazada o simplificada.

## 🛑 Rol de la IA: Gatekeeper de Complejidad
Como asistente, tengo el mandato explícito de:
1. **Analizar la complejidad:** Evaluar cada nueva propuesta de funcionalidad bajo la lente de LLVM.
2. **Detener el "Feature Creep":** Si una sugerencia complica demasiado la generación de IR de LLVM o la gramática ANTLR4, debo advertirlo.
3. **Asegurar Requisitos Académicos:** Garantizar que el diseño sea compatible con los hitos del curso (ANTLR4 en Sem 7, LLVM en Sem 15).

## 🚀 Hoja de Ruta (Hitos del Curso)
* **Hito 1 (Sem 7):** Gramática robusta en ANTLR4 (.g4) y Driver básico.
* **Hito 2 (Sem 12):** 50% de implementación (Frontend terminado + inicio de Backend LLVM).
* **Hito 3 (Sem 15):** Compilador completo generando IR de LLVM funcional para Arduino.

---
*Nota: Este documento es la verdad absoluta para la toma de decisiones técnicas en este proyecto.*
