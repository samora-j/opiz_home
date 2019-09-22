#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time
import json
import random
import OPi.GPIO as GPIO
from datetime import datetime

topic = 'home-assistant/opiz/pir-1'
on_sleep_time = 7
off_sleep_time = 0.01

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {}".format(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect( 'fusion', 1883, 60)
client.loop_start()


GPIO.setmode(GPIO.SUNXI)
GPIO.setup('PA16', GPIO.IN, pull_up_down=GPIO.PUD_UP)
last_state = 1
sleep_time = off_sleep_time
while True:
    new_state = GPIO.input('PA16')
    if last_state != new_state:
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
        print('Motion detected: ',date_time) 
        if new_state == 1:
            sleep_time = on_sleep_time
            payload = 'ON'
        else:
            sleep_time = off_sleep_time
            payload = 'OFF'
        client.publish(topic, payload)
        print('State published: ', payload)
    last_state = new_state
    time.sleep(sleep_time)
