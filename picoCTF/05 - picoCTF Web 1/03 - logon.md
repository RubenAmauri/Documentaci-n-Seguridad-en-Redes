## Descripción
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/13594/` ([link](https://jupiter.challenges.picoctf.org/problem/13594/)) or http://jupiter.challenges.picoctf.org:13594
## Solución
- Entrar a la página.
- La página sólo comprueba la contraseña del usuario *Joe*.
- Al entrar con cualquier otro usuario con cualquier contraseña, se crean las cookies del sitio en tu dispositivo.
- Con ayuda de las dev tools del navegador edge, logré llegar a las cookies del sitio, cambiando los permisos del usuario actual.
- Cambiando el valor de *admin* de *false* a *true* y luego recargando la página, ya se muestra la bandera.
## Notas adicionales
## Referencias