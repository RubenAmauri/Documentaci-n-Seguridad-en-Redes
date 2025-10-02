## Descripción
Alright, enough of using my own encryption. Flask session cookies should be plenty secure! [server.py](https://mercury.picoctf.net/static/cae5577e6b8f86e17d7884723204f61e/server.py) [http://mercury.picoctf.net:6259/](http://mercury.picoctf.net:6259/)
## Solución
- Abrir la página.
- Nos da una pista sobre una cookie con la que empezar.
- Al ingresarla se crea la primer cookie, la cual tiene un valor alfanumerico.
- Al parecer está cifrado con flask.
- Usamos comando:
``` zsh
echo [valor_de_la_cookie] | base64 -d 
```
- Lo que nos da una salida que nos indica dos cosas: 
	- La galleta se llama "very_auth".
	- El valor es snickerdoodle (lo que ingresamos en la página).
- Leemos el código proporcionado con cat.
- Nos damos cuenta de que hay un arreglo con los posibles valores que puede tener una cookie en el sitio.
- Hay una función que toma un valor aleatorio de ese arreglo para convertirlo en "llave secreta".
- Hay otra función que verifica ese valor y si pasa el chequeo, nos manda a flag.html.
- Copiamos todas las posibles cookies a un archivo de texto nuevo, usaremos el editor de texto pluma.
- Con el editor usaremos la herramienta reemplazar, para darle más legibilidad a las galletas.
- Ahora con nuestro ambiente virtual con flask-unsign instalado, vamos a mandar un ataque de fuerza bruta:
	- Tomamos el valor de la cookie desde cookie editor y lo dejamos en el portapapeles.
	- Usamos comando *flask-unsign --unsign --cookie "valor_de_la_cookie" --wordlist \[archivo_con_lista_de_palabras]*.
	- Con eso nos da el valor con el que firmada la cookie, de la lista que le pasamos.
- Ahora forjaremos la cookie con *sign*:
	- Usaremos comando *flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret "palabra_firmada"*.
	- Con eso, nos debería arrojar el valor de la cookie firmada.
- Ahora haremos un curl a la página para mandarle la cookie, usaremos modificador -s para que sea silencioso y -H para mandarle el valor.
``` zsh
curl -s [url] -H "Cookie: session=[valor_de_la_cookie_firmada]" | grep pico
```
- Eso ya nos arrojó la bandera.

## Notas adicionales
- Necesitamos instalar una herramienta llamada flask-unsign, la cual nos ayudará:
	- La herramienta se instala con pip, así que crearemos un ambiente virtual de python para poder instalar la herramienta.
## Referencias
