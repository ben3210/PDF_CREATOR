class Car:
    def __init__(self, model = "", year_of_release = "", manufacturer = "", engine_capacity = "", color = "", price = ""):
        self.model = model
        self.year_of_release = year_of_release
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price
    
    def input_data(self):
        self.model = input("Model: ")
        self.year_of_release = input("Year of Release: ")
        self.manufacturer = input("Manufacturer: ")
        self.engine_capacity = input("Engine Capacity: ")
        self.color = input("Color: ")
        self.price = input("Price: ")

    def output_data(self):
        print(f"Model: {self.model}")
        print(f"Year of Release: {self.year_of_release}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine Capacity: {self.engine_capacity}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")

    def print_model(self):
        print(f"Model: {self.model}")

    def print_year_of_release(self):
        print(f"Year of Release: {self.year_of_release}")

    def print_manufacturer(self):
        print(f"Manufacturer: {self.manufacturer}")

    def print_engine_capacity(self):
        print(f"Engine Capacity: {self.engine_capacity}")

    def print_color(self):
        print(f"Color: {self.color}")

    def print_price(self):
        print(f"Price: {self.price}")

car = Car()
car.input_data()
print("-" * 20)
car.output_data()
print("-" * 20)
car.print_model()