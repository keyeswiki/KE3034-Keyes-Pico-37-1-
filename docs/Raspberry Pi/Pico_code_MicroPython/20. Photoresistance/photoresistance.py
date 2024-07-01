'''
 * Keyes Starter Kit for Raspberry Pi Pico
 * lesson 20
 * Photoresistance
'''
import machine
import utime

photoresistance = machine.ADC(28)
while True:
    value = photoresistance.read_u16()
    print(value)
    utime.sleep(0.1)

