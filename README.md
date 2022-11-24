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

## Source code

# Modules

- `ai.py` This is a module that classifies the content of the image as blottle, can, other, and no_object. It returns a category.
- `lookforObjects.py` This is a module that looks for the center of any object in the image and their orientations. It returns a list of orientations, a list of centers and an image with visual info. If no objects, it returns empty lists.

## Test files (to use as Scripts)

- `kinematics.py` kinematics calculations and robot model
- `serialcomTest.py` test on serial communications with pyserial
- `lookObjectsVideo.py` lookforObjects module working on on frames from webcam's video
- `ai_video.py` test on frames from webcam's video
- `test_camera.py` Code to check out whether your camera is working

## Files to be imported as additional source code  

- `robotClasses.py` This is a file with the [Class Diagram](https://app.genmymodel.com/personal/projects/_cYSoYGWiEe2ck8ytUMEi6A) for the robot use cases. Edited in www.genmymodel.com  
- `robotStateMach.py` This is a file with the Robot State Machine.
- `gui.py` This is file with a Simple graphical user interface for the robot
- `training.py` This is a file with the AI training code using Convolutional Neural Networks



For any other questions, solicitations email [Henry Roncancio](mailto:henryroncanciovelandia@gmail.com) (initial author)