import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
pir = 24
led = 23
GPIO.setup(pir, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

def loop():
    cnt = 0
    while True:
        cur_stat = GPIO.input(pir)
        if cur_stat == GPIO.LOW:
            cnt += 1
            detected()
        else:
            undetected()


def detected():
    GPIO.output(led, 1)


def undetected():
    GPIO.output(led, 0)


try:
    loop()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()