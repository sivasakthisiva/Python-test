class product:
    def __init__(self,name,org_price,dis_price=10):
        self.product_name=name
        self.org_price=org_price
        self.dis_price=dis_price
    def disval(self):
        return self.org_price*self.dis_price/100
    def product(self):
        print("Your Product Name :",self.product_name)
        print("Actual Price :",self.org_price)
        print("Discount For this Product :",self.dis_price,"%")
        print("Discounted Value :",self.disval())
        print("Final Total Value :",self.org_price-self.disval())
disp=product("Red",100)
disp1=product("Milk",40,5)
disp.product()
disp1.product()