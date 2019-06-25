<img src="https://github.com/deltarobotone/image_database/blob/master/logos/logos%20(9).PNG" width="300">

Delta-Robot One recieve data in a very simple way which is developed for arduino based simple robot systems.This Pothon package includes classes and functions to privide an high level API for an easy usage of Delta-Robot One controlled from a system connected over USB. Use example "test.py" to do the first steps... 

## Use python package manager to install one easy protocol on your system

```c
pip install one-easy-protocol
```

## Import package

```c
import easyprotocol as ep
```

## Prepare the robot

First you have to set the robot in remote contol mode with the switch on the circuit board (right side of display)

[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(19).PNG" width="120">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(19).PNG)

If you use the FullSystemDemo of the OneSystemLibrary examples navigate to remote using rotary encoder. Press the rotary encoder button and navigate to USB. Press the rotary encoder butten again.

[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(8).PNG" width="200">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(8).PNG)

The second option to set the robot in the right mode for the remote control based on the One easy protocol to do it in your programm code. Use the API of the OneSystemLibrary [Remote example](https://github.com/deltarobotone/one_system_library/blob/master/examples/Remote/Remote.ino)

## Option 1: Connet robot automatically

```c
# Option 1: Automatic (console info on)
robot = ep.EasyProtocol(info = True)

# Find robot (port/id) automatically
robot.findRobot()

# Start communication
robot.start()
```

## Option 2: Connect robot manually

```c
# Option 2: Manual (console info on)
# robot = ep.EasyProtocol(info = True)

# Set port, baudrate and timeout of serial communication
# robot.setPort(port='COM37',baudrate=9600, timeout=1)

# Start communication and set id's
# robot.start(robotid='1' ,deviceid='1')
```

## Robot control functions of this package

```c
# Gripper
robot.gripper.open()
robot.functions.waitFor(2000)
robot.gripper.close()
robot.functions.waitFor(2000)

# Move (pick and place)
robot.move.ptp(0.0,0.0,85.0,50.0)
robot.move.ptp(-30.0,0.0,105.0,85.0)
robot.move.ptp(-30.0,0.0,115.00,20.00)
robot.move.ptp(-30.0,0.0,105.0,50.0)
robot.move.ptp(30.0,0.0,105.0,85.0)
robot.move.ptp(30.0,0.0,115.00,20.00)
robot.move.ptp(30.0,0.0,105.0,50.0)
robot.move.ptp(0.0,0.0,105,5.0)

# Console info off
robot.printInfo(False)

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
## Deconnect robot

```c
# Stop communication
robot.stop()
```

## Protocol information

One easy protocol is based on a simple 22 Byte long data sequence shown in the picture below.
The sequence consists of human readable characters so everybody can understand the communication.

[<img src="https://github.com/deltarobotone/image_database/blob/master/drawings/drawings%20(20).PNG" width="900">](https://raw.githubusercontent.com/deltarobotone/image_database/master/drawings/drawings%20(20).PNG)
