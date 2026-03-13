class Mobile:
    def __init__(self):
        self.__price = 0 
    def set_price(self, price):
        self.__price = price  
    def get_price(self):
        print("Mobile price is:", self.__price)
m1 = Mobile()
m1.set_price(25000)  
m1.get_price()        