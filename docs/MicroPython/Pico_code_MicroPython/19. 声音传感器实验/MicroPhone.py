'''
 * Keyes Starter Kit for Raspberry Pi Pico
 * lesson 19
 * MicroPhone
'''
import machine
import utime

MicroPhone = machine.ADC(27)
while True:
    value = MicroPhone.read_u16()
    print(value)
    utime.sleep(0.1)