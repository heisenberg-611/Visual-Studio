# from car import Car

# car_1 = Car("Chevy","Corvett",2021,"blue")
# car_2 = Car("Ford","Mustang",2022,"red")

# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)

# car_1.drive()
# car_2.stop()

# car_1.wheels = 2
# Car.wheels = 2
# print(car_1.wheels)
# print(car_2.wheels)

# print(Car.wheels)

# class Animal:

#     alive = True

#     def eat (self):
#         print("This animal is eating")
    
#     def sleep(self):
#         print("This animal is sleeping")

# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running")
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying")

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

# rabbit.run()
# fish.swim()
# hawk.fly()


#Multi level inheritence

# class Organism:

#     alive = True

# class Animal(Organism):

#     def eat(self):
#         print("This animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("This dog is barking")

# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

#Multiple inheritence

# class Prey:

#     def flee(self):
#         print("This animal flees")

# class Predetor:

#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predetor):
#     pass

# class Fish(Prey, Predetor):
#     pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# fish.flee()
# rabbit.flee()

#Method Overriding

# class Animal:

#     def eat(self):
#         print("This animal is eating")

# class Rabbit(Animal):
#     def eat(self):
#         print("This rabbit is eating is eating a carrot")

# rabbit = Rabbit()
# rabbit.eat()

#method chaining = calling multiple method sequentially

# class Car:
#     def turn_on(self):
#         print("You start the engine")
#         return self
#     def drive(self):
#         print("You drive the car")
#         return self
#     def brake(self):
#         print("You step on the brakes")
#         return self
#     def turn_off(self):
#         print("You turn off the engine")
#         return self

# car = Car()

# car.turn_on().drive()

# car.brake().turn_off()

# car.turn_on().drive().brake().turn_off()

#super() = Function used to give access to the methods of a parent class.
#          Returns a temporary ovject of a parent class when used

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    

# class Square(Rectangle):
#     def __init__(self, length, width):
#         super().__init__(length, width)
#     def area(self):
#         return self.length*self.width

# class Cube(Rectangle):

#     def __init__(self,length,width, height):
#         super().__init__(length, width)
#         self.height = height

#     def volume(self):
#         return self.length*self.width*self.height

# square = Square(3,3)
# cube = Cube(3,3,3)

# print(square.area())
# print(cube.volume())

