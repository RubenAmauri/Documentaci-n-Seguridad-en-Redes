## Descripción
We received an encrypted message. The modulus is built from primes large enough that factoring them isn’t an option, at least not today. See if you can make sense of the numbers and reveal the flag. Download the [message](https://challenge-files.picoctf.net/c_amiable_citadel/d75bf3f0753b354c1fabcaec0bdeb5902d67448835d57a0b0b268560a19f16a3/message.txt).
## Solución
- Descargar el archivo.
- Al analizar los valores, vi que podía usar un ataque para desencriptar ese código
- Escribí un script que utilizara un coppersmith attack para descifrar el mensaje:
  ``` python
  import gmpy2

e = 20
c = 64063743081040685750056670209627408039666134432614898981914985563770727598347289989275044441930023407989265333336298950685280168500>

root , exact = gmpy2.iroot(c,e)

if not exact:
        print("404 NOT FOUND")
print(root)

print(root.to_bytes((root.bit_length()+7)//8))
print(int(root).to_bytes((root.bit_length()+7)//8,'big').decode())
  ```
  - Al correrlo conseguí la bandera.
## Notas adicionales
- El valor "e" se salía de lo común, era demasiado pequeño, eso hace el encriptado muy vulnerable a un  "coppersnith attack"
## Referencias
