# Inheritence in Python
class Car :
    
    @staticmethod
    def start_car() :
        print('Car started...')
        
    @staticmethod
    def stop_car () :
        print("Car stopped.")

class ToyotoCar(Car) :
    def __init__ (self,name):
        self.name = name
    

car_1 = ToyotoCar("fortuner")
car_2 = ToyotoCar("prius")
print(car_1.name)
car_1.start_car()
car_1.stop_car()