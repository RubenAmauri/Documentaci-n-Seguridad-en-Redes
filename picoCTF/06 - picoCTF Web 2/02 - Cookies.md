## Descripción
Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:17781/](http://mercury.picoctf.net:17781/)
## Solución
- La página consta con una entrada, donde puedes poner varios nombres de "cookies".
- Al ingresar la primera, se crea la primer cookie, con un valor de "0".
- Al editar el valor con cookie editor y guardarlo, nos damos cuenta de que cada que aumentamos el valor de la cookie, cambia el contenido de la pantalla.
- Para no intentar con cada valor de la cookie, prepararemos un ataque intruder con  burpsuite.
- Para generar el ataque, primero accedimos al url que genera la cookie desde firefox en kalilinux.
- Activamos el proxy ya preestablecido "BURP".
- Ahora gracias al proxy, burp puede ver lo que pasa por el navegador.
- Desde burpsuite, en la pestaña *proxy*, podemos ver *https history*, donde buscamos la url con la que estamos trabajando.
- Damos click derecho sobre el url y seleccionamos *send to Intruder*.
- La pestaña *Intruder* cambiará de color, indicando que recibió el url, ahí podemos ver en el código, la línea que se encarga de recibir el valor de la cookie.
- Eliminamos el valor 0 de la cookie y usamos el botón add para que el ataque lo reconozca como la variable a trabajar.
- Le damos como límite el valor 30 y presionamos send atack.
- Revisamos la lista de cada ataque hasta que encontramos la bandera.

## Notas adicionales
## Referencias
