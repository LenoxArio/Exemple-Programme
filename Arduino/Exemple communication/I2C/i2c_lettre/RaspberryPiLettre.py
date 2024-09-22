from smbus import SMBus

addr = 0x8  # adresse du périphérique sur le bus I2C
bus = SMBus(1)  # indique /dev/ic2-1

message = "hello"

# Envoyer chaque caractère du message
for char in message:
    bus.write_byte(addr, ord(char))  # envoyer le caractère en tant que valeur ASCII
input("Appuyez sur Entrée pour quitter")
