## Descripción
Help us test the form by submiting the username as `test` and password as `test!` The website running [here](http://saturn.picoctf.net:51737/).
## Solución
- Abrir la página.
- Intentar iniciar sesión con los datos que proporciona pico.
- Con inspeccionar accedemos a las redirecciones que ha hecho la página.
- Entre ellas hay una que termina con un id=[base64].
- Decodificamos con cyberchef y parece ser la última parte de la bandera.
- Volvemos en la página y encontramos un id diferente.
- Decodificamos y ya tenemos la bandera completa.
## Notas adicionales
## Referencias