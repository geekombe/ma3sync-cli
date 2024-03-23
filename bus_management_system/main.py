from .database import init_db
from .bus_management import BusManagement
from .models import Bus, User


def main():
    init_db()
    bm = BusManagement()

    print("Welcome to the Bus Management System")
    role = input("Are you an admin or a user? (admin/user): ").lower()

    if role == "admin":
        username = input("Username: ")
        password = input("Password: ")
        if bm.authenticate_admin(username, password):
            admin_operations(bm)
        else:
            print("Authentication failed.")
    elif role == "user":
        user_operations(bm)
    else:
        print("Invalid role selected.")

def admin_operations(bm):
    while True:
        print("\nAdmin Operations")
        print("1. Add Bus")
        print("2. Delete Bus")
        print("3. Add Passenger")
        print("4. Delete Passenger")
        print("5. List Passengers")
        print("6. List Users")
        print("7. Exit")

        choice = input("Choose an action: ")
        if choice == '1':
            capacity = input("Enter bus capacity: ")
            bm.add_bus(capacity=int(capacity))
        elif choice == '2':
            bus_id = input("Enter bus ID to delete: ")
            bm.delete_bus(bus_id=int(bus_id))
        elif choice == '3':
            name = input("Enter passenger name: ")
            bus_id = input("Enter bus ID for the passenger: ")
            bm.add_passenger(name=name, bus_id=int(bus_id))
        elif choice == '4':
            passenger_id = input("Enter passenger ID to delete: ")
            bm.delete_passenger(passenger_id=int(passenger_id))
        elif choice == '5':
            bm.list_passengers_and_users()
        elif choice == '6':
            bm.list_users()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations(bm):
    print("\n1. Register")
    print("2. Login")
    choice = input("Choose an option: ")

    if choice == '1':
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        bm.register_user(username=username, password=password)
    elif choice == '2':
        username = input("Username: ")
        password = input("Password: ")
        user = bm.login_user(username=username, password=password)
        if user:
            if user.bus_id:
                show_bus_info(bm, user.bus_id)
            else:
                print("You have not booked any bus.")
                bm.list_buses()
                bus_id = input("Enter bus ID to book: ")
                try:
                    bm.book_bus_for_user(username, int(bus_id))
                except ValueError:
                    print("Please enter a valid numerical bus ID.")

def show_bus_info(bm, bus_id):
    bus = bm.session.query(Bus).filter_by(id=bus_id).first()
    if bus:
        remaining_seats = bus.capacity - len(bus.passengers) - len(bus.users)
        print(f"Bus ID: {bus.id}, Remaining Seats: {remaining_seats}")
    else:
        print("No bus found with the specified ID.")


if __name__ == "__main__":
    main()
