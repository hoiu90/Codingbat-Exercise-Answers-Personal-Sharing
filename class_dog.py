class reastaurant:
    def __init__(self, name, type,boss_name):
        self.name = name
        self.type = type
        self.boss_name = boss_name
        self.num=0
    def drink(self):
        print(self.name + " is drinking.")
    def eat(self):
        print(self.name + " is eating.")
    def describe(self):
        print("This is a " + self.type + " restaurant.")
    def boss(self):
        print(self.name + " is boss by " + self.boss_name + ".")
    def set_num(self):
        print(f"The number of people in {self.name} is {self.num}.")
    def increment_num(self,count=1):
        if count>0:
            self.num+=count
        else:
            print("The count should be positive.")
            
class_rest=reastaurant("Tacos", "Mexican","juan")
print(f"this reastaurant's name is {class_rest.name} and type is {class_rest.type}")

class_rest.describe()
class_rest.eat()
class_rest.boss()

reastaurant.set_num()
reastaurant.set_num(10)
