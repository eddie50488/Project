
import ROS

def dot(Circle,Square,Triangle,Plus):

    if Circle.get_speed != 0:

        if (Triangle.get_direction() == 0) and (Plus.get_direction() == 0):
            print("Robot is travelling left")

        if (Triangle.get_direction() == 0) and (Plus.get_direction() == 1):
            print("Robot is travelling right")

        if (Circle.get_direction() == 0) and (Square.get_direction() == 0):
            print("Robot is travelling backwards")

        if (Circle.get_direction() == 1) and (Square.get_direction() == 1):
            print("Robot is travelling forwards")




my_robot = ROS.Robot(0,0)

Triangle = my_robot.Triangle(0,0,1)
Plus = my_robot.Plus(0,0,1)

Circle = my_robot.Circle(50,1,0)
Square = my_robot.Square(50,1,0)


dot(Circle,Square,Triangle,Plus)
