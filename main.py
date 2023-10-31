from fast_car import FastCar
from slow_car import SlowCar
from fancy_car import FancyCar

def main():
    fast_car = FastCar()
    slow_car = SlowCar()
    fancy_car = FancyCar()

    fast_car.on()
    fancy_car.on()
    slow_car.on()

    fast_car.toggle_headlights()
    fancy_car.toggle_headlights()

    fast_car.gas(11)
    slow_car.gas(11)
    fancy_car.gas(11)

    fast_car.drive(30)
    slow_car.drive(30)
    fancy_car.drive(30)

    fancy_car.brake(5)
    fancy_car.drive(3)

    slow_car.brake(6)

    fancy_car.brake(5)
    fancy_car.drive_reverse()
    fancy_car.gas(20)
    fancy_car.drive(30)

    slow_car.brake(10)
    slow_car.off()

    fancy_car.toggle_headlights()

    fast_car.drive(30)
    fast_car.gas(20)
    fast_car.drive(60)

    fast_car.check_dashboard()
    fancy_car.check_dashboard()
    slow_car.check_dashboard()

    fancy_car.horn()
    fancy_car.horn()

    slow_car.on()
    slow_car.toggle_headlights()
    slow_car.gas(4)
    slow_car.drive(2000)

    slow_car.check_dashboard()

    car_2 = FancyCar()
    car_2.toggle_headlights()
    car_2.on()
    car_2.drive_reverse()
    car_2.gas(1)
    car_2.drive(10)
    car_2.check_dashboard()

if __name__ == "__main__":
    main()
