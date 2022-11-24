
from roboticstoolbox import *
# https://github.com/petercorke/robotics-toolbox-python/
# https://github.com/petercorke/robotics-toolbox-python/wiki/Kinematics
# https://github.com/petercorke/robotics-toolbox-python/blob/master/notebooks/kinematics.ipynb


from math import pi
import numpy as np
from spatialmath import *
import matplotlib.pyplot as plt
from matplotlib import cm
np.set_printoptions(linewidth=100, formatter={'float': lambda x: f"{x:8.4g}" if abs(x) > 1e-10 else f"{0:8.4g}"})

#%matplotlib notebook

# robot length values (metres)
d1 = 0.352
a1 = 0.070
a2 = 0.360
d4 = 0.380
d6 = 0.065

robot = DHRobot([
  RevoluteDH(d=d1, a=a1, alpha=-pi/2), 
  RevoluteDH(a=a2), 
  RevoluteDH(alpha=pi/2),
  ], name="wally")
#Joint angles at home state
qhome = np.array([0, 0, 0])
#Set robot joint configuration at home
robot.q = qhome
print(robot)
#robot.plot(robot.q)

# SE3 is a transformation but it is aslo a pose
# we want the end-effector to be at position (0.5, 0.2, 0.1) 
# and to have its gripper pointing (its approach vector) in the x-direction, 
# and its fingers one above the other so that its orientation vector is parallel to the z-axis.
#Check Two Vector Representation on Peter Corke - Robot, Vision and Control
desiredPose =  SE3(0.4, 0.2, 0.2) * SE3.OA([0,0,1], [1,0,0])
# Other pose
desiredPoseValid = SE3(0.3246, 0, 0.09744) * SE3.OA([0,1,0], [0,0,1])

def findJointAngles(desiredPose, seed):
    solution = robot.ikine_LM(desiredPose)
    return solution.success, solution.q 

#def findTrajJointAngles(robot, desiredPose):

def testOnkine():
    #Forward kinematics
    T = robot.fkine([pi/4, pi/4, pi/4])
    print(T)
    #Inverse kinematics with numerical method
    #Starting pose is the pose in robot.q
    solution = robot.ikine_LM(T)
    if (solution.success == True):
      print("A solution for ikine was found")
      q = solution.q
      print(q)
    else:
        print("No solution was found")

    #Set new pose
    robot.q = solution.q
    #Alternatively, robot.plot visualizes and updates robot.q at once
    #robot.plot(solution.q)

    #A simple trajectory from previous pose to home
    qt = jtraj(solution.q, qhome, 50)
    #Array of Joint angles
    print(qt.q)
    #Animate trajectory
    robot.plot(qt.q, dt=0.1)
    #Robot joint angles are updated in robot.q
    print(robot.q)
    #time vector
    #print(qt.t)
    input("Press Enter to continue...")
    
    
    #New trajectory
    
    #Levenberg-Marquadt with Sugihara's tweak
    desiredSolution = robot.ikine_LMS(desiredPose)
    if desiredSolution.success == False:
      print("Robot can't reach the desired pose")
    else:
      print("Robot can reach the desired pose")
    print(desiredSolution.q)
    #From current joint angles to desired joint angles
    qt = jtraj(robot.q, desiredSolution.q , 50)
    robot.plot(qt.q, dt=0.1)
    input("Press Enter to continue...")

    #New trajectory
    
    #Levenberg-Marquadt with Sugihara's tweak
    desiredSolutionV = robot.ikine_LMS(desiredPoseValid, ilimit=500)
    if desiredSolutionV.success == False:
      print("Robot can't reach the desired pose")
      print(desiredSolutionV.reason)
    else:
      print("Robot can reach the desired pose")

    print(desiredSolutionV.q)
    #From current joint angles to desired joint angles
    qt = jtraj(qhome, desiredSolutionV.q , 50)
    robot.plot(qt.q, dt=0.1)
    input("Press Enter to continue...")

#Create an object of SE3 class, i.e., Homogeneous transformation or pose.
#As example, this pose could be the end-effector pose to go to the container
pose_in_container = SE3()
# SE3 is a transformation but it is aslo a pose
endeffectorPose =  SE3()

#This test runs when kinematics.py is run as a script
if __name__ == "__main__":
    testOnkine()