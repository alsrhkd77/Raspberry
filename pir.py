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
        if cur_stat == 1:
            cnt += 1
            print("감지됨")
            detected()
        else:
            print("감지안됨")
            undetected()
        time.sleep(0.5)


def detected():
    GPIO.output(led, 1)


def undetected():
    GPIO.output(led, 1)


try:
    loop()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()