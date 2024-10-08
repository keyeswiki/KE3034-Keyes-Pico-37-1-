'''
 * Keyes Starter Kit for Raspberry Pi Pico
 * lesson 40
 * Avoiding alarm
'''
from machine import Pin
import time

buzzer = Pin(16, Pin.OUT)
sensor = Pin(15, Pin.IN)
while True:
    buzzer.value(not(sensor.value()))
    time.sleep(0.01)