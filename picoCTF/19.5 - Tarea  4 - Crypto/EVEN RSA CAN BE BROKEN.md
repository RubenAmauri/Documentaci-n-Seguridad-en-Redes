## Descripción
This service provides you an encrypted flag. Can you decrypt it with just N & e?Connect to the program with netcat:`$ nc verbal-sleep.picoctf.net 61681`The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/2b0f68c54cfcb2dafd4ca90c4abcbe73c208f09edf65af336fc7023e1c1314ca/encrypt.py).
## Solución
- Conectarse al netcat y descargar el archivo.
- Con el código fuente podemos ver los métodos que se usaron para encriptar la llave.
- Elaboré un script para decodificar el mensaje:
  ``` python
  def long_to_bytes(n):

    """Convierte un número largo a bytes"""

    if n == 0:

        return b'\x00'

    byte_length = (n.bit_length() + 7) // 8

    return n.to_bytes(byte_length, 'big')

  

def extended_gcd(a, b):

    """Algoritmo extendido de Euclides"""

    if a == 0:

        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1

    y = x1

    return gcd, x, y

  

def inverse(e, phi):

    """Calcula el inverso modular"""

    gcd, x, y = extended_gcd(e, phi)

    if gcd != 1:

        raise ValueError("El inverso modular no existe")

    return (x % phi + phi) % phi

  

# Parámetros RSA

p = 11548176201127249454922191404210383905809576604178150315165078689589889352773013293616511860689151517394130159112102250110630665699584441149368588948352281

q = 2

e = 65537

  

# Calcular clave privada

phi_n = (p-1) * (q-1)

d = inverse(e, phi_n)

  

# Mensaje cifrado

encrypted_message = 12840715242169225954349712198824255327218690098764059422264478212193143821577443676165177331045193483391948599787337580601807221043992646425524833661604577

  

# Descifrar

n = p * q

decrypted_message = pow(encrypted_message, d, n)

  

# Convertir a texto

try:

    plaintext = long_to_bytes(decrypted_message).decode('utf-8')

    print(f"Mensaje descifrado: {plaintext}")

except Exception as e:

    print(f"Error al decodificar: {e}")

    print(f"Número descifrado: {decrypted_message}")

    print(f"Bytes: {long_to_bytes(decrypted_message)}")
  ```
  - Al correrlo conseguí la bandera.
## Notas adicionales
- Algo que hay que notar, es que el valor "N" siempre entrega un valor par, lo cual lo hace vulnerable, ya que es fácilmente divisible entre 2
- Tuve muchos problemas con el simple hecho de copiar y pegar en el editor nano, ya que al pegar números muy grandes había problemas, también tuve problemas usando la librería "crypto" de python, así que le pedí a una ia que modificara el  código que tenía para que funcionara sin dependencias.
## Referencias