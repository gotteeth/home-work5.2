class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner


vehicle1 = Vehicle("ABC123", "Car", "Canelo Alverez")
vehicle2 = Vehicle("XYZ789", "Truck", "Gervonta Davis")

print(f"Original owner of vehicle1: {vehicle1.owner}")
vehicle1.update_owner("Jaron Ennis")
print(f"New owner of vehicle1: {vehicle1.owner}")

print(f"Original owner of vehicle2: {vehicle2.owner}")
vehicle2.update_owner("Jamie Munguia")
print(f"New owner of vehicle2: {vehicle2.owner}")
