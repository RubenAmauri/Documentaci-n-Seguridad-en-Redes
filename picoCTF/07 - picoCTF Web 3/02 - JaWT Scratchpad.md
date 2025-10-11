## Descripción
Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/63090/` or http://jupiter.challenges.picoctf.org:63090
## Solución
- Abrimos la página.
- Intentamos acceder como admin y no deja.
- La página sugiere que te logees como John.
- Eso nos genera un token JaWT (en la cookie).
- Lo decodificamos en una página decodificadora de tokens json.
- Vemos que usa algoritmo HS256.
- Iremos a la terminal, vamos a crear un archivo *jwt.txt*  donde ingresaremos nuestro token.
- Ahora usaremos comando john para procesarlo.
- Encontraremos el token y lo usaremos para convertirlo en el token del admin.
- Al editar la cookie y convertirla en el token del admin descubriremos la bandera.
## Notas adicionales
## Referencias
