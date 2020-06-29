![Python package](https://github.com/deltarobotone/one-easy-protocol/workflows/Python%20package/badge.svg?branch=master)
![Upload Python Package](https://github.com/deltarobotone/one-easy-protocol/workflows/Upload%20Python%20Package/badge.svg?branch=v0.4)

<img src="https://github.com/deltarobotone/image_database/blob/master/logos/logos%20(9).PNG" width="300">

Delta-Robot One recieve data in a very simple structure which is developed for this arduino based robot system. This Python package is called easyprotocol and includes classes and functions to provide an high level interface to control Delta-Robot One from other systems or devices. Use example "test.py" to do the first steps... 

## Use python package manager to install one-easy-protocol on your system

```c
pip install one-easy-protocol
```
or
```c
pip3 install one-easy-protocol
```

Tested successfully on Raspberry Pi 3 with Raspbian (Version: June 2019) and Windows machine with Anaconda using Python 3.5

## NEW!!! Flowchart support

[<img src="https://github.com/deltarobotone/image_database/blob/master/logos/logos%20(15).PNG" width="550">](https://raw.githubusercontent.com/deltarobotone/image_database/master/logos/logos%20(15).PNG)

Flowcharts can be used to write your own robot control programs for Delta-Robot One. Flowcharts can be stored in the flowchart data format (.fc). The One Smart Control Software (actually supported on Windows 10 and Android) provides functions to use (play), create, change, save and load flowcharts. Check out One Smart Control Software on your Device ([direct download](https://github.com/deltarobotone/one_smart_control_desktop) for Windows 10 or Play Store for Android). Additionally the One Easy Protocol development packages provide some basic functions for Flowcharts (actually supported with python on Linux and Windows and c++ on Windows). Load, print and start your flowchart file you have been created with One Smart Control. Check out One Easy Protocol on your Device (pip install one-easy-protocol for python or [direct download](https://github.com/deltarobotone/one_easy_protocol) for c++). With Flowcharts you are able to use your robot on an easy way.

## Prepare the robot

First you have to set the robot in remote contol mode with the switch on the circuit board (right side of display)

[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(19).PNG" width="120">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(19).PNG)

If you have the FullSystemDemo of the OneSystemLibrary examples installed on your robot navigate to remote using rotary encoder. Press the rotary encoder button and navigate to USB. Press the rotary encoder button again.

[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(8).PNG" width="250">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(8).PNG)

The second option is to set the robot in the right mode for the remote control. You have to do it in your programm code. Use the API of the OneSystemLibrary in your arduino sketch like this:

```c
DeltaRobotOne robot(0, 0, 0, 0, 0, 0, 0x27);

void setup()
{
  robot.setup();
  robot.power.mainOn();
}

void loop()
{
  robot.remote.control();
}
```

For more instructions like bluetooth remote control have a look on the full [remote contol example](https://github.com/deltarobotone/one_system_library/blob/master/examples/Remote/Remote.ino) of the library.

## Import the package

```c
import easyprotocol as ep
```

## Optional: Logging

```c
# For Logging
import logging
```

Print logging information to file (replace example.log with "path_to_your_logfile.log")

```c
# Log in a file
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='example.log', level=logging.DEBUG)
```

Print logging information to console

```c
# Log console output
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
```

## Option 1: Connect the robot automatically

```c
# Option 1: Automatic
robot = ep.EasyProtocol()

# Find robot port an ID automatically
robot.findRobot()

# Start communication
robot.start()
```

## Option 2: Connect robot manually

```c
# Option 2: Manually
robot = ep.EasyProtocol()

# Set port, baudrate and timeout of serial communication
# Windows: COM<myPort> 
# Linux: /dev/ttyACM<myPort> 
robot.setPort(port='COM37',baudrate=9600, timeout=1)

# Start communication and set ID's
robot.start(robotid = "1" ,deviceid = "1")
```

## Robot control functions of this package

>Note: All functions are waiting for robot response after a command was transmitted. In the case of a robot movement command the package function is waiting until the robot reached the target position. After that your code continue with the next given command.

```c
# Gripper
robot.gripper.open()
robot.functions.waitFor(2000)
robot.gripper.close()
robot.functions.waitFor(2000)

# Move (pick and place)
# ptp(X-Position, Y-Position, Z-Position, Speed)
# Note: Only one number after the comma is used by the protocol and the robot

robot.move.ptp(0.0,0.0,85.0,50.0)
robot.move.ptp(-30.0,0.0,105.0,85.0)
robot.move.ptp(-30.0,0.0,115.00,20.00)
robot.move.ptp(-30.0,0.0,105.0,50.0)
robot.move.ptp(30.0,0.0,105.0,85.0)
robot.move.ptp(30.0,0.0,115.00,20.00)
robot.move.ptp(30.0,0.0,105.0,50.0)
robot.move.ptp(0.0,0.0,105,5.0)

# Colour object
colour = ep.Colour()

# Light intensity
robot.light.setColour(colour.red,10.0)
robot.functions.waitFor(1000)
robot.light.setColour(colour.red,50.0)
robot.functions.waitFor(1000)
robot.light.setColour(colour.red,100.0)
robot.functions.waitFor(1000)

# Light colours
robot.light.setColour(colour.blue)
robot.functions.waitFor(1000)
robot.light.setColour(colour.green)
robot.functions.waitFor(1000)
robot.light.setColour(colour.yellow)
robot.functions.waitFor(1000)
robot.light.setColour(colour.magenta)
robot.functions.waitFor(1000)
robot.light.setColour(colour.cyan)
robot.functions.waitFor(1000)
robot.light.setColour(colour.white)
robot.functions.waitFor(1000)

#Light off
robot.light.off()
robot.functions.waitFor(1000)

# External motor control
robot.extmotor.start()
robot.functions.waitFor(2000)
robot.extmotor.setSpeed(50.0)
robot.functions.waitFor(2000)
robot.extmotor.stop()
```

## Flowchart support 
Load and start a flowchart file (.fc) created with One Smart Control Desktop or Mobile

```c
# Load Flowchart from file
robot.flowchart.load("<path to your file>.fc")

# Print Flowchart to console
robot.flowchart.print()

# Start Flowchart
robot.flowchart.start()
```

## Deconnect robot

```c
# Stop communication
robot.stop()
```

## Protocol information

One easy protocol is based on a simple 22 byte long data sequence shown in the picture below.
The sequence consists of human readable characters.

[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(20).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(20).PNG)

## Move sequence
[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(21).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(21).PNG)
## Move example
[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(22).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(22).PNG)
## Light sequence
[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(23).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(23).PNG)
## Light example
[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(24).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(24).PNG)
## Gripper sequence
[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(25).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(25).PNG)
## Gripper example
[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(26).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(26).PNG)
## External motor sequence
[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(27).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(27).PNG)
## External motor example
[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(28).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(28).PNG)
