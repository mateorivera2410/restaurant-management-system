# Restaurant Management System

Restaurant order management system developed in Python using Tkinter.

This project allows a restaurant to manage users, take customer orders, charge tables, view unpaid orders, view paid orders, and calculate daily profit.

## Features

* Graphical interface using Tkinter
* Login system for managers and waiters
* Account creation system
* Waiter panel to take orders
* Waiter panel to charge tables
* Manager panel to view paid orders
* Manager panel to view unpaid orders
* Daily profit calculation
* Data storage using JSON files

## Technologies Used

* Python
* Tkinter
* JSON
* File handling
* Functions
* Modular programming

## Project Structure

```txt
restaurant-management-system/
├── gui.py
├── logic.py
├── orders.json
├── paid_orders.json
├── users.json
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Run the main file:

```bash
python gui.py
```

## Default Login

Manager account:

```txt
Username: admin
Password: 1234
```

## Files Description

* `gui.py`: Main file. Contains the graphical interface.
* `logic.py`: Contains the main logic of the system.
* `orders.json`: Stores unpaid orders.
* `paid_orders.json`: Stores paid orders.
* `users.json`: Stores users.
* `README.md`: Project explanation.
* `requirements.txt`: Project dependencies.
* `.gitignore`: Files and folders that should not be uploaded to GitHub.

## What I Learned

In this project, I practiced:

* How to create a graphical interface with Tkinter
* How to organize a Python project in different files
* How to store data using JSON
* How to create a login system
* How to manage orders in a restaurant system
* How to separate interface code from logic code

## Future Improvements

* Improve the design of the interface
* Add password encryption
* Add database support
* Add better input validation
* Add sales reports
* Add product management
* Improve error handling

## Author

Mateo Rivera
Systems Engineering Student
