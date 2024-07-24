from typing import Protocol, Literal


class Vehicle(Protocol):
    name: str

    def turn_on(self) -> None: ...

    def turn_off(self) -> None: ...


class Factory(Protocol):

    def construct_vehicle(self) -> Vehicle: ...


class Car(Vehicle):
    name: str = "car"

    def turn_on(self) -> None:
        print("turning the car on")


class CarFactory:

    def construct_vehicle(self) -> Car:
        return Car()


class MotorCycle(Vehicle):
    name: str = "motor cycle"

    def turn_on(self) -> None:
        print("turning the motorcycle on")


class MotorCycleFactory:

    def construct_vehicle(self) -> MotorCycle:
        return MotorCycle()


class Concessionary:
    vehicle: Vehicle
    factory: Factory

    def __init__(self, vehicle_type: Literal["car", "motorcycle"]):
        if vehicle_type == "car":
            self.factory = CarFactory()
        elif vehicle_type == "motorcycle":
            self.factory = MotorCycleFactory()

    def client_buys(self) -> Vehicle:
        return self.factory.construct_vehicle()


if __name__ == "__main__":
    moto_concessionary = Concessionary(vehicle_type="motorcycle")
    moto = moto_concessionary.client_buys()

    moto.turn_on()
    moto.turn_off()

    car_concessionary = Concessionary(vehicle_type="car")
    car = car_concessionary.client_buys()

    car.turn_on()
    car.turn_off()