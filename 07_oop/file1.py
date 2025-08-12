# ****CLASS & MODEL****
# class volkswagon:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

# car = volkswagon("PoloGTI", "Blue")
# print(car.model)
# print(car.color)

# new_car = volkswagon("Golf-R", "Black")

# print(new_car.model)
# print(new_car.color)



# ****CLASS,METHOD & SELF****
# class car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# my_car = car("Volkswagon", "PoloGTi")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())




# ****INHERITANCE****
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
class Electric_Car(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 

tesla_car = Electric_Car("Tesla", "Model Y", "85kWh")
print(tesla_car.brand)
print(tesla_car.full_name())   