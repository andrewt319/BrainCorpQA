from base_car import BaseCar
from car_gear import CarGear
import pytest

def test_base_car_on_off():
    car = BaseCar()
    car.on()
    assert car.engine == True
    assert car.gear == CarGear.DRIVE

    car.off()
    assert car.engine == False
    assert car.gear == CarGear.PARK

def test_base_car_on_while_moving():
    car = BaseCar()
    car.on()
    car.gas(5)
    car.drive(10)
    with pytest.raises(ValueError):
        car.on()

def test_base_car_gas():
    car = BaseCar()
    car.on()
    car.gas(5)
    assert car.speed == 5 * car.acceleration

def test_base_car_gas_100second():
    car = BaseCar()
    car.on()
    car.gas(100)
    assert car.speed == 50

def test_base_car_drive():
    car = BaseCar()
    car.on()
    car.gas(5)
    car.drive(10)
    assert car.odometer == 10 * car.speed
    assert car.home == 10 * car.speed

def test_base_car_brake():
    car = BaseCar()
    car.on()
    car.gas(5)
    car.drive(10)
    car.brake(5)
    assert car.speed == 0

def test_base_car_brake_100seconds():
    car = BaseCar()
    car.on()
    car.gas(10)
    car.drive(10)
    car.brake(100)
    assert car.speed == 0

def test_base_car_toggle_headlights():
    car = BaseCar()
    car.toggle_headlights()
    assert car.headlights == True
    car.toggle_headlights()
    assert car.headlights == False

def test_base_car_odometer():
    car = BaseCar()
    car.on()
    car.gas(10)
    car.drive(10)
    assert car.odometer == 500

def test_base_car_off_while_moving():
    car = BaseCar()
    car.on()
    car.gas(5)
    with pytest.raises(ValueError):
        car.off()

def test_base_car_gas_while_off():
    car = BaseCar()
    with pytest.raises(ValueError):
        car.gas(5)

def test_base_car_drive_while_off():
    car = BaseCar()
    with pytest.raises(ValueError):
        car.drive(5)

def test_base_car_brake_while_off():
    car = BaseCar()
    with pytest.raises(ValueError):
        car.brake(5)