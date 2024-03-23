# busmanagement/main.py
from .bus_management import BusManagement
from .database import init_db

def main():
    init_db()
    bm = BusManagement()
    # Implement CLI logic for interacting with BusManagement instance
    
if __name__ == "__main__":
    main()
