## Descripción
Why use p and q when I can use more? Connect with `nc jupiter.challenges.picoctf.org 4557`.
## Solución
- Creamos un nuevo script de python para calcular los valores.
- Nos damos cuenta que nos faltan varios valores importantes: tn, p y q.
- Intentamos factorizar n para encontrar p y q, pero nos da demasiados factores.
- Usamos una nueva página para factorizar: *https://www.alpertron.com.ar/ECM.HTM
- Esta página aparte de factorizar, nos da el tn, o sea el totien de euler.
- Con este valor ya podemos desencriptar la bandera con nuestro script.
## Notas adicionales
## Referencias