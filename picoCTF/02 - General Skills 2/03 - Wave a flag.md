## Descripción
Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm) has extraordinarily helpful information...
## Solución
- Descargué el archivo con wget
- Di permisos de ejecución al archivo "warm" con *chmod +x*
- Ejecuté el archivo con *./warm*
- Al ejecutarlo, me mencionó que le agregara un *-h* para mostrar el archivo de ayuda de tal programa, donde estaba la bandera.
## Notas adicionales
- chmod - cambia los permisos del archivo.
- chmod +x - da permisos de ejecución al archivo.
- . - *current directory* 
- ./[archivo] - ejecutar [archivo] en el directorio actual
- -h o --help - para ver el archivo de ayuda de algún comando o archivo(No todos lo incluyen).
## Referencias
