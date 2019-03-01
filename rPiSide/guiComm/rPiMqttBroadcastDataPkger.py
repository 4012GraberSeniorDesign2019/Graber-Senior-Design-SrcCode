
#Communication protocol (BrodcastSide) for the Raspberry Pi back to the PC to send GUI information

import paho.mqtt.client as mqtt
import time
import random

broker = "143.215.100.24" #This will change everytime you reconnect to GTOther (Set it to be the RPi IP addr)
port = 1883
topic = "guiSensorData"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)

#This will stand in place of the sensor data received via serial from
#the Arduino due

while True:
    #AirQualitySensor
    aQS = random.random()
    #InfraredTempSensor
    iRS = random.random()
    #GasContentSensor
    gCS = random.random()
    sensorData= 'aQS: %.2f, iRS: %.2f, gCS: %.2f' %(aQS,iRS,gCS)
    client.publish(topic,sensorData)    
    time.sleep(1)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

