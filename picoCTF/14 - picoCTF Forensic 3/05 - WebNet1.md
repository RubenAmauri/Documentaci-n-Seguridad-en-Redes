## Descripción
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.
## Solución
- Descargamos loa archivos.
- Intentamos el mismo procedimiento que con WebNet1, pero no funcionó.
- Abrimos wireshark
- Al abrir el pcap, me di cuenta de que no se mostraban los paquetes http, así que investigando un poco ví cómo configurar la llave para poder verlos.
- En wireshark, fui a las confifuraciones de protocolos y en el de tsl agregué mi archivo de llaves.
- Ahora puedo analizar otros paquetes.
- Siguiendo un stream tsl me encontré la bandera.
## Notas adicionales
## Referencias