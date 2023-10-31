from base_car import BaseCar

"""
Represents a fast car with enhanced performance based on the BaseCar class.
Attributes:
    max_speed (float): The maximum speed in meters per second.
    acceleration (float): The acceleration rate in meters per second squared.
    brake_efficiency (float): The brake efficiency in meters per second squared.
"""
class FastCar(BaseCar):
    """
    Initialize a new FastCar instance with enhanced performance.
    """
    def __init__(self):
        super().__init__()
        self.max_speed = 3 * BaseCar.max_speed
        self.acceleration = 2 * BaseCar.acceleration
        self.brake_efficiency = BaseCar.brake_efficiency
