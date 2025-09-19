## Descripción
Can you break into this super secure portal? `https://jupiter.challenges.picoctf.org/problem/56816/` ([link](https://jupiter.challenges.picoctf.org/problem/56816/)) or http://jupiter.challenges.picoctf.org:56816
## Solución
- Abrir la página desde el navegador.
- Inspeccionar la página con dev-tools.
- Nos damos cuenta que el método que verifica la bandera es ilegible, está "obfuscado".
- Usamos un desobfuscador web (ver en referencias) para hacer legible el método.
- En el método está un arreglo que contiene la bandera, pero está en desorden y también hay elementos que no corresponden a la bandera.
- Copiamos el arreglo dentro de la consola en dev-tools.
- Ahora usando la lógica de la sintaxis que llevan las banderas pico, comenzamos a sumar desde la consola las posiciones del arreglo en el orden que pensamos que está la bandera.
- Las suposiciones fueron correctas, el órden que seguimos para armar la bandera era el correcto.
## Notas adicionales
- Obfuscation es un "método" para hacer ilegible alguna parte del código. En este caso se utilizó para esconder una parte del string, que es la que contiene la contraseña.
## Referencias
- [Code Integrity: Code Protection & Code Hardening for Apps](https://jscrambler.com/code-integrity)
- [JS NICE: Statistical renaming, Type inference and Deobfuscation](http://jsnice.org/)