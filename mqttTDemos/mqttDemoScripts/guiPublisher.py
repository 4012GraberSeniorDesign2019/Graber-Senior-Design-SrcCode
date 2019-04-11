import clientObjClass as cli
import pdb
import time
import random

class guiPublisher(object):

    def __init__(self):
        self.__connectionStatus = False
        clientObj = cli.clientObjClass()
        self.__clientObj = clientObj
        self.__sensorDataPreParse = ''
        self.__sensorDataPostParse = {'AirQualitySensor': '', 'InfraredTempSensor' : '', 'GasContentSensor' : ''}

    def getClient(self):
        a = self.__clientObj.getClient()
        return(a)

    def buildPublisher(self):
        self.__clientObj.createClient()

    def addPublisherParams(self,broker,port,topic):
        self.__clientObj.setClientParams(broker,port,topic)

    def connectPublisher(self):
        self.__clientObj.connectClient()
        self.__connectionStatus = True

    def startPublishLoop(self,indicator):
        self.__clientObj.subscribeToTopic()
        status = self.__clientObj.startLoop(indicator)

    def stopPublishLoop(self):
        status = self.__clientObj.endLoop()

    def publishInfo(self,data):
        print('Assigned Sensor Data')
        a = self.__clientObj.publishData(data)
        return(a)

    def parseGuiData(self,data):
        self.__sensorDataPreParse = data

        sensorList = data.split(",")

        if 'aQS' in sensorList[0] or 'gCS' in sensorList[1] or 'iRS' in sensorList[2]:

            aQSFloat = sensorList[0]
            aQSFloatData = aQSFloat.split(":")
            self.__sensorDataPostParse['AirQualitySensor'] = aQSFloatData[1]

            gCSFloat = sensorList[1]
            gCSFloatData = gCSFloat.split(":")
            self.__sensorDataPostParse['GasContentSensor'] = gCSFloatData[1]

            iRSFloat = sensorList[2]
            iRSFloatData = iRSFloat.split(":")
            self.__sensorDataPostParse['InfraredTempSensor'] = iRSFloatData[1]

        return(self.__sensorDataPostParse)

    #def serialReceiving(self):
    #    while True:
    #        while (ser.in_waiting>0):
    #            print("in: "+str(ser.in_waiting))
    #            ser.reset_input_buffer()
    #            time.sleep(.01)
    #        while (ser.out_waiting>0):
    #            print("out: "+str(ser.out_waiting))
    #            ser.reset_output_buffer()
    #            time.sleep(.01)
    #        ser.write(message.encode())
    #        print("message sent")
    #        data = ser.readline()
    #        if data or True:
    #            print(data.decode())
    #        else:
    #            print('nothing')

    def checkConnection(self):
        return(self.__connectionStatus)

    def checkClientDetails(self):
        details = self.__clientObj.getClientParams()
        return(details)

    def foreverLoopClient(self):
        self.__clientObj.loopClientForever()
