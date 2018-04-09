import RPi.GPIO as GPIO
LedPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, GPIO.HIGH)

def on_off(i):
    if i == '1':
        GPIO.output(LedPin, GPIO.HIGH)
        print('led on')
    else:
        GPIO.output(LedPin, GPIO.LOW)
        print('led off')