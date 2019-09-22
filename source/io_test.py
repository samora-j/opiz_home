import OPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.SUNXI)
GPIO.setup('PA16', GPIO.IN, pull_up_down=GPIO.PUD_UP)
last_state = 1
while True:
    new_state = GPIO.input('PA16')
    if last_state != new_state:
        print(new_state)
    last_state = new_state
    sleep(0.05)

