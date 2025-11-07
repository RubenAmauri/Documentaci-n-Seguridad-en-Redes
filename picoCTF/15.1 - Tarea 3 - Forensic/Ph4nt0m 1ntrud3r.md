## Descripción
A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!Find the PCAP file here [Network Traffic PCAP file](https://challenge-files.picoctf.net/c_verbal_sleep/4d25aca04e2409ba0d917d8ed27d49c6fb616ff9603fa3926712cce623a3d7f5/myNetworkTraffic.pcap) and try to get the flag.
## Solución
- Descargar el archivo .pcap.
- Abrir el archivo en wireshark.
- Usar el filtro de "time", para desplegar los paquetes por tiempo
- Ahora, a partir de un paquete, dentro de ellos empieza a revelarse un mensaje en base64
- Juntar esos mensajes encriptados y usar una herramienta como cyberchef para desencriptarlo.
- Así obtuvimos la bandera.
## Notas adicionales
## Referencias