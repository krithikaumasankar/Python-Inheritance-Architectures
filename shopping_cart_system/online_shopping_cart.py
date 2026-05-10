#ONLINE SHOPPING CART
# Base Class
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def add_to_cart(self):
        print(f"\n{self.name} added to cart.")

    def get_details(self):
        print("\n---Product Details---")
        print("\nID:", self.pid)
        print("Name:", self.name)
        print("Price:", self.price)

    def display(self):
        print(f"{self.name} - ₹{self.price}")


# Derived Class: Electronics
class Electronics(Product):
    def __init__(self, pid, name, price, brand, warranty):
        super().__init__(pid, name, price)
        self.brand = brand
        self.warranty = warranty

    def get_electronics_details(self):
        self.get_details()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")

    def display(self):
        print(f"Electronics: {self.name}, Brand: {self.brand}, Price: ₹{self.price}")


# Derived Class: Clothing
class Clothing(Product):
    def __init__(self, pid, name, price, cloth_type, size, color):
        super().__init__(pid, name, price)
        self.cloth_type = cloth_type
        self.size = size
        self.color = color

    def get_cloth_details(self):
        self.get_details()
        print("Type:", self.cloth_type)
        print("Size:", self.size)
        print("Color:", self.color)

    def display(self):
        print(f"Clothing: {self.name}, Type: {self.cloth_type}, Size: {self.size}, Price: ₹{self.price}")


# -------- Main Program --------
print("\n\tONLINE SHOPPING CART\n")
print("1. Electronics\n2. Clothing")
choice = int(input("Enter your choice: "))

pid = int(input("\nEnter Product ID: "))
name = input("Enter Product Name: ")
price = float(input("Enter Price: "))

if choice == 1:
    brand = input("Enter Brand: ")
    warranty = int(input("Enter Warranty (years): "))

    item = Electronics(pid, name, price, brand, warranty)
    item.add_to_cart()
    item.get_electronics_details()
    item.display()

elif choice == 2:
    cloth_type = input("Enter Clothing Type: ")
    size = input("Enter Size: ")
    color = input("Enter Color: ")

    item = Clothing(pid, name, price, cloth_type, size, color)
    item.add_to_cart()
    item.get_cloth_details()
    item.display()

else:
    print("Invalid choice!")
