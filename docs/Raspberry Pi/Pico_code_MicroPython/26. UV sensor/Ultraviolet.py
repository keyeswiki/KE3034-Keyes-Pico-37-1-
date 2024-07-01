'''
 * Keyes Starter Kit for Raspberry Pi Pico
 * lesson 26
 * UV_sensor
'''
import machine
import utime


sensor = machine.ADC(26)

while True:
    analogVal = sensor.read_u16()
    print(analogVal)
    utime.sleep(0.1)
