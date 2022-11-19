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


- `ai.py` This a module that classifies the content of the image as blottle, can, other, and no_object. It returns a category.
- `lookforObjects.py` This is a module that looks for the center of any object in the image and their orientations. Return a list of orientations, a list of centers and an image with visual info. If no objects, it returns empty lists.
- `lookObjectsVideo.py` lookforObjects module working on on frames from webcam's video
- `ai_video.py` test on frames from webcam's video
- `robotClasses.py` This is a file with the [Class Diagram](https://app.genmymodel.com/personal/projects/_cYSoYGWiEe2ck8ytUMEi6A) for the robot use cases. Edited in www.genmymodel.com  
- `robotStateMach.py` This is a file with the Robot State Machine.
- `gui.py` Simple graphical user interface to control robot
- `test_camera.py` Code to check out whether your camera is working
- `training.py` This is a file with AI training code using Convolutional Neural Networks
- `kinematics.py` kinematics calculations and robot model


For any other questions, solicitations email [Henry Roncancio](mailto:henryroncanciovelandia@gmail.com) (initial author)