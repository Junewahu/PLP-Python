# Define the Smartphone class
class Smartphone:
    # Constructor (__init__ method) to initialize attributes
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand  # Attribute: Brand of the smartphone
        self.model = model  # Attribute: Model of the smartphone
        self.storage = storage  # Attribute: Storage capacity in GB
        self.battery_life = battery_life  # Attribute: Battery life in hours

    # Method to display smartphone details
    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours")

    # Method to simulate using the smartphone
    def use(self, hours):
        if hours <= self.battery_life:
            self.battery_life -= hours
            print(f"Used {hours} hours. Remaining battery: {self.battery_life} hours.")
        else:
            print("Not enough battery!")

# Create an object (instance) of the Smartphone class
my_phone = Smartphone("Apple", "iPhone 15", 128, 24)

# Call methods on the object
my_phone.display_details()
my_phone.use(5)
my_phone.display_details()

# Define the GamingPhone subclass
class GamingPhone(Smartphone):
    # Constructor for GamingPhone
    def __init__(self, brand, model, storage, battery_life, graphics_card):
        super().__init__(brand, model, storage, battery_life)  # Call the parent class constructor
        self.graphics_card = graphics_card  # New attribute

    # New method specific to GamingPhone
    def play_game(self, hours):
        if hours <= self.battery_life:
            self.battery_life -= hours
            print(f"Played game for {hours} hours. Remaining battery: {self.battery_life} hours.")
        else:
            print("Not enough battery!")

# Create an object of the GamingPhone class
my_gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, 36, "Adreno 660")

# Call methods
my_gaming_phone.display_details()
my_gaming_phone.play_game(3)