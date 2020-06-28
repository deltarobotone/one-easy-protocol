import serial
import time
import sys
import glob
import logging
    
class Protocol(object):
    
    def __init__(self):
        self.gripperopen =  'GRIPPEROPEN'
        self.gripperclose = 'GRIPPERCLOSE'
        self.lighton =      'LIGHTON'
        self.lightoff =     'LIGHTOFF'
        self.lightred =     'RED'
        self.lightgreen =   'GREEN'
        self.lightblue =    'BLUE'
        self.lightyellow =  'YELLOW'
        self.lightmagenta = 'MAGENTA'
        self.lightcyan =    'CYAN'
        self.lightwhite =   'WHITE'
        self.extmotoron =   'EXTMOTORON'
        self.extmotoroff =  'EXTMOTOROFF'
        
class Colour(object):
    
    def __init__(self):
        self.__protocol = Protocol()
        self.red =     self.__protocol.lightred
        self.green =   self.__protocol.lightgreen
        self.blue =    self.__protocol.lightblue
        self.yellow =  self.__protocol.lightyellow
        self.magenta = self.__protocol.lightmagenta
        self.cyan =    self.__protocol.lightcyan
        self.white =   self.__protocol.lightwhite

class ID(object):

    def __init__(self):
        self.move = "M"
        self.light = "L"
        self.gripper = "G"
        self.extMmotor = "E"
        self.waitFor = "T"

        
class Pos(object):
    
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        
class Utils (object):
    
    def __init__(self):
        self.logger = logging.getLogger('one-easy-protocol')
    
    def valueToString(self,value):
        
        if(value>-1000.0 and value<1000.0):
            
            upvalue = value * 10.0
            tempstr = int(upvalue)
            string = str(tempstr)
            
            if (value > -1.0 and value < 1.0):
                string = '000' + string
                
            elif(value> -10.0 and value < 10.0):
                string = '00' + string
                
            elif(value> -100.0 and value < 100.0):
                string = '0' + string
            
            elif (value > -1000.0 and value < 1000.0):
                string = string 
            else:
                return '0000'
                
            if(value>=0.0):
                string = '+' + string
            else:
                string = string.replace('-','')
                string = '-' + string
            return string
        
        else:
            self.logger.info("Values not valid! Please check you values. Valid numbers are between -999.9 and 999.9")
            return None
        
    def posToString(self,pos):
        strX=self.valueToString(pos.x)
        strY=self.valueToString(pos.y)
        strZ=self.valueToString(pos.z)
        return strX,strY,strZ
    
    def fillData(self,txString,length=22):
        i=0
        if len(txString) < length:
            i=len(txString)
            while(i<length):
                txString = txString +'#' 
                i+=1
        return txString

class Basic(object):
    
    def __init__(self, connection=None, robotid=None, deviceid=None):
        self._robotid = robotid
        self._deviceid = deviceid
        self._connection = connection
        self._protocol = Protocol()
        self._utils = Utils()
        
    def _checkParameters(self):
        if( self._robotid==None and self._deviceid==None and self._connection==None):
            return 1
        else:
            return 0
        
    def _sendData(self,txString):
        txBytes = str.encode(txString)
        self._connection.reset_output_buffer()
        time.sleep(0.01)
        self._connection.write(txBytes)
        self._utils.logger.info('One easy protocol: ' + txString)
        self._connection.reset_input_buffer()
        time.sleep(0.01)
        while True:
            line = self._connection.read(1)
            if line == self._robotid.encode():
                break
        return 0        

class Functions(Basic):  
    
    def waitFor(self,milliseconds):
        if(self._checkParameters()==0):
            seconds = milliseconds/1000.0
            time.sleep(int(seconds))
        return 0
    
