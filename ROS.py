class Robot:

    def __init__(self,x,y):
        self.x = x
        self.y = y


    def position(self):
        return [float(self.x), float(self.y)]
    
    class Wheel:

        def __init__(self,speed, direction, brake):
            self.speed = speed
            self.direction = direction
            self.brake = brake

        def ismoving(self):
            if (self.brake == 0) and (self.speed >= 0):
                return 1
            else:
                return 0

        def set_speed(self, new_speed):
            self.speed = new_speed

        def set_direction(self, new_direction):
            self.direction = new_direction

        def set_brake(self, new_brake):
            self.brake = new_brake

        def get_speed(self):
            return int(self.speed)
        
        def get_direction(self):
            return int(self.direction)
        
        def get_brake(self):
            return int(self.brake)


    class Plus(Wheel):
        pass

    class Square(Wheel):
        pass

    class Circle(Wheel):
        pass

    class Triangle(Wheel):
        pass



