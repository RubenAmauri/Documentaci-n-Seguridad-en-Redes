## Descripción
Can you read files in the root file?The system admin has provisioned an account for you on the main server:`ssh -p 54338 picoplayer@saturn.picoctf.net`Password: `vCR2tuwCRm`Can you login and read the root file?
## Solución
- Accedemos al servidor copiando el comando que te ofrece el propio picoCTF
- Al estar dentro, nos damos cuenta de que no podemos hacer mucho, ni un ls.
- Usando *sudo -l* nos damos cuenta de que tenemos permiso de usar el comando *vi* el cual es un editor de texto.
- Usando *sudo vi*, accedemos al vi, desde el cual podemos navegar por los archivos, entre ellos los de la carpeta root.
- Desde la carpeta root encontramos el archivo *flag.txt*, el cual podemos abrir con vi y encontrar la bandera.
## Notas adicionales
## Referencias