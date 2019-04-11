import clientObjClass as cli
import guiPublisher as guiPub
import pdb
import time
import serial
import random

broker = '143.215.95.16'
port = 1883
topic = 'guiParseTest'
tracker = 0
sensorData = ''

cliePub = guiPub.guiPublisher()

cliePub.buildPublisher()
cliePub.addPublisherParams(broker,port,topic)

cliePub.connectPublisher()

d = cliePub.checkConnection()
c = cliePub.checkClientDetails()

print("Publisher details")
print(c)
print("Publisher is connected: ")
print(d)
pubClient = cliePub.getClient()
print(pubClient)
print('Here in the publisher')


while True:
    #Replace this (below) with the serial reading of the port for the sensor data

    #AirQualitySensor
    aQS = random.random()
    #InfraredTempSensor
    iRS = random.random()
    #GasContentSensor
    gCS = random.random()
    print('Sending this data to the subscriber')
    sensorData= "aQS: %.2f, gCS: %.2f, iRS: %.2f" % (aQS,gCS,iRS)
    time.sleep(1)
    status = cliePub.publishInfo(sensorData)
    #tracker += 1
    #print('At ' + str(tracker) + ' second ' + str(status))
    #newData = cliePub.parseGuiData(sensorData)
    #print('Data parsed into dictionary')
    #print(newData)
    #print('\n')

cliePub.foreverLoopClient()


#cliePub.stopPublishLoop()
