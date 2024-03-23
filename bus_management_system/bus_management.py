
from sqlalchemy.exc import IntegrityError
from .database import Session
from .models import Bus, Passenger, Admin, User
from werkzeug.security import generate_password_hash, check_password_hash

class BusManagement:
    def __init__(self):
        self.session = Session()

    def add_bus(self, capacity):
        new_bus = Bus(capacity=capacity)
        self.session.add(new_bus)
        try:
            self.session.commit()
            print(f"Added bus with capacity {capacity}.")
        except IntegrityError:
            print("Failed to add bus. It might already exist.")
            self.session.rollback()

    def add_passenger(self, name, bus_id):
        new_passenger = Passenger(name=name, bus_id=bus_id)
        self.session.add(new_passenger)
        try:
            self.session.commit()
            print(f"Added passenger {name} to bus {bus_id}.")
        except IntegrityError:
            print("Failed to add passenger. There might be a problem with the bus ID or the passenger name might already be taken.")
            self.session.rollback()


    def list_passengers_and_users(self):
        print("\nCurrent Bus Occupants:")

        passengers = self.session.query(Passenger).all()
        if passengers:
            print("\nRegistered Passengers:")
            for passenger in passengers:
                print(f"Passenger Name: {passenger.name}, Bus ID: {passenger.bus_id}")

        users = self.session.query(User).filter(User.bus_id.isnot(None)).all()
        if users:
            print("\nUsers Who Booked a Bus:")
            for user in users:
                print(f"User: {user.username}, Booked Bus ID: {user.bus_id}")

        if not passengers and not users:
            print("No current bus occupants.")


    def authenticate_admin(self, username, password):
        admin = self.session.query(Admin).filter_by(username=username, password=password).first()
        return admin is not None

    def delete_bus(self, bus_id):
        bus_to_delete = self.session.query(Bus).filter_by(id=bus_id).first()
        if bus_to_delete:
            self.session.delete(bus_to_delete)
            self.session.commit()
            print(f"Deleted bus {bus_id}.")
        else:
            print("Bus not found.")

    def delete_passenger(self, passenger_id):
        passenger_to_delete = self.session.query(Passenger).filter_by(id=passenger_id).first()
        if passenger_to_delete:
            self.session.delete(passenger_to_delete)
            self.session.commit()
            print(f"Deleted passenger {passenger_id}.")
        else:
            print("Passenger not found.")

    def list_buses(self):
        buses = self.session.query(Bus).all()
        if buses:
            print("\nAvailable Buses:")
            for bus in buses:
                print(f"Bus ID: {bus.id}, Capacity: {bus.capacity}, Passengers: {len(bus.passengers)}")
        else:
            print("No buses available.")
    def register_user(self, username, password):
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        self.session.add(new_user)
        try:
            self.session.commit()
            print("User registration successful.")
        except IntegrityError:
            print("This username is already taken.")
            self.session.rollback()

    def login_user(self, username, password):
        user = self.session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            print(f"Login successful. Welcome, {username}!")
            return user
        else:
            print("Invalid username or password.")
            return None

    def book_bus_for_user(self, username, bus_id):
        user = self.session.query(User).filter_by(username=username).first()
        bus = self.session.query(Bus).filter_by(id=bus_id).first()
        if user and bus:
            if user.bus:
                print(f"You have already booked a bus (Bus ID: {user.bus_id}).")
            else:
                user.bus_id = bus_id
                self.session.commit()
                print(f"Bus (ID: {bus_id}) booked successfully.")
        elif not bus:
            print("Bus ID not found.")

    def list_users(self):
        users = self.session.query(User).all()
        if users:
            print("\nList of registered users:")
            for user in users:
                booked_bus = "Not booked" if not user.bus_id else f"Booked Bus ID: {user.bus_id}"
                print(f"Username: {user.username}, {booked_bus}")
        else:
            print("No users registered.")
