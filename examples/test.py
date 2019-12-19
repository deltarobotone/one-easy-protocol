import easyprotocol as ep

# For Logging
# import logging

# Log in a file
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='example.log', level=logging.DEBUG)

# Log console output
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)


# Option 1: Automatic
robot = ep.EasyProtocol()

# Find robot (port/id) automatically
robot.findRobot()

# Start communication
robot.start()

# Option 2: Manually
# robot = ep.EasyProtocol()

# Set port, baudrate and timeout for serial communication
# robot.setPort(port='COM37',baudrate=9600, timeout=1)

# Start communication and set id's
# robot.start(robotid='1',deviceid='1')

# Robot control

# Gripper
robot.gripper.open()
robot.functions.waitFor(2000)
robot.gripper.close()
robot.functions.waitFor(2000)

# Move robot (pick and place)
robot.move.ptp(0.0,0.0,85.0,50.0)
robot.move.ptp(-30.0,0.0,105.0,85.0)
robot.move.ptp(-30.0,0.0,115.0,20.0)
robot.move.ptp(-30.0,0.0,105.0,50.0)
robot.move.ptp(30.0,0.0,105.0,85.0)
robot.move.ptp(30.0,0.0,115.0,20.0)
robot.move.ptp(30.0,0.0,105.0,50.0)
robot.move.ptp(0.0,0.0,105.0,5.0)

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

# Load Flowchart from file
# robot.flowchart.load("<path to your file>.fc")

# Print Flowchart to console
# robot.flowchart.print()

# Start Flowchart
# robot.flowchart.start()

# Stop communication
robot.stop()

