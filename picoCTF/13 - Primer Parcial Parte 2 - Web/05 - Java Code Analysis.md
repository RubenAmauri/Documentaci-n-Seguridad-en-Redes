## Descripción
BookShelf Pico, my premium online book-reading service. I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book! Here are the credentials to get you started:

- Username: "user"
- Password: "user"

Source code can be downloaded [here](https://artifacts.picoctf.net/c/479/bookshelf-pico.zip). Website can be accessed [here!](http://saturn.picoctf.net:59503/).
## Solución
- Abrir la pagina.
- Entrar con las credenciales que otorga pico.
- Inspeccionar la página, buscaremos el token jwt.
- Gracias a un decodificador, cambiaremos los valores del token, para darnos permisos de administrador.
- Con los permisos podremos escoger el libro 'flag', el cual contiene la bandera.
## Notas adicionales
## **Referencias**