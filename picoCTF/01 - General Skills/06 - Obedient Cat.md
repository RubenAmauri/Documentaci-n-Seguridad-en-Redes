## Descripción
This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/2d24d50b4ebed90c704575627f1f57b2/flag).
## Solución
- Descargar el archivo en la terminal con wget
- ls para ver el nombre del archivo ("flag")
- Usar el comando cat en el archivo 'flag'
``` Terminal
RubenAmauri-picoctf@webshell:~$ $ wget https://mercury.picoctf.net/static/2d24d50b4ebed90c704575627f1f57b2/flag
-bash: $: command not found
RubenAmauri-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/2d24d50b4ebed90c704575627f1f57b2/flag
--2025-09-01 17:16:24--  https://mercury.picoctf.net/static/2d24d50b4ebed90c704575627f1f57b2/flag
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34 [application/octet-stream]
Saving to: 'flag'

flag                                                     100%[==================================================================================================================================>]      34  --.-KB/s    in 0s      

2025-09-01 17:16:24 (20.5 MB/s) - 'flag' saved [34/34]

RubenAmauri-picoctf@webshell:~$ ls
README.txt  file  flag
RubenAmauri-picoctf@webshell:~$ cat flag
picoCTF{s4n1ty_v3r1f13d_f28ac910}
```
## Notas adicionales
- **wget** - para descargar archivos en la terminal
- **cat** - Para concatenar archivos a salida estándar (Mostrar su contenido).
- **cat -n** - 
## Referencias