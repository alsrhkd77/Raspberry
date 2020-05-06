import serial

con = serial.Serial('/dev/ttyS0', 9600)  # 라즈베리파이 1, 2인 경우 /dev/ttyAMA0
while True:
    text = input("Input any text message: ")
    text = text + '\r\n'
    text = bytes(text.encode("utf-8"))
    con.write(text)
