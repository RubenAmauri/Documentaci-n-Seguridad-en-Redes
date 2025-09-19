## Descripción
This website can be rendered only by **picobrowser**, go and catch the flag! `https://jupiter.challenges.picoctf.org/problem/26704/` ([link](https://jupiter.challenges.picoctf.org/problem/26704/)) or http://jupiter.challenges.picoctf.org:26704
## Solución
- Entrar a la página desde el navegador.
- Inspeccionar el código fuente. Parece que no hay nada en él.
- Volver a la página, darle click al botón **flag** y volver a inspeccionar el código fuente. Ahora sí hay un cambio.
- En el código "nuevo" se da el indicio de que la bandera no puede ser vista si se usa el User-Agent *picobrowser* (También en la página lo decía).
- Desde linux, usamos *curl \[URL de la página] -H "User-Agent:picobrowser"*, lo cual nos da el código de la página siendo accedido desde el agente picobrowser.
- En ese código se podía encontrar la bandera.
## Notas adicionales
- User-Agent es la forma en que la página sabe desde dónde estás accediendo; gracias a él las páginas pueden ser vistas de otra forma, por ejemplo, en el celular, en una tablet o en una PC.
- curl - Es un comando de linux que descargué en la terminal usando *apt update && apt install -y curl*. Nos sirve precisamente para ver el código de una página con su dirección url. En este caso lo usamos con ayuda de su comando *-H* (o --header), y permite añadir un encabezado personalizado a la petición, como "User-Agent" .
## Referencias
- [curl Command in Linux with Examples - GeeksforGeeks](https://www.geeksforgeeks.org/linux-unix/curl-command-in-linux-with-examples/)**