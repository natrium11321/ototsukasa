pin_red = 21
pin_yellow = 20
pin_green = 16

import RPI.GPIO as GPIO

def LEDon(color):
    if color not in ["red","yellow","green","r","y","g"]:
        return False
    if color in ["red","r"]:
        pin = pin_red
    elif color in ["yellow","y"]:
        pin = pin_yellow
    elif color in ["green","g"]:
        pin = pin_green
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)

def LEDoff(color):
    if color not in ["red","yellow","green","r","y","g"]:
        return False
    if color in ["red","r"]:
        pin = pin_red
    elif color in ["yellow","y"]:
        pin = pin_yellow
    elif color in ["green","g"]:
        pin = pin_green
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)

def main():
    import time
    for c in ["y","g","r"]:
        LEDon(c)
        time.sleep(3)
    for c in ["y","g","r"]:
        LEDoff(c)
        time.sleep(3)

if __name__ == "__main__":
    main()
