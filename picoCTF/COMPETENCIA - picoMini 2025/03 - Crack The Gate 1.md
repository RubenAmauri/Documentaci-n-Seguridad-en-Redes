## Solución
- Se inspeccionó el código fuente de la página de login y se encontró un comentario en HTML que contenía un texto cifrado: ``.    
- Se identificó el cifrado como **ROT13**. Al descifrarlo, se obtuvo la instrucción para un bypass: `NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes"`.
- Se analizó el código JavaScript de la página, descubriendo que el login se realizaba a través de una petición `POST` al endpoint `/login` con un cuerpo en formato JSON.    
- Se dedujo que el bypass no eliminaba la necesidad de un usuario existente. La estrategia consistió en combinar un email válido con la cabecera del bypass para saltarse la verificación de la contraseña.    
- Se construyó y ejecutó un comando `curl` que simulaba la petición `POST` a `/login`, incluyendo la cabecera `Content-Type`, la cabecera de bypass `X-Dev-Access` y un cuerpo JSON con el email válido (`ctf-player@picoctf.org`).
``` zsh
curl -X POST \
-H "Content-Type: application/json" \
-H "X-Dev-Access: yes" \
-d '{"email":"ctf-player@picoctf.org","password":"cualquiercosa"}' \
http://amiable-citadel.picoctf.net:51280/login
```
- Al ejecutar el comando, el servidor respondió con un JSON que contenía `success:true` y la bandera.