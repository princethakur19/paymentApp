cars = ["thar", "scorpio", "xuv", "thar", "fortuner"]

unique_cars = set()

for car in cars:
    if car in unique_cars:
        print("Same car: ", car)
        break
    unique_cars.add(car)