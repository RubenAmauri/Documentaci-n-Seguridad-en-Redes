## Descripción
Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:34561/](http://mercury.picoctf.net:34561/)
## Solución
- Inspeccionar código fuente de la página.
- Puntos clave: GET y POST.
- Al usar *curl -X  GET/POST  [Link de la página]* podíamos ver el código de esa página dependiendo del método HTTP que usara la página en cada método.
- Intentamos con otro método HTTP,  *HEAD*, al usar *curl -X HEAD ...*, la terminal indicó que no podía usarse con -X, y sugirió hacerlo con -I en su lugar.
- Al usar *curl -I HEAD ...*, nos arrojó la bandera.
## Notas adicionales
- Métodos HTTP.
- curl -X - Indica qué método se usará en el curl para solicitar la información
## Referencias