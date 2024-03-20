class Bus():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            print(f"No available seats for {name}")
            return False
        self.passengers.append(name)
        print(f"Added {name} to the bus successfully")
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passengers_cli(self):
        print(f"Bus capacity is {self.capacity}. There are {self.open_seats()} seats available.")
        while self.open_seats() > 0:
            name = input("Enter passenger name (or type 'exit' to stop): ").strip()
            if name.lower() == 'exit':
                break
            self.add_passenger(name)
        if self.open_seats() == 0:
            print("The bus is now full.")
        else:
            print(f"Stopped adding passengers. {self.open_seats()} seats are still available.")

bus = Bus(3)

bus.add_passengers_cli()
