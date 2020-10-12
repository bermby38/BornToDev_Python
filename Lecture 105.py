class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turnOnAirConditioner(self):
        print("Turn On : Air")


class Car(Vehicle):
    def sayhello(self):
        print("Hello World")


class Pickup(Vehicle):
    pass


class Van(Vehicle):
    pass


Car1 = Car()
Car1.turnOnAirConditioner()
Car1.sayhello()

Pickup1 = Pickup()
Pickup1.turnOnAirConditioner()

Van1 = Van()
Van1.turnOnAirConditioner()
