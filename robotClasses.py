"""
 Class Diagram for Garbage Selection Robot - Henry Roncancio - V1
"""



 

class Robot(object):
    pass
    # Start of user code -> properties/constructors for Robot class

    # End of user code
    # Start of user code -> methods for Robot class

    # End of user code


class Terrain(object):
    def __init__(self):
        self.pose = None
        
        self.robotActivity = None
        
    # Start of user code -> properties/constructors for Terrain class

    # End of user code
    # Start of user code -> methods for Terrain class

    # End of user code



class Dimensions(object):
    def __init__(self):
        self.width = 0.
        self.lenght = 0.
        self.height = 0.
        
        self.object = None
        
    # Start of user code -> properties/constructors for Dimensions class

    # End of user code
    # Start of user code -> methods for Dimensions class

    # End of user code

class Image(object):
    def __init__(self):
        
        self.camera = None
        
    # Start of user code -> properties/constructors for Image class

    # End of user code
    # Start of user code -> methods for Image class

    # End of user code

class Object(object):
    def __init__(self):
        self.distance = 0.
        self.orientation = 0.
        self.category = 0
        self.dimensions = None
        self.image = None
        
        self.dimensions2 = None
        self.container = None
        self.robotActivity = None
        
    # Start of user code -> properties/constructors for Object class

    # End of user code
    def LabelObject(self, parameter2):
        # Start of user code protected zone for LabelObject function body
        return 0
        # End of user code	
    # Start of user code -> methods for Object class

    # End of user code



class Container(object):
    def __init__(self):
        self.position = None
        self.category = 0
        self.objects = None
        
        self.object = []
        self.robotActivity = None
        
    # Start of user code -> properties/constructors for Container class

    # End of user code
    # Start of user code -> methods for Container class

    # End of user code


class RobotActivity(Robot):
    def __init__(self):
        self.__state = ""
        
        self.object = []
        self.terrain = None
        self.container = []
        
    # Start of user code -> properties/constructors for RobotActivity class

    # End of user code
    def openEndeffector(self):
        # Start of user code protected zone for openEndeffector function body
        return False
        # End of user code	
    def closeEndeffector(self):
        # Start of user code protected zone for closeEndeffector function body
        return False
        # End of user code	
    def moveffectortoObject(self, object):
        # Start of user code protected zone for moveffectortoObject function body
        return False
        # End of user code	
    def setState(self, state):
        # Start of user code protected zone for setState function body
        return False
        # End of user code	
    def getState(self, state):
        # Start of user code protected zone for getState function body
        return False
        # End of user code	
    def lookforObject(self, image):
        # Start of user code protected zone for lookforObject function body
        return False
        # End of user code	
    def detectObject(self, image):
        # Start of user code protected zone for detectObject function body
        return None
        # End of user code	
    def exploreWithTrajectory(self):
        # Start of user code protected zone for exploreWithTrajectory function body
        return False
        # End of user code	
    # Start of user code -> methods for RobotActivity class

    # End of user code

class Sensor(Robot):
    def __init__(self):
        self.pose = None
        self.__measure = 0.
        
        
    # Start of user code -> properties/constructors for Sensor class

    # End of user code
    def setMeasure(self, measure):
        # Start of user code protected zone for setMeasure function body
        return False
        # End of user code	
    def getMeasure(self, measure):
        # Start of user code protected zone for getMeasure function body
        return False
        # End of user code	
    # Start of user code -> methods for Sensor class

    # End of user code

class EndEffector(Robot):
    def __init__(self):
        self.pose = None
        self.state = False
        
        
    # Start of user code -> properties/constructors for EndEffector class

    # End of user code
    # Start of user code -> methods for EndEffector class

    # End of user code

class Camera(Robot):
    def __init__(self):
        self.pose = None
        self.name = ""
        self.image = None
        
        self.image = None
        
    # Start of user code -> properties/constructors for Camera class

    # End of user code
    def getImage(self):
        # Start of user code protected zone for getImage function body
        return None
        # End of user code	
    # Start of user code -> methods for Camera class

    # End of user code


# Start of user code -> functions/methods for Robot package

# End of user code
