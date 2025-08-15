class cars:
    tm = price = ""
    

    def __init__(self, tm, price):
        self.tm = tm
        self.price = price

    def car_price(self, price):
        print(self.name, 'at the price of', price)

    def speed(self, speed):
        print(self.speed, 'with maximum speed', speed)
   
    def fuel(self,fuel):
        print(self.fuel, 'needs fuel with', fuel)



lamborghini = cars("Automobili Lamborghini©", "$500.000")
lamborghini.speed("300 Km/H")
lamborghini.fuel("octane 91 or higher")

vw = cars("VolksWagen©", "$250.000")
vw.speed("150 Km/H")
vw.fuel("octane 87")

toyota = cars("VolksWagen©", "$250.000")
toyota.speed("150 Km/H")
toyota.fuel("octane 87")
