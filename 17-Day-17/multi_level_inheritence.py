# Multi level Inheritence in Python

# Base Class
class Car :
    @staticmethod
    def start_car() :
        print('Car started...')
        
    @staticmethod
    def stop_car () :
        print("Car stopped.")
        
        
# Class 2 
class ToyotoCar(Car) :
    
    def __init__ (self,brand):
        self.brand = brand

class fortuner (ToyotoCar):
    def __init__ (self, type) :
        self.type = type
        
car_1 = fortuner("Diesel")
# Accessing the start method for var 1 which is in the Base class or first class 
car_1.start_car()