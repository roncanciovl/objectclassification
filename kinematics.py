
from roboticstoolbox import *
# https://github.com/petercorke/robotics-toolbox-python/


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

print(robot)

robot.plot(robot.q)

def testOnkine():
  #Forward kinematics
  T = robot.fkine([pi/4, pi/4, pi/4])
  print(T)
  #Inverse kinematics with numerical method
  solution = robot.ikine_LM(T)
  if (solution[1] == True):
    print("A solution for ikine was found")
    q = solution[0]
    print(q)
  else:
      print("No solution was found")

#Create an object of SE3 class, i.e., Homogeneous transformation or pose.
#As example, this pose could be the end-effector pose to go to the container
pose_in_container = SE3()
# SE3 is a transformation but it is aslo a pose
endeffectorPose = SE3()

if __name__ == "__main__":
    testOnkine()