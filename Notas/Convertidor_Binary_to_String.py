# Archivo: convertidor.py
import sys

# Verifica si se proporcionó un argumento en la terminal
if len(sys.argv) > 1:
    # El primer argumento (sys.argv[1]) es tu cadena binaria
    binary_string = sys.argv[1]

    # Realiza la conversión
    final_text = "".join(chr(int(c, 2)) for c in binary_string.split())

    # Imprime el resultado
    print(final_text)
else:
    print("Error: Por favor, proporciona la cadena binaria entre comillas.")