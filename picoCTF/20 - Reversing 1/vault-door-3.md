## Descripción
This vault uses for-loops and byte arrays.The source code for this vault is here: [VaultDoor3.java](https://challenge-files.picoctf.net/c_fickle_tempest/856cff883937e1cfe99e7e5b9c2fbbf08232a8135f919b1111615f007a4de03a/VaultDoor3.java)
## Solución
- Analizamos el código.
- La bandera ahora se construye con ciclos, usando otra "clave" para armarla. Algo así como funcionan los de sustitución.
- Usamos javascript para hacer el código línea por línea, así como lo hace python.
- Nos ayudamos de las devtools de firefox para acceder a una consola con javascript.
- Creamos dos variables, una con la constraseña que se sustituirá y otra con el buffer, para indicar el tamaño.
- Ahora copiamos una parte relevante del código fuente, luego agregamos una línea que imprime el buffer y los une en una sola línea (Ya que era un arreglo de caracteres).
- Nuestro código quedaría algo así:
  ``` javascript
  var password = 'jU5t_a_sna_3lpm11g54e_u_4_m4r042';
  var buffer = Array(32);

          for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        
  buffer.join("");
  ```
  - Al imprimir lo último, se nos revela la bandera, solo hay que darle el formato.
## Notas adicionales
## Referencias