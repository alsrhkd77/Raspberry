import RPi.GPIO as GPIO
from lirc import LircdConnection
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
ON = "on"
OFF = "off"

with LircdConnection("airconditionor") as conn:
    while (True):
        codeIR = conn.readline()
        if len(codeIR) != 0:
            print(codeIR)
        if codeIR == ON:
            GPIO.output(24, True)
        elif codeIR == OFF:
            GPIO.output(24, False)
