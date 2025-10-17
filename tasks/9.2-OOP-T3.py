class Stadium:
    def __init__(self, stadium_name = "", date_of_opening = "", country = "", city = "", seating_capacity = ""):
        self.stadium_name = stadium_name
        self.date_of_opening = date_of_opening
        self.country = country
        self.city = city
        self.seating_capacity = seating_capacity
    
    def input_data(self):
        self.stadium_name = input("Stadium name: ")
        self.date_of_opening = input("Date of opening: ")
        self.country = input("Country: ")
        self.city = input("City: ")
        self.seating_capacity = input("Seating capacity: ")

    def output_data(self):
        print(f"Stadium name: {self.stadium_name}")
        print(f"Date of opening: {self.date_of_opening}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Seating capacity: {self.seating_capacity}")

    def print_stadium_name(self):
        print(f"Stadium name: {self.stadium_name}")

    def print_date_of_opening(self):
        print(f"Date of opening: {self.date_of_opening}")

    def print_country(self):
        print(f"Country: {self.country}")

    def print_city(self):
        print(f"City: {self.city}")

    def print_seating_capacity(self):
        print(f"Seating capacity: {self.seating_capacity}")

stadium = Stadium()
stadium.input_data()
print("-" * 20)
stadium.output_data()
print("-" * 20)
stadium.print_stadium_name()