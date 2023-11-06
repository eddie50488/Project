import time

class Robot:

    def __init__(self, x: float, y: float, speed: float = 1):
        self.x = x
        self.y = y    
        self.wheel_handler = WheelHandler()
        self.speed = speed

    def move(self, x: float, y: float):
        # generate list of intermediate points
        pass
    
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
        for wheel_type in wheel_types:
            self.wheel_handler.buffer_wheel_speed_changes(self.speed, wheel_type)
        self.wheel_handler.commit_speed_changes()
        time.sleep(distance/self.speed)
        for wheel_type in wheel_types:
            self.wheel_handler.buffer_wheel_speed_changes(0, wheel_type)
        self.wheel_handler.commit_speed_changes()

class WheelHandler:

    @staticmethod
    def convert_speed_to_pwm(speed: float) -> int:
        pass

    def __init__(self):
        self.buffer = {
            "triangle": 0,
            "square": 0,
            "circle": 0,
            "plus": 0,
        }
    
    def buffer_wheel_speed_changes(self, speed: float, wheel_type):
        self.buffer[wheel_type] = speed
    
    def commit_speed_changes(self):
        triange_pwm = WheelHandler.convert_speed_to_pwm(self.buffer['triange'])
        # build the instruction string
        # send instruction
        self.buffer = {
            "triangle": 0,
            "square": 0,
            "circle": 0,
            "plus": 0,
        }
