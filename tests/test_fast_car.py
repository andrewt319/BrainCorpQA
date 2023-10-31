from fast_car import FastCar
from car_gear import CarGear
import pytest

def test_fast_car_on_off():
    car = FastCar()
    car.on()
    assert car.engine is True
    assert car.gear == CarGear.DRIVE

    car.off()
    assert car.engine is False
    assert car.gear == CarGear.PARK

def test_fast_car_gas():
    car = FastCar()
    car.on()
    car.gas(5)
    assert car.speed == 5 * car.acceleration

def test_fast_car_gas_100seconds():
    car = FastCar()
    car.on()
    car.gas(100)
    assert car.speed == 150

def test_fast_car_acceleration():
    car = FastCar()
    car.on()
    car.gas(3)
    assert car.speed == 3 * car.acceleration

def test_fast_car_drive():
    car = FastCar()
    car.on()
    car.gas(5)
    car.drive(10)
    assert car.odometer == 10 * car.speed
    assert car.home == 10 * car.speed

def test_fast_car_brake():
    car = FastCar()
    car.on()
    car.gas(5)
    car.drive(10)
    car.brake(5)
    assert car.speed == 0