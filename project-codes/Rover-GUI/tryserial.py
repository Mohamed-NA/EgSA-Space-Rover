# Python code transmits a byte to Arduino /Microcontroller

import serial
from ssp import *
import time
import struct

ser = serial.Serial(

    # port='/dev/ttyS0' Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
    port=None,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter = 1
string = b''

data = [6, 77, 8, 9, 0x44, 0x33, 0x11, 0x44]
header = [0x0f, 0xB, 5, 0x08]

y = []
z = ssp_construction(bytearray(header), bytearray(data), len(data))
print(f"z: {z}")

ddd = data_extraction(z, len(data))
print(f"data: {ddd}")

resp = []
type_num = response(bytearray(header), bytearray(data), resp)
x: bytearray
while 1:
    string += struct.pack('B', counter)
    # ser.write(string)
    ser.write(z)
    time.sleep(1)
    # counter += 1
    x = bytearray(ser.read(20))
    print(f"this is x: {x}")
    dd = data_extraction(x, len(data))
    time.sleep(1)
    print(f'this is : {dd}')
