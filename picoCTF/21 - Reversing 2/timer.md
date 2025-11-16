## Descripción
You will find the flag after analysing this apk.
Download [here](https://artifacts.picoctf.net/c/449/timer.apk).
## Solución
- Descargamos el apk.
- La misma página descompiladora del reto anterior, también tiene una opción para descompilar apk.
- Al descompilarlo tendremos todo el proyecto dividido en carpetas.
- Hacemos una búsqueda manual por carpetas conocidas.
- Al final, encontramos la bandera en el directorio sources/com/example/timer/Buildconfig.java.
## Notas adicionales
- NUNCA descompiles un programa con información sensible con una herramienta online, ya que podría quedar expuesta dicha información.
- El mismo reto sugiere otras herramientas que trabajan de manera local, como jadx o mobsf.
## Referencias
- http://www.javadecompilers.com