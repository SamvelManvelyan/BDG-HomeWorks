# 10. Class Exercise:
# Create a Python class representing a car with methods for accelerating and braking..

class Car:
    def __init__(self, model, year, speed):
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, gaz=5):
        self.speed += gaz
        print("car speed" ,  self.speed)

    def brake(self, argelakum=5):
            self.speed -= argelakum
            print("car speed" , self.speed)


my_car = Car("Chevrolet" , 2014 , 100)
my_car.accelerate()
my_car.accelerate(15)
my_car.brake(10)
my_car.brake(20)
