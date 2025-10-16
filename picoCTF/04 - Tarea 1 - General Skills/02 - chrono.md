## Descripción
How to automate tasks to run at intervals on linux servers?Use ssh to connect to this server:

```
Server: saturn.picoctf.net
Port: 51319
Username: picoplayer 
Password: H9RmN0m18U
```
## Solución
- Conectarse al ssh con usuario y contraseña.
- Hacer un cat a /etc/crontab.
- Ahí estaba la bandera.
## Notas adicionales
- Crontab es donde se encuentran las tareas automatizadas en un servidor ssh linux
## Referencias