#Communication protocol (subscriber end) for the Raspberry Pi to the PC to
#send GUI info

import paho.mqtt.client as mqtt
import time
import serial
import pdb

class guiSensorDataReceiver(object):
    """Class accepting the sensor inputs from the rPi and translating it into lists"""

    def __init__(self):
        global broker
        broker = "143.215.100.24" #Always set this to the IP addr of the RPi
        global port
        port = 1883
        global topic
        topic = "guiSensorData"
        global sensorData
        sensorData = {'Air Quality': 0.0, 'Infrared Temp Sensor': 0.0, 'Gas Content Sensor': 0.0}
        global tempMsg
        tempMsg = 'nothing.'
        global client



    def on_connect(client, userdata, rc):
        print("Connected with result code "+str(rc))

        client.subscribe(broker)

    def on_message(client, userdata, msg):
        print(msg.topic +" "+str(msg.payload))

        tempMsg = (msg.topic +" "+str(msg.payload)+"DePkg")

        return tempMsg

    def dataPkg(self):

        testString = tempMsg
        print('I get here with ')
            #testString = data.split(",")
        print(tempMsg)
            #sensorData['AirQuality']
            #sensorData['IR Temp']
            #sensorData['Gas Content']

    def main(self):

        print(topic)
        client = mqtt.Client()
        on_connect = client.on_connect
        on_message = client.on_message
        client.connect(broker,port)
        client.subscribe(topic)
        print(tempMsg)    #For debugging purposes
        print(client.on_message)
        print(tempMsg)   #For debugging purposes
        self.dataPkg()

        client.loop_forever()



if __name__ == "__main__":
    guiData = guiSensorDataReceiver()
    guiData.main() #Assigns events to dictionaries
