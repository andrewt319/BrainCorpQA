from base_car import BaseCar

"""
Represents a slow car that inherits from the BaseCar class.
"""
class SlowCar(BaseCar):
    """
    Initialize a new SlowCar instance.
    """
    def __init__(self):
        super().__init__()
        self.max_speed = 0.75 * BaseCar.max_speed  # Maximum speed of the slow car
        self.acceleration = 0.75 * BaseCar.acceleration  # Acceleration rate of the slow car
        self.brake_efficiency = 2 * BaseCar.brake_efficiency  # Brake efficiency of the slow car
