from enum import Enum

class Robot:

    def __init__(self,x_robot,y_robot):
        self.x_robot = x_robot              #Property of the robot is its x,y pos
        self.y_robot = y_robot    
        self.wheel_list = []                #Property of the robot is its wheels

    def position(self):
        return [float(self.x_robot), float(self.y_robot)]
    
    def create_wheel(self,enum):
        self.wheel_list.append(Wheel(enum))

    def return_wheels(self):
        return self.wheel_list

class Wheel(Enum):

    Triangle = 1
    Square = 2
    Circle = 3
    Plus = 4

    def __init__(self, wheel_type):
        self.wheel_type = wheel_type
        self.direction = None
        self.speed = None
        self.brake = None

    def status(self):
        return self.direction,self.speed, self.brake

    def set_speed(self,speed):
        self.speed = speed

    def set_direction(self,direction):
        self.direction = direction

    def set_brake(self,brake):
        self.brake = brake

    def ismoving(self):
        if (self.brake == 0) and (self.speed >= 0):
            return True
        else:
            return False
        