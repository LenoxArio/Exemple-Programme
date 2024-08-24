from machine import Pin
from ir_tx.nec import NEC

pin = Pin(15, Pin.OUT, value=0) #Définir le pin pour l'émeteur
irb = NEC(pin, 38000) #Définir le signal en encodage NEC

def send_ir_signal(addr, data):
    irb.transmit(addr, data, toggle=0, validate=True) #Envoie le signal IR avec l'adresse (0xDF00) et le data (0x1C)


# Exemple d'envoi de signal IR avec l'adresse 0xDF00 et les données 0x1C
send_ir_signal(0xDF00, 0x1C)

