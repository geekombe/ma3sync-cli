import sqlite3

class BusManagement:
    def __init__(self, db_name='bus_management.db'):
        self.db_connection = sqlite3.connect(db_name)
        self.db_cursor = self.db_connection.cursor()
        self.setup_tables()

    def setup_tables(self):
        """Create necessary tables if they don't exist."""
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS buses (
                bus_id INTEGER PRIMARY KEY,
                capacity INTEGER NOT NULL
            )
        """)
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS passengers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                bus_id INTEGER NOT NULL,
                FOREIGN KEY (bus_id) REFERENCES buses(bus_id)
            )
        """)
        self.db_connection.commit()

    def register_bus(self, bus_id, capacity):
        """Add a new bus to the database."""
        try:
            self.db_cursor.execute("INSERT INTO buses (bus_id, capacity) VALUES (?, ?)", (bus_id, capacity))
            self.db_connection.commit()
            print(f"Bus {bus_id} added successfully with capacity {capacity}.")
        except sqlite3.IntegrityError:
            print("This bus ID already exists.")

    def add_passenger_to_bus(self, name):
        """Automatically add a passenger to a bus with available seats."""
        self.db_cursor.execute("SELECT * FROM passengers WHERE name = ?", (name,))
        if self.db_cursor.fetchone():
            print(f"{name} is already added to a bus.")
            return
        
        self.db_cursor.execute("""
            SELECT buses.bus_id, buses.capacity - COUNT(passengers.id) as available_seats
            FROM buses
            LEFT JOIN passengers ON buses.bus_id = passengers.bus_id
            GROUP BY buses.bus_id
            HAVING available_seats > 0
            ORDER BY available_seats DESC
            LIMIT 1
        """)
        bus = self.db_cursor.fetchone()
        if bus:
            bus_id, _ = bus
            try:
                self.db_cursor.execute("INSERT INTO passengers (name, bus_id) VALUES (?, ?)", (name, bus_id))
                self.db_connection.commit()
                print(f"Added {name} to bus {bus_id} successfully.")
            except sqlite3.IntegrityError as e:
                print("Error adding passenger:", e)
        else:
            print("No available seats on any bus for {name}.")

    def list_passengers(self):
        """List all passengers."""
        self.db_cursor.execute("SELECT name, bus_id FROM passengers ORDER BY bus_id, name")
        for row in self.db_cursor.fetchall():
            print(f"Passenger: {row[0]}, Bus ID: {row[1]}")

    def close(self):
        """Close the database connection."""
        self.db_connection.close()

def main():
    bm = BusManagement()
    try:
        while True:
            role = input("Login as 1. User 2. Admin (Enter number or 'exit' to quit): ").strip()
            if role.lower() == 'exit':
                break
            elif role == '1':
                name = input("Enter your name: ").strip()
                bm.add_passenger_to_bus(name)
            elif role == '2':
                # Prompt for the Admin password
                password = input("Enter Admin password: ").strip()
                if password == "1234":
                    action = input("Choose action: 1. Add Bus 2. Add Passenger 3. List Passengers (Enter number): ").strip()
                    if action == '1':
                        bus_id = int(input("Enter new bus ID: ").strip())
                        capacity = int(input("Enter bus capacity: ").strip())
                        bm.register_bus(bus_id, capacity)
                    elif action == '2':
                        name = input("Enter passenger name: ").strip()
                        bm.add_passenger_to_bus(name)
                    elif action == '3':
                        bm.list_passengers()
                else:
                    print("Invalid password. Access denied.")
            else:
                print("Invalid role selection. Please enter 1 for User or 2 for Admin.")
    finally:
        bm.close()

if __name__ == "__main__":
    main()
