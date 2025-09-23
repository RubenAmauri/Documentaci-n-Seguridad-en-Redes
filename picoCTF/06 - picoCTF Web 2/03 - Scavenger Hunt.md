## Descripción
There is some interesting information hidden around this site [http://mercury.picoctf.net:27278/](http://mercury.picoctf.net:27278/). Can you find it?
## Solución
- Abrimos el sitio web desde el navegador.
- Inspeccionamos el código fuente.
- Encontramos en él la primera parte de la bandera.
- Inspeccionando el código fuente, nos pasamos a la hoja de estilos *css*, donde encontramos la segunda parte de la bandera.
- Para la tercer parte, nos dan una pista *How can I keep Google from indexing my website?*, a lo cual respondemos con un robots.txt.
- Indexamos /robots.txt al final del url de la página y accedemos, donde encontramos la tercer parte de la bandera.
- Siguiente pista *I think this is an apache server... can you Access the next flag?*.
- Investigando descubrimos que en el url puede haber otro archivo debido a apache *.htaccess*, el cual es un archivo que guarda los ajustes personalizados del servidor.
- Última pista: *I love making websites on my Mac, I can Store a lot of information there.*
- Los sistemas MacOS guardan un archivo oculto en todos sus directorios: *".DS_Store"*, el cual puede contener mucha información sobre el directorio, como la forma en la que están sorteados los archivos, por ejemplo.
- Al indexar *.DS_Store* al final del URL, podemos acceder a la última parte de la bandera.
## Notas adicionales
## Referencias