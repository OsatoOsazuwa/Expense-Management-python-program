# Expense Management System

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Cloning the Repository](#cloning-the-repository)
- [Running the Code](#running-the-code)
  - [Prerequisites](#prerequisites)
  - [Running Tests](#running-tests)
  - [Example Usage](#example-usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Project Description

The **Expense Management System** is a lightweight yet powerful tool designed to help users efficiently track and manage their financial expenses. Whether for personal budgeting, business accounting, or financial record-keeping, this system provides a structured way to handle expenses with ease.

The system consists of two primary components:

1. **Expense Class**: This class represents an individual financial transaction with key attributes, including:
   - A unique identifier (UUID) for each expense.
   - A title describing the expense.
   - The amount spent.
   - The creation and last update timestamps (in UTC format).
   
   Additionally, the Expense class allows for updates to existing expenses while ensuring the timestamp reflects the most recent modification.

2. **ExpenseDB Class**: This class functions as a database to store and manage multiple expenses. It provides methods to:
   - Add new expenses.
   - Remove existing expenses.
   - Retrieve expenses by unique ID or title.
   - Convert all stored expenses into a structured dictionary format for easy data processing.

## Features

- **Expense Creation:** Generate new expenses with a unique ID, title, and amount.
- **Expense Modification:** Update existing expenses with a new title or amount, ensuring timestamps are adjusted accordingly.
- **Expense Lookup:** Retrieve expenses based on unique IDs or search by title.
- **Expense Removal:** Delete unwanted expenses from the system efficiently.
- **Data Representation:** Convert expenses into dictionary format for easy integration with other financial tools or applications.
- **User-Friendly Design:** The system is simple to use, making it ideal for both personal finance management and business expense tracking.

## Cloning the Repository

To clone this project, make sure you have **Git** installed. Run the following command in your terminal:

```sh
git clone https://github.com/OsatoOsazuwa/Expense-Management-python-program.git
```

## Running the Code

### Prerequisites

Ensure you have **Python 3.7+** installed on your system. You can check your Python version using:

```sh
python --version
```
### Running Tests
This project uses `pytest` for testing. To run the tests, install the required dependencies:

```sh
pip install -r requirements.txt
```

Then, execute the following command:

```sh
pytest test_expenses_mgt_program.py
```

This will run all test cases and provide results on the functionality of the Expense Management Program.

### Example Usage

You can create and manage expenses using the following sample code:

```python
from expense_db import Expense, ExpenseDB

db = ExpenseDB()
expense = Expense("Groceries", 50.0)
db.add_expense(expense)
print(db.to_dict())  # Displays all stored expenses
```

## Contributing

If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## Contact

For any issues or suggestions, feel free to open an issue on GitHub.

