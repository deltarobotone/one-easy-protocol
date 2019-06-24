import OneEasyProtocol as oep
robot = oep.EasyProtocol(info = True)
robot.find_robot()
robot.start()

robot.gripper.open()
robot.functions.waitFor(2000)
robot.gripper.close()
robot.functions.waitFor(2000)

robot.move.ptp(0.0,0.0,85.0,50.0)
robot.move.ptp(-30.0,0.0,105.0,85.0)
robot.move.ptp(-30.0,0.0,115.00,20.00)
robot.move.ptp(-30.0,0.0,105.0,50.0)
robot.move.ptp(30.0,0.0,105.0,85.0)
robot.move.ptp(30.0,0.0,115.00,20.00)
robot.move.ptp(30.0,0.0,105.0,50.0)
robot.move.ptp(0.0,0.0,105,5.0)

robot.printInfo(False)

color = oep.Color()

robot.light.setColour(color.red,10.0)
robot.functions.waitFor(1000)
robot.light.setColour(color.red,50.0)
robot.functions.waitFor(1000)
robot.light.setColour(color.red,100.0)
robot.functions.waitFor(1000)

robot.light.setColour(color.blue)
robot.functions.waitFor(1000)
robot.light.setColour(color.green)
robot.functions.waitFor(1000)
robot.light.setColour(color.yellow)
robot.functions.waitFor(1000)
robot.light.setColour(color.magenta)
robot.functions.waitFor(1000)
robot.light.setColour(color.cyan)
robot.functions.waitFor(1000)
robot.light.setColour(color.white)
robot.functions.waitFor(1000)

robot.light.off()
robot.functions.waitFor(1000)

robot.extmotor.start()
robot.functions.waitFor(2000)
robot.extmotor.setSpeed(50.0)
robot.functions.waitFor(2000)
robot.extmotor.stop()

robot.stop()
