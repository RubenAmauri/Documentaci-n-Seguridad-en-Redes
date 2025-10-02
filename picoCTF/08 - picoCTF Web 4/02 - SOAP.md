## Descripción
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?[Web Portal](http://saturn.picoctf.net:54516/)
## Solución
- Entrar al portar proporcionado.
- Inspeccionar código fuente de la página.
- En el código hay un formulario que envía datos a un point llamado /data, a través de un método post.
- Se envía el ID.
- Usaremos burp, viendo que se usan métodos.
- Damos click en todos los botones de la página para generar las peticiones en burpsuite.
- Vamos a hacer uso del repeater para atacar.
- Como valor del ID, solo son permitidos los valores 1, 2 y 3, que son las universidades registradas.
- Usamos ayuda de la IA para crear payloads que ataquen la vulnerabilidad del XXE.
- La vulnerabilidad existe, ahora se usará un nuevo payload que lea archivos del sistema.
- Entre esos archivos se encuentra la bandera.
## Notas adicionales
- XXE - Es una vulnerabilidad que afecta a los parsers XML mal configurados, permitiendo, por ejemplo, al atacante leer archivos del sistema, entre otros ataques.
## Referencias