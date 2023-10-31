from car_gear import CarGear

"""
Represents a basic car with standard functionality.
"""
class BaseCar:
    """
    Initialize a new BaseCar instance.
    """
    def __init__(self):
        self.engine = False
        self.headlights = False
        self.speed = 0
        self.odometer = 0
        self.home = 0  # distance from 'home' in meters
        self.gear = CarGear.PARK

    """
    Turn on the car's engine and set the gear to Drive.
    Raises: ValueError: If the engine is already turned on.
    """
    def on(self):
        self.check_car_engine_off()
        self.engine = True
        self.gear = CarGear.DRIVE

    """
    Turn off the car's engine and set the gear to Park.
    Raises: ValueError: If the engine is already turned off or if the car is in motion.
    """
    def off(self):
        self.check_car_speed_zero()
        self.engine = False
        self.gear = CarGear.PARK

    """
    Add gas to accelerate the car.
    Args: time (float): The time in seconds for which the gas pedal is pressed.
    Raises:
        ValueError: If the engine is not turned on.
    """
    def gas(self, time):
        self.check_car_engine_on()
        self.speed = min(self.max_speed, self.speed + time * self.acceleration)

    """
    Drive the car for a specified time.
    Args: time (float): The time in seconds for which the car should drive.
    Raises: ValueError: If the engine is not turned on.
    """
    def drive(self, time):
        self.check_car_engine_on()
        self.odometer += self.speed * time
        self.home += self.speed * time

    """
    Apply the brakes to slow down the car.
    Args: time (float): The time in seconds for which the brake pedal is pressed.
    Raises: ValueError: If the engine is not turned on.
    """
    def brake(self, time):
        self.check_car_engine_on()
        self.speed = max(0, self.speed - time * self.brake_efficiency)

    """
    Toggle the car's headlights on or off, independent of the engine state.
    """
    def toggle_headlights(self):
        self.headlights = not self.headlights

    """
    Display the car's current status on the dashboard.
    """
    def check_dashboard(self):
        print(f"engine: {'On' if self.engine else 'Off'}")
        print(f"lights: {'On' if self.headlights else 'Off'}")
        print(f"speed: {self.speed} m/s")
        print(f"odometer: {self.odometer} m")
        print(f"home: {abs(self.home)} m")
        print(f"gear: {self.gear.name}")
        print()

    """
    Check if the car's engine is turned off and raise an error if it's on.
    Raises: ValueError: If the engine is turned on.
    """
    def check_car_engine_on(self):
        if not self.engine:
            raise ValueError("Car is not turned on")

    """
    Check if the car's engine is turned on and raise an error if it's off.
    Raises: ValueError: If the engine is turned off.
    """
    def check_car_engine_off(self):
        if self.engine:
            raise ValueError("Car is already on")

    """
    Check if the car's speed is zero and raise an error if it's not.
    Raises: ValueError: If the car is in motion.
    """
    def check_car_speed_zero(self):
        if self.speed != 0:
            raise ValueError("Car cannot be turned off when speed isn't zero")

BaseCar.max_speed = 50
BaseCar.acceleration = 5
BaseCar.brake_efficiency = 10
