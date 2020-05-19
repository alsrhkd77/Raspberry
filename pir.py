import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
pir = 24
GPIO.setup(pir, GPIO.IN)

def loop():
    cnt = 0
    while True:
        cur_stat = GPIO.input(pir)
        if cur_stat == 1:
            cnt += 1
            print("감지됨")
        else:
            print("감지안됨")
        time.sleep(0.5)
    GPIO.cleanup()


try:
    loop()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()