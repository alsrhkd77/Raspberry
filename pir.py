import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
pir = 11
GPIO.setup(pir, GPIO.IN)

def loop():
    cnt = 0
    while True:
        cur_stat = GPIO.input(pir)
        if cur_stat == 1:
            cnt += 1
            print(GPIO.input(pir))
            print("%d번 감지됨" % cnt)
            time.sleep(1)


try:
    loop()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()