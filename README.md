# Python Inventory Management System

## Project Overview

The Inventory Management System is a console-based Python application designed to manage products and track inventory efficiently.

It allows users to add, view, search, update, and delete products. Users can also sell products, restock inventory, monitor low-stock items, and calculate total inventory value.

This project uses Python dictionaries, functions, loops, conditional statements, and JSON file handling.

## Features

- Add Multiple Products
- View All Products
- Search Products by ID
- Update Product Information
- Delete Products
- Sell Products
- Restock Products
- Low Stock Alert
- Calculate Total Inventory Value
- Display Inventory Statistics
- Automatically Save Inventory Data
- Load Previous Data When Program Starts

## Technologies Used

- Python
- JSON
- OS Module
- File Handling
- Dictionaries
- Functions
- Loops
- Conditional Statements

## Project Structure

```text
Python-Inventory-Management-System/
│
├── main.py
└── products.json
```

## How to Run

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run the following command:

```bash
python main.py
```

5. Select an option from the menu.

## Data Storage

This project uses JSON file handling to store inventory data permanently.

- `json.dump()` saves product data.
- `json.load()` loads previously saved data.
- `os.path.exists()` checks whether the data file exists.

The inventory remains available even after closing and restarting the program.

## Learning Objectives

Through this project, I practiced:

- Python Dictionaries and Nested Dictionaries
- Functions and Modular Programming
- For and While Loops
- If-Else Conditions
- Dictionary Operations
- JSON File Handling
- Reading and Writing Files
- Building a Menu-Driven Application

## Author

**Abubakar Sadique**

BS Artificial Intelligence Student

## Project Status

Completed – Basic Python Project with JSON File Handling.