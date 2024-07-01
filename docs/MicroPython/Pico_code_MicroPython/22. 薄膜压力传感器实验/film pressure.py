'''
 * Keyes Starter Kit for Raspberry Pi Pico
 * lesson 22
 * Film pressure sensor
'''
import machine
import utime

film = machine.ADC(1)
while True:
    value = film.read_u16()
    print(value)
    utime.sleep(0.1)
