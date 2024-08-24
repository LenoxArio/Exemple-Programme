import machine
import time

# Configuration des broches UART (TX: GP0, RX: GP1)
uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

while True:
    if uart.any():
        data = uart.readline()
        print(data.decode().strip())
    time.sleep(0.1)

