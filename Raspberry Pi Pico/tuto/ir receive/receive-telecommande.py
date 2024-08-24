from sys import platform
import time
import gc
from machine import Pin, freq
from ir_rx.nec import NEC_8, NEC_16, SAMSUNG


irReceive = Pin(2, Pin.IN)

# User callback
def cb(data, addr, ctrl):
    print(f"Data 0x{data:02x} Addr 0x{addr:04x} Ctrl 0x{ctrl:02x}")


def test(proto=0):
    classes = (NEC_8, NEC_16)
    ir = classes[proto](irReceive, cb)  # Instantiate receiver
    try:
        while True:
            time.sleep(5)
            gc.collect()
    except KeyboardInterrupt:
        ir.close()


test(1)
print(s)


