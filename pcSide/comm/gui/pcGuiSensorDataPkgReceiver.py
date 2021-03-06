#Communication protocol (subscriber end) for the Raspberry Pi to the PC to
#send GUI info

import paho.mqtt.client as mqtt
import time
import serial
import pdb

broker = "143.215.100.24" #Always set this to the IP addr of the RPi
port = 1883
topic = "guiSensorData"

tempMsg = ''
sensorData = {'Air Quality': 0.0, 'Infrared Temp Sensor': 0.0, 'Gas Content Sensor': 0.0}

def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(broker)

def on_message(client, userdata, msg):
    print(msg.topic +" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker,port)
client.subscribe(topic)
client.on_message

client.loop_forever()