class Move(Basic):

    def ptp(self,positionX,positionY,positionZ,speed=50.0):
        pos = Pos()
        if(self._checkParameters()==0):
            pos.x = positionX
            pos.y = positionY
            pos.z = positionZ
            x,y,z = self._utils.posToString(pos)
            
            v = self._utils.valueToString(speed)
            v = v.replace('+','')
            v = v.replace('-','')
            
            txString = self._robotid + self._deviceid +'M'+ x + y + z + v
            txString = self._utils.fillData(txString)
            self._sendData(txString)
        return 0
        
    def home(self):
        if(self._checkParameters()==0):
            self.ptp(0.0,0.0,85.0,50.0)
        return 0
    
class Gripper(Basic):
    
    def open(self):
        if(self._checkParameters()==0):
            txString = self._robotid + self._deviceid + self._protocol.gripperopen
            txString = self._utils.fillData(txString)
            self._sendData(txString)
        return 0
    
    def close(self):
        if(self._checkParameters()==0):
            txString = self._robotid + self._deviceid + self._protocol.gripperclose
            txString = self._utils.fillData(txString)
            self._sendData(txString)
        return 0
        
class ExtMotor(Basic):
        
    def start(self,speed=100.0):
        if(self._checkParameters()==0):
            v = self._utils.valueToString(speed)
            v = v.replace('+','')
            v = v.replace('-','')
            txString = self._robotid + self._deviceid + self._protocol.extmotoron
            txString = self._utils.fillData(txString,18)
            txString = txString + v
            self._sendData(txString)
        return 0
        
    def stop(self):
        if(self._checkParameters()==0):
            txString = self._robotid + self._deviceid + self._protocol.extmotoroff
            txString = self._utils.fillData(txString)
            self._sendData(txString)
        return 0
        
    def setSpeed(self,speed):
        if(self._checkParameters()==0):
            v = self._utils.valueToString(speed)
            v = v.replace('+','')
            v = v.replace('-','')
            txString = self._robotid + self._deviceid + self._protocol.extmotoron
            txString = self._utils.fillData(txString,18)
            txString = txString + v
            self._sendData(txString)
        return 0
        
class Light(Basic):
    
    def on(self, intensity=100.0):
        if(self._checkParameters()==0):
            i = self._utils.valueToString(intensity)
            i = i.replace('+','')
            i = i.replace('-','')
            txString = self._robotid + self._deviceid + self._protocol.lighton
            txString = self._utils.fillData(txString,18)
            txString = txString + i
            self._sendData(txString)
        return 0
        
    def off(self):
        if(self._checkParameters()==0):
            txString = self._robotid + self._deviceid + self._protocol.lightoff
            txString = self._utils.fillData(txString)
            self._sendData(txString)
        return 0
        
    def setColour(self, colour, intensity = 100.0):
        if(self._checkParameters()==0):
            i = self._utils.valueToString(intensity)
            i = i.replace('+','')
            i = i.replace('-','')
            txString = self._robotid + self._deviceid + self._protocol.lighton + '#' + colour
            txString = self._utils.fillData(txString,18)
            txString = txString + i
            self._sendData(txString)
        return 0
             
