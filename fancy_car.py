from base_car import BaseCar
from car_gear import CarGear

"""
Represents a fancy car that inherits from the BaseCar class.
"""
class FancyCar(BaseCar):
    """
    Initialize a new FancyCar instance with extra features.
    """
    def __init__(self):
        super().__init__()
        self.max_speed = 2 * BaseCar.max_speed  
        self.acceleration = BaseCar.acceleration  
        self.brake_efficiency = BaseCar.brake_efficiency  

    """
    Change the gear of the car between Drive and Reverse.
    Can only change gears if the car is not in motion.
    """
    def drive_reverse(self):
        self.check_car_speed_zero()
        if self.gear == CarGear.DRIVE:
            self.gear = CarGear.REVERSE
        else:
            self.gear = CarGear.DRIVE
    
    """
    Override parent drive method so if we are in reverse, to detect
    that in our distance from home
    """
    def drive(self, time):
        self.check_car_engine_on()
        self.odometer += self.speed * time
        if self.gear == CarGear.DRIVE:
            self.home += self.speed * time
        else:
            self.home -= self.speed * time

    
    """Activate the car's horn to make a "Beep Beep" sound."""
    def horn(self):
        print("Beep Beep")