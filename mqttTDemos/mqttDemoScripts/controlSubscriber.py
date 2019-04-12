import clientObjClass as cli
import pdb


class controlSubscriber(object):

    def __init__(self):
        self.__connectionStatus = False
        clientObj = cli.clientObjClass()
        self.__clientObj = clientObj
        self.__guiDataPreParse = ''
        self.__sensorDataPostParse = {'AirQualitySensor': '', 'InfraredTempSensor' : '', 'GasContentSensor' : ''}


    def getClient(self):
        a = self.__clientObj.getClient()
        return(a)

    def buildSubscriber(self):
        self.__clientObj.createClient()

    def addSubscriberParams(self,broker,port,topic):
        self.__clientObj.setClientParams(broker,port,topic)

    def connectSubscriber(self):
        self.__clientObj.connectClient()
        self.__connectionStatus = True


    def receiveMvmnt(self):
        subscribedData = self.__clientObj.printFromSubscriber()
        print('subscribed Data')
        self.__sensorDataPreParse = subscribedData.payload
        return(self.__sensorDataPreParse)

    def foreverLoopClient(self):
        self.__clientObj.loopClientForever()

    def startSubscribeLoop(self,indicator):
        self.__clientObj.startLoop(indicator)

    def stopSubscribeLoop(self):
        self.__clientObj.endLoop()

    def parseGuiData(self,data):
        self.__sensorDataPreParse = data
        data = str(data)  #Due to Python 3 update, information needs to be cast as a string again
        sensorList = data.split(",")

        if 'aQS' in sensorList[0] or 'gCS' in sensorList[1] or 'iRS' in sensorList[2]:

            aQSFloat = sensorList[0]
            aQSFloatData = aQSFloat.split(":")
            self.__sensorDataPostParse['AirQualitySensor'] = aQSFloatData[1]

            iRSFloat = sensorList[1]
            iRSFloatData = iRSFloat.split(":")
            self.__sensorDataPostParse['GasContentSensor'] = iRSFloatData[1]

            gCSFloat = sensorList[2]
            gCSFloatData = gCSFloat.split(":")
            self.__sensorDataPostParse['InfraredTempSensor'] = gCSFloatData[1]

        return(self.__sensorDataPostParse)



    def checkConnection(self):
        return(self.__connectionStatus)

    def checkClientDetails(self):
        details = self.__clientObj.getClientParams()
        return(details)
