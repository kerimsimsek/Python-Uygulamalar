class Car:
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
        self.is_running = False
        self.speed = 0

    def start(self):
        if not self.is_running:
            print(f"The {self.color} {self.brand} {self.model} is starting.")
            self.is_running = True
        else:
            print("The car is already running.")

    def stop(self):
        if self.is_running:
            print(f"The {self.color} {self.brand} {self.model} is stopping.")
            self.is_running = False
            self.speed = 0
        else:
            print("The car is already stopped.")

    def accelerate(self, amount):
        if self.is_running:
            self.speed += amount
            print(f"The {self.color} {self.brand} {self.model} is accelerating. Current speed: {self.speed} km/h")
        else:
            print("Cannot accelerate, the car is not running.")

    def brake(self, amount):
        if self.is_running:
            if self.speed >= amount:
                self.speed -= amount
                print(f"The {self.color} {self.brand} {self.model} is slowing down. Current speed: {self.speed} km/h")
            else:
                print("Cannot brake beyond the current speed.")
        else:
            print("Cannot brake, the car is not running.")

# Örnek kullanım
my_car = Car(color="Red", brand="Toyota", model="Camry")
my_car.start()
my_car.accelerate(50)
my_car.brake(20)
my_car.stop()
