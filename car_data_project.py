# ## First attempt
# ## Worls but doesn't store user entry beyond the sesion, lines 3-30
# from dataclasses import dataclass

# @dataclass
# class Car:
#     manu: str
#     mod: str
#     year: int

# cars = [
#     Car(manu="Nissan", mod="350z", year=2003),
#     Car(manu="Mazda",mod= "RX-7",year= 1997),
#     Car(manu="Subaru",mod="Impreza",year=1995),
# ]
# start=int(input("For new entry type 1 for search type 2"))
# if start == 1:
#     new_entry_manu=input("Manufacturer? ")
#     new_entry_mod=input("Model? ")
#     new_entry_year=int(input("Year? "))
#     new_car = Car(manu=new_entry_manu, mod=new_entry_mod, year=new_entry_year)
#     cars.append(new_car)
#     print(f"{new_car} added to the list.")

# if start == 2:
#     search_manu = input("Car brand")
#     found_car = next((car for car in cars if car.manu.lower() == search_manu.lower()), None)
#     print(f"Manufacturer:{found_car.manu}, Model:{found_car.mod} Year:{found_car.year}")
# else:
#     print("User not found.")
# Second attempt, works and stores new entries in the JSON file. Still only allows searchiung
# by manufacturer/brand, and will load everyone that has that manu class. 
import json
from dataclasses import dataclass, asdict

@dataclass
class Car:
    manu: str
    mod: str
    year: int

# Load existing cars from file (if available)
try:
    with open("cars.json", "r") as f:
        cars_data = json.load(f)
        cars = [Car(**entry) for entry in cars_data]
except FileNotFoundError:
    cars = []

start = int(input("For new entry type 1, for search type 2: "))

if start == 1:
    new_entry_manu = input("Manufacturer? ")
    new_entry_mod = input("Model? ")
    new_entry_year = int(input("Year? "))
    new_car = Car(manu=new_entry_manu, mod=new_entry_mod, year=new_entry_year)
    cars.append(new_car)

    # Save updated list to JSON file
    with open("cars.json", "w") as f:
        json.dump([asdict(car) for car in cars], f, indent=4)

    print(f"{new_car} added to the list.")

elif start == 2:
    search_manu = input("Car brand? ")
    found_cars = [car for car in cars if car.manu.lower() == search_manu.lower()]
    if found_cars:
        print(found_cars)
        # print(f"Manufacturer: {found_car.manu}, Model: {found_car.mod}, Year: {found_car.year}")
    else:
        print("Car not found.")

else:
    print("Invalid selection.")
