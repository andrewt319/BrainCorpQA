from slow_car import SlowCar
from base_car import BaseCar
from car_gear import CarGear
import pytest

def test_slow_car_max_speed():
    car = SlowCar()
    assert car.max_speed == 0.75 * BaseCar.max_speed

    car.on()
    car.gas(100)
    assert car.speed == 37.5

def test_slow_car_acceleration():
    car = SlowCar()
    assert car.acceleration == 0.75 * BaseCar.acceleration

    car.on()
    car.gas(5)
    assert car.speed == 18.75

def test_slow_car_brake_efficiency():
    car = SlowCar()
    assert car.brake_efficiency == 2 * BaseCar.brake_efficiency

    car.on()
    car.gas(100)
    car.brake(1)
    assert car.speed == 17.5

