class Vehicle:
    def Getdetails(self):
        print("\nEnter Vehicle Details")
        self.make = input("Enter company name        : ")
        self.year = int(input("Enter manufacturing year : "))
        self.colour = input("Enter colour             : ")

    def display_info(self):
        print("\n----- VEHICLE DETAILS -----")
        print("\nMake   :", self.make)
        print("Year   :", self.year)
        print("Colour :", self.colour)


class Car(Vehicle):
    def GetCarDetails(self):
        print("\nEnter Car Details")
        self.model = input("Enter car model          : ")
        self.capacity = int(input("Enter seating capacity   : "))
        self.fuel = input("Enter fuel type          : ")

    def Display_car(self):
        print("\n----- CAR DETAILS -----")
        self.display_info()
        print("Model      :", self.model)
        print("Capacity   :", self.capacity)
        print("Fuel Type  :", self.fuel)


class Bike(Vehicle):
    def GetBikeDetails(self):
        print("\nEnter Bike Details")
        self.type = input("Enter bike type          : ")
        self.mileage = float(input("Enter mileage (km/l)     : "))
        self.gear = int(input("Enter number of gears    : "))

    def Display_bike(self):
        print("\n----- BIKE DETAILS -----")
        self.display_info()
        print("Type      :", self.type)
        print("Mileage   :", self.mileage)
        print("Gears     :", self.gear)


# Main Program
while True:
    print("\n========= VEHICLE MANAGEMENT =========")
    print("1. Car")
    print("2. Bike")
    print("3. Exit")

    ch = int(input("Enter your choice : "))

    if ch == 1:
        c1 = Car()
        c1.Getdetails()
        c1.GetCarDetails()
        c1.Display_car()

    elif ch == 2:
        b1 = Bike()
        b1.Getdetails()
        b1.GetBikeDetails()
        b1.Display_bike()

    elif ch == 3:
        print("\nThank You...")
        break

    else:
        print("\nInvalid Choice")
