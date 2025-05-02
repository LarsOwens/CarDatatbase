# ## First attempt
# ## Works but doesn't store user entry beyond the sesion, lines 3-32
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
## Attempt 3 to allow it to break down through each seach, make, then model then year. 
## It doesnt completely work but still placing it to learn from Attempt 4 which is 
## ChatGPT generated to fix. So ill compare the 2 and see where I went wrong and how I can 
## improve.

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
    found_manu = [car for car in cars if car.manu.lower() == search_manu.lower()]
    if found_manu:
        search_mod = input("Car model? ")
        found_mod = [car for car in cars if car.mod.lower() == search_mod.lower()]
        if found_mod:
            search_year = int(input("Car year? "))
            found_cars = [car for car in cars if car.year.lower() == search_year.lower()]
    
    if found_cars:
        print(found_cars)
        # print(f"Manufacturer: {found_car.manu}, Model: {found_car.mod}, Year: {found_car.year}")
    else:
        print("Car not found.")

else:
    print("Invalid selection.")


## Attempt 4, ChatGPT generated off of my original code. 
## After trial, it technically works since the database is so small and it doesn't 
## have a UI to see the models and years availble, so if your input doesn't exist it says not found
## If you leave the entry black it errors out.
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
    found_manu = [car for car in cars if car.manu.lower() == search_manu.lower()]
    
    if found_manu:  # Check if we found any cars with the manufacturer
        search_mod = input("Car model? ")
        found_mod = [car for car in found_manu if car.mod.lower() == search_mod.lower()]
        
        if found_mod:  # Check if we found any cars with the model
            search_year = input("Car year? ")
            # Convert the search_year to integer
            found_cars = [car for car in found_mod if car.year == int(search_year)]
        else:
            found_cars = found_mod  # If no model match, use the found cars from manufacturer search
    else:
        found_cars = found_manu  # If no manufacturer match, use the empty result
    
    if found_cars:
        print("Found cars:")
        for car in found_cars:
            print(f"Manufacturer: {car.manu}, Model: {car.mod}, Year: {car.year}")
    else:
        print("Car not found.")

else:
    print("Invalid selection.")
