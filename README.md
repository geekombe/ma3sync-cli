
# MA3SYNC -  Bus Management System

The Bus Management System is a simple command-line application built with Python and SQLAlchemy, designed to manage buses and their passengers. This system allows;
- Administrators to add buses, add passengers to buses, and list all passengers on buses.
- Users to Create accounts and book a bus.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11 or higher
- pip
- pipenv

### Installation

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/geekombe/ma3sync-cli.git
   cd ma3sync-cli
   ```

2. **Set Up a Virtual Environment**

   Use pipenv to create a virtual environment and activate it:

   ```bash
   pip install pipenv  # Skip if pipenv is already installed
   pipenv --python 3.11.8
   pipenv shell
   ```

3. **Install Dependencies**

   Install the required Python packages specified in `Pipfile`:

   ```bash
   pipenv install
   ```

### Running the Application

To start the application, run:

```bash
pipenv run python -m bus_management_system.main
```
- Admin User Name: admin
- Admin Password: 1234


This will launch the command-line interface (CLI) of the ma3sync-cli. Follow the on-screen prompts to explore its features.

### Features

- **Add a Bus**: Administrators can add new buses to the system, specifying the bus capacity.
- **Add a Passenger**: Passengers can be added to specific buses, provided there is available capacity.
- **List Passengers**: List all passengers currently registered on any bus within the system.
- **User Registration**: New users can register and Login to Book buses.


## .gitignore

The project's `.gitignore` file is configured to exclude SQLite database files (`*.db`) from the repository to so once you run the program, a new database will be created.

## Authors

- **Victor Njogu** - [geekombe](https://github.com/geekombe)


## License
@2024 Victor Njogu (geekombe) - Copyright
---

<c>@geekombe</c>

# contact Information:
- Phone - 254700919007
- eMail - victorgekombe@gmail.com
