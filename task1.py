class Car:

    def __init__(self, color = 'white', engine_power = 90, tank_capacity = 50, fuel_consumption = 9.3, fuel_now = 0):
        self.color = color
        self.engine_power = engine_power
        self.tank_capacity = tank_capacity
        self.fuel_consumption = fuel_consumption
        self.fuel_now = fuel_now

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_fuel_now(self):
        return self.fuel_now

    def refuel(self, liters_of_fuel):
        if liters_of_fuel + self.fuel_now <= self.tank_capacity:
            self.fuel_now += liters_of_fuel

    def get_engine_power(self):
        return self.engine_power

    def get_fuel_consumption(self):
        return self.fuel_consumption


def test_init_1():
    Car(color='white',
        engine_power=90,
        tank_capacity=50,
        fuel_consumption=9.3,
        fuel_now=0)


def test_init_2():
    Car(color='white')


def test_color_1():
    c = Car(color='white',
            engine_power=90,
            tank_capacity=50,
            fuel_consumption=9.3,
            fuel_now=0)
    assert c.get_color() == 'white'


def test_color_2():
    c = Car(color='white',
            engine_power=90,
            tank_capacity=50,
            fuel_consumption=9.3,
            fuel_now=0)
    assert c.get_color() == 'white'
    c.set_color('red')


def test_color_3():
    c = Car(color='white',
            engine_power=90,
            tank_capacity=50,
            fuel_consumption=9.3,
            fuel_now=0)
    assert c.get_color() == 'white'
    c.set_color('red')

    assert c.get_color() == 'red'


test_color_1()
test_color_2()
test_color_3()
test_init_1()
test_init_2()
