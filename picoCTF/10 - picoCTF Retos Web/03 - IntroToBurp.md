## Descripción
Try [here](http://titan.picoctf.net:55245/) to find the flag
## Solución
- Lanzamos la instancia.
- Abrimos burpsuite.
- Activamos la intercepción.
- Hacemos un registro en el sitio con usuarios aleatorios.
- Hacemos forward en burpsuite sin modificar nada.
- En la parte de la verificacion pondremos un valor aleatorio.
- En la intercepcion notaremos una linea que valida la verificacion.
- Borramos esa linea y hacemos forward.
- Obtenemos la bandera.
## Notas adicionales
## Referencias