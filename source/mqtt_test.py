#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time
import json
import random

topic = 'temperature/dht22'
sleep_time = 0.1


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
while True:
    new_state = GPIO.input('PA16')
    if last_state != new_state and new_state:
        print(new_state)
        data = {'temperature': random.randint(-20, 40),
                'humidity': random.randint(0, 100)}
        client.publish(topic, json.dumps(data))
        print('Published...')
    last_state = new_state
    time.sleep(sleep_time)
