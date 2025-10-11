## Descripción
Can you login to this website? Try to login [here](http://saturn.picoctf.net:58697/).
## Solución
- Abrir la página.
- Intentar acceder como admin con cualquier contraseña.
- La página indica que no ha sido correcto el inicio, pero te revela la query sql que se usa para buscar los usuarios y contraseñas.
- Usamos *admin' --* como usuario y cualquier contraseña.
- Logramos iniciar sesión, pero no se ve la bandera.
- Está escondido en el código de la página.
## Notas adicionales
## Referencias