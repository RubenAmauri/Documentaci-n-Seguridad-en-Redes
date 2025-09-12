## Descripción
Fix the syntax error in the Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/6/fixme2.py)
## Solución
- Descargar el archivo
- Ejecutar con python3
- Hay un error de sintaxis, al parecer tiene que ver con una asignación
- Era un if en el que se estaba haciendo una asignación en lugar de comparación
- se agrega un =
- Correr de nuevo y ya da la bandera.
## Notas adicionales
- En python, "=" indica asignación, y "\==" indica comparación
## Referencias