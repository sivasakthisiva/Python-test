class Vehicle:
    def __init__(self,brand):
        self.brand=brand
class car(Vehicle):
    def display(self):
        print("Brand Name is :",self.brand)
class bike(Vehicle):
    def display(self):
        print("Brand Name is :",self.brand)
disp=car("BMW")
disp2=bike("KTM")
disp.display()
disp2.display()