class EasyProtocol(object):
    def __init__(self):
        self.__timeout = 1
        self.__port = ""
        self.__baudrate = 9600
        self.__connection = serial.Serial()
        self.__robotid = ''
        self._utils = Utils()
        
        self.move = Move()
        self.gripper = Gripper()
        self.extmotor = ExtMotor()
        self.light = Light()
        self.functions = Functions()
        self.flowchart = Flowchart()

    def setPort(self,port,baudrate = 9600,timeout = 1):
        self.__timeout = timeout
        self.__port = port
        self.__baudrate = baudrate
        return 0
    
    def __setCommunication(self):
        self._utils.logger.info("Try to connect robot...")
        self._utils.logger.info("ID: "+ self.__robotid+" / "+"Port: "+self.__port+" / "+"Baudrate: "+str(self.__baudrate))
        traffic=None
        try:
            self.__connection = serial.Serial(port=self.__port,baudrate=self.__baudrate,timeout=self.__timeout)
            time.sleep(0.25)
            for i in range(10):
                traffic = self.__connection.read(1)
                time.sleep(0.25)
                if traffic == self.__robotid.encode():
                    self._utils.logger.info("...connection sucessfully etablished!")
                    break
                self._utils.logger.info("...searching for robot ("+str(i+1)+'/'+str(10)+')')
                traffic = None
        except:
            self._utils.logger.warning("...no robot available. Please check your parameters!")
            
        if traffic == None:
            self._utils.logger.warning("...no robot available. Please connect your robot and activate serial communication software!")
            self._utils.logger.warning("Dont't forget to activate the USB Control Mode (Ctrl) using the switch on the circuit board!")
        elif traffic!=None:
            self.move = Move(self.__connection,self.__robotid,self.__deviceid)
            self.gripper = Gripper(self.__connection,self.__robotid,self.__deviceid)
            self.extmotor = ExtMotor(self.__connection,self.__robotid,self.__deviceid)
            self.light = Light(self.__connection,self.__robotid,self.__deviceid)
            self.functions = Functions(self.__connection,self.__robotid,self.__deviceid)
            self.flowchart = Flowchart(self.move,self.gripper,self.extmotor,self.light,self.functions)
        return 0
    
    def __find_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i+1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            portsUSB = glob.glob('/dev/ttyUSB*')
            portsACM = glob.glob('/dev/ttyACM*')
            ports = portsUSB + portsACM
        else:
            self._utils.logger.info("Can't find ports on your operating system")
            ports = ""
        return ports
    
    def findRobot(self):
        ports = self.__find_ports()
        if ports != "":
            traffic=None
            portname=""
            for port in ports:
                try:
                    self.__connection = serial.Serial(port,baudrate=self.__baudrate,timeout=self.__timeout)
                    self._utils.logger.info("Checking port: " + port +"...")
                    check = ""
                    time.sleep(0.25)
                    self.__connection.reset_input_buffer()
                    time.sleep(0.25)
                    traffic = self.__connection.read(1)
                    time.sleep(0.25)
                    if traffic != None and str(traffic.decode()) != "":
                        check = str(traffic.decode())
                        
                    time.sleep(0.25)
                    self.__connection.reset_input_buffer()
                    time.sleep(0.25)
                    traffic = self.__connection.read(1)
                    time.sleep(0.25)
                    if traffic != None and str(traffic.decode()) == check and check != "":
                        self._utils.logger.info("...found robot with ID: " + str(traffic.decode()) + " on port: "+ port)
                        self.__connection.close()
                        self.__robotid = traffic.decode()
                        self.__port = port
                        break
                    self.__robotid = None
                    self.__connection.close()
                except:
                    self._utils.logger.info("...no device on port: "+ port) 
            else:
                self.__port = None
                self._utils.logger.warning("...no robot available. Please connect your robot and activate serial communication software!")
                self._utils.logger.warning("Dont't forget to activate the USB Control Mode (Ctrl) using the switch on the circuit board!")
        return 
    
    def start(self,robotid=1,deviceid=0):
        robotidstr = str(robotid)
        deviceidstr = str(deviceid)
        if len(robotidstr)==1 and len(deviceidstr)==1:
            self.__robotid = robotidstr
            self.__deviceid = deviceidstr
            if self.__port != None:
                self.__setCommunication()
        else:
            self._utils.logger.info("Please enter only one symbol to set the Robot-ID and Device-ID") 
        return 0
    
    def stop(self):
        self.__connection.close()
        
    def __del__(self):
        self.stop()
        
    def __waitForRobot(self):
        self._utils.logger.info("Robot executes a command...")
        for i in range(60):
            line = self.__connection.read(1)
            if line == self.__robotid.encode():
                break
            self._utils.logger.info("...")
        if i+1==60:
            self._utils.logger.info("Timout! Please check the connection to the robot!")
        else:   
            self._utils.logger.info("Robot is waiting for signals...")
        return 0

class SmartControlData(object):
    def __init__(self):
        self.dataid = ""
        self.robotid = ""
        self.deviceid = ""
        self.colour = ""
        self.intensity = 0
        self.xPosition = 0
        self.yPosition = 0
        self.zPosition = 0
        self.velocity = 0
        self.workingSpaceStatus = False
        self.gripperStatus = False
        self.waitFortime = 0
        

    def toString(self):

        dataString = ""
        id = ID()

        if self.dataid==id.waitFor :
            dataString = "Wait for >> " + str(self.waitFortime) + " ms "
            
        if self.dataid==id.move:
            dataString = "Move to >> X: " + str(self.xPosition) + " mm " + "> Y: " + str(self.yPosition) + " mm " + "> Z: " + str(self.zPosition) + " mm " + "> speed: " + str(self.velocity)+ " %"
    

        if self.dataid==id.gripper:
 
            if self.gripperStatus == True: 
                dataString = "Gripper >> close"
            else: 
                dataString = "Gripper >> open"
    
        if self.dataid==id.light:
    
            colourData = "";
            lightStatus = False;
            colourID = Colour()

            if self.colour == colourID.red:
        
                colourData = "red"
                lightStatus = True
        
            elif self.colour == colourID.green:
        
                colourData = "green"
                lightStatus = True
        
            elif self.colour == colourID.blue:
        
                colourData = "blue"
                lightStatus = True
        
            elif self.colour == colourID.cyan:
        
                colourData = "cyan"
                lightStatus = True
        
            elif self.colour == colourID.magenta:
        
                colourData = "magenta"
                lightStatus = True
        
            elif self.colour == colourID.yellow:
        
                colourData = "yellow"
                lightStatus = True
        
            elif self.colour == colourID.white:
        
                colourData = "white"
                lightStatus = True
        
            else:
                colourData = "off"
                lightStatus = False
        

            if lightStatus == True:
                dataString = "Light >> on > colour: " + colourData + " > intensity: " + str(self.intensity) + " %";
            else:
                dataString = "Light >> off";
        
        return dataString;

    def toDataString(self):
        
        dataString = ""
        id = ID()

        if self.dataid==id.waitFor:
    
            dataString = id.waitFor + " " + str(self.waitFortime);
    

        if self.dataid==id.move:
    
            dataString = id.move + " " + str(self.xPosition) + " " + str(self.yPosition) + " " + str(self.zPosition) + " " + str(self.velocity) + " " + str(self.workingSpaceStatus);
    

        if(self.dataid==id.gripper):
    
            if(self.gripperStatus == True): 
                dataString = id.gripper + " " + "1";
            else: 
                dataString = id.gripper + " " + "0";
    

        if(self.dataid==id.light):
    
            colourData = ""
            lightStatus = False
            colourID = Colour()

            if self.colour == colourID.red:
        
                colourData = "1"
                lightStatus = True
        
            elif self.colour == colourID.green:
        
                colourData = "2"
                lightStatus = True
       
            elif self.colour == colourID.blue:
        
                colourData = "3"
                lightStatus = True
        
            elif self.colour == colourID.cyan:
        
                colourData = "4"
                lightStatus = True
        
            elif self.colour == colourID.magenta:
        
                colourData = "5"
                lightStatus = True
        
            elif self.colour == colourID.yellow:
        
                colourData = "6"
                lightStatus = True
        
            elif self.colour == colourID.white:
        
                colourData = "7"
                lightStatus = True
        
            else:
        
                colourData = "off"
                lightStatus = False
        
            if(self.lightStatus == True):
                dataString = str(colourID.light) + " " + "1" + " " + colourData + " " + str(self.intensity);
            else:
                dataString = str(colourID.light) + " " + "0";
 
        return dataString


    def fromDataString(self,dataString):
        
        id = ID()

        datalist=dataString.split(" ")
        
        if datalist[0]==id.waitFor:
            
            self.dataid = datalist[0]
            self.robotid = ""
            self.deviceid = ""

            self.colour = ""
            self.intensity = 0

            self.xPosition = 0
            self.yPosition = 0
            self.zPosition = 0
            self.velocity = 0

            self.workingSpaceStatus = False

            self.gripperStatus = False

            self.waitFortime = int(datalist[1])
    

        if datalist[0]==id.move:
    
            self.dataid = datalist[0]
            self.robotid = ""
            self.deviceid = ""

            self.colour = ""
            self.intensity = 0

            self.xPosition = int(datalist[1])
            self.yPosition = int(datalist[2])
            self.zPosition = int(datalist[3])
            self.velocity = int(datalist[4])

            if int(datalist[5])==0: 
                self.workingSpaceStatus = False
            if int(datalist[5])==1: 
                self.workingSpaceStatus = True

            self.gripperStatus = False

            self.waitFortime = 0
    

        if datalist[0]==id.gripper:
    
            self.dataid = datalist[0];
            self.robotid = ""
            self.deviceid = ""

            self.colour = ""
            self.intensity = 0

            self.xPosition = 0
            self.yPosition = 0
            self.zPosition = 0
            self.velocity = 0

            self.workingSpaceStatus = False

            if int(datalist[1])==0: 
                self.gripperStatus = False
            if int(datalist[1])==1: 
                self.gripperStatus = True

            self.waitFortime = 0
    

        if datalist[0]==id.light:
    
            self.dataid = datalist[0]
            self.robotid = ""
            self.deviceid = ""

            if int(datalist[1])==0:
        
                protocol = Protocol()
                self.colour = protocol.lightoff
                self.intensity = 0
        
            if int(datalist[1])==1:

                colourID = Colour()
            
                if int(datalist[2])==1: 
                    self.colour = colourID.red
                   
                elif int(datalist[2])==2: 
                    self.colour = colourID.green
                    
                elif int(datalist[2])==3: 
                    self.colour = colourID.blue
                   
                elif int(datalist[2])==4: 
                    self.colour = colourID.cyan
                    
                elif int(datalist[2])==5: 
                    self.colour = colourID.magenta
                    
                elif int(datalist[2])==6: 
                    self.colour = colourID.yellow
                    
                elif int(datalist[2])==7: 
                    self.colour = colourID.white
                    
            
                self.intensity = int(datalist[3])
        

            self.xPosition = 0
            self.yPosition = 0
            self.zPosition = 0
            self.velocity = 0

            self.workingSpaceStatus = False
            self.gripperStatus = False

            self.waitFortime = 0

class Flowchart(object):

    def __init__(self,move=None,gripper=None,extmotor=None,light=None,functions=None):
        self.__move = move
        self.__gripper = gripper
        self.__extmotor = extmotor
        self.__light = light
        self.__functions = functions
        self._utils = Utils()
        self.__controlDataStore = []
        self.__controlDataList = []

    
    def print(self):
        for line in self.__controlDataList:
            print(line)

    def load(self,path):

        file = open(path, "r")

        self.__controlDataStore = []

        header = 3;

        for line in file:

            if header == 0:
        
                data = SmartControlData();
                data.fromDataString(line);
                self.__controlDataStore.append(data);
        
            else:
                header=header-1

        self.__controlDataList = []

        for data in self.__controlDataStore:
            self.__controlDataList.append(data.toString());
            
        return self.__controlDataStore,self.__controlDataList

    def start(self):
        id = ID()

        if self.__move!=None and self.__gripper!=None and self.__extmotor!=None and self.__light!=None and self.__functions!=None:

            for controlData in self.__controlDataStore:
    
                if controlData.dataid == id.move:
                  self.__move.ptp(controlData.xPosition,controlData.yPosition,controlData.zPosition,controlData.velocity);

                if controlData.dataid == id.gripper:
                    if(controlData.gripperStatus == True): 
                        self.__gripper.close();
                    else: 
                        self.__gripper.open();
                    
                if controlData.dataid == id.light:
                    protocol = Protocol()
                    if controlData.colour!=protocol.lightoff:
                        self.__light.setColour(controlData.colour,controlData.intensity)
                    else: 
                        self.__light.off()
                        
                if controlData.dataid == id.waitFor:
                    self.__functions.waitFor(controlData.waitFortime)

        else:
            self._utils.logger.warning("...no robot available. Please connect your robot and activate serial communication software!")
            self._utils.logger.warning("Dont't forget to activate the USB Control Mode (Ctrl) using the switch on the circuit board!")
