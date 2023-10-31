from fancy_car import FancyCar
from car_gear import CarGear
import pytest

def test_fancy_car_drive_reverse():
    car = FancyCar()
    car.on()
    car.gas(5)
    car.drive(10)
    
    with pytest.raises(ValueError):
        car.drive_reverse()
    
    car.brake(10)
    car.drive_reverse()
    assert car.gear == CarGear.REVERSE
    
    car.drive_reverse()
    assert car.gear == CarGear.DRIVE

def test_fancy_car_drive_reverse_odometer_and_home():
    car = FancyCar()
    car.on()
    car.gas(5)
    car.drive(10)

    assert car.odometer == car.speed * 10

    car.brake(10)
    car.drive_reverse()
    car.gas(5)
    car.drive(5)

    assert car.odometer == car.speed * 15
    assert car.home == car.speed * 5

def test_fancy_car_horn():
    car = FancyCar()
    car.horn() 

def test_fancy_car_max_speed():
    car = FancyCar()
    assert car.max_speed == 2 * FancyCar.max_speed

def test_fancy_car_acceleration():
    car = FancyCar()
    assert car.acceleration == FancyCar.acceleration

def test_fancy_car_brake_efficiency():
    car = FancyCar()
    assert car.brake_efficiency == FancyCar.brake_efficiency
