## Descripción
I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :) I heard templating is a cool and modular way to build web apps! Check out my website [here](http://shape-facility.picoctf.net:64659/)!
## Solución
- Abrimos el sitio web.
- Intentamos con el mismo código que en SSTI1.
- Este nuevo reto bloqueaba cierto tipo de caracteres, por lo que tuvimos que usar un código que le hiciera bypass a la nueva seguridad.
- Con este nuevo código hacemos cat flag y encontramos la bandera.
## Notas adicionales
## Referencias