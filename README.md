# Object Classification on Robotic Application

Garbage Classification and selection using robotic arm

## Table of Contents

- [Quickstart](#quickstart)
- [Non-Quickstart](#the-non-quickstart)
- [Files](#files)


## Quickstart 

In order for this code to work you will need to install a few packages 

```shell script
pip install -r requirements.txt
```
## The Non Quickstart


Recomended instructions for a person new to Python and git hub on how to install the packages, clone the repository, and run the code: [deployment in (Spanish)](https://github.com/roncanciovl/objectclassification/blob/main/deployment.md)

For more information about how to deploy software, you may also check out [tutorials](https://github.com/roncanciovl/objectclassification/blob/main/tutorials.md)

## Files


- `ai.py` pedricts whether there is or not an object (blottle, can, other) in the input image
- `lookforObjects.py` look for the center of an object and its orientation. If no object, there is no return.
- `ai_video.py` test on continuous predictions on frames from webcam's video
- `robotClasses.py` [Class Diagram](https://app.genmymodel.com/personal/projects/_cYSoYGWiEe2ck8ytUMEi6A) for Robot's use cases. Edited in www.genmymodel.com  
- `robotStateMach.py` State Machine of the robot.
- `gui.py` Simple graphical user interface to control robot
- `test_camera.py` Code to check out whether your camera is working
- `training.py` AI training code using Convolutional Neural Networks
- `kinematics.py` kinematics calculations and robot model


For any other questions, solicitations email [Henry Roncancio](mailto:henryroncanciovelandia@gmail.com) (initial author)