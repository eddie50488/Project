import time

class Robot:

    def __init__(self, x: float, y: float, speed: float = 0.05): #units of m/s
        self.x = x
        self.y = y    
        self.wheel_handler = WheelHandler()
        self.speed = speed


    # the robot deconstructs, based off a final destination, the required horizontal/vertical movements to reach it.
    def move(self, x: float, y: float):
        # generate list of intermediate points
        pass
    

    # the robot uses the list of points calcualted above and moves to them
    def _move_to_points(self, points: list[tuple[float, float]]):  
        for point in points:
            x = point[0]
            y = point[1]
            self._move_line(x, y)

    def _move_line(self, x: float, y: float):
        if self.x == x:
            self._move_vertically(y-self.y)
        elif self.y == y:
            self._move_horizontally(x-self.x)
        else:
            raise RuntimeError(f"Position ({x},{y}) does not form a straight line with current robot position ({(self.x),{self.y}})")
    
    def _move_vertically(self, distance: float):
        self._move_wheels(distance, ['circle', 'square'])
        self.y += distance

    def _move_horizontally(self, distance: float):
        self._move_wheels(distance, ['triangle', 'plus'])
        self.x += distance
    
    def _move_wheels(self, distance, wheel_types: list[str]):
        self.wheel_handler.change_speeds({wheel_type: self.speed for wheel_type in wheel_types})
        time.sleep(distance/self.speed)
        self.wheel_handler.change_speeds({wheel_type: 0 for wheel_type in wheel_types})

class WheelHandler:

    @staticmethod
    def convert_speed_to_pwm(speed: float) -> int:         #static method of class WheelHandler made to convert from m/s to pwm value
        return 1 if speed != 0 else 0

    def __init__(self):                                    #properties of the wheel handler class - the desired speeds to be pushed to the wheeels
        self.default_speeds = {
            "triangle": 0,
            "square": 0,
            "circle": 0,
            "plus": 0,
        }
    
    def change_speeds(self, updating_speeds: dict[str: float]):
        new_pwms = {wheel_type: WheelHandler.convert_speed_to_pwm(speed) for wheel_type, speed in (self.default_speeds | updating_speeds).items()}
        # build the instruction string
        print(new_pwms)
        # send instruction


