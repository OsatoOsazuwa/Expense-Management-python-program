import pytest
from datetime import datetime, timezone
from Expenses_Management_Program import Expense, ExpenseDatabase

def main():
    test_expense_creation()
    test_expense_update()
    test_expense_to_dict()
    test_expense_db_add()
    test_expense_db_remove()
    test_get_expense_by_id()
    test_get_expense_by_title()
    test_expense_db_to_dict()


def test_expense_creation():
    expense = Expense("Groceries", 50.0)
    assert expense.title == "Groceries"
    assert expense.amount == 50.0
    assert isinstance(expense.id, str)
    assert isinstance(expense.amount, float)
    assert expense.created_at == expense.updated_at  # Ensuring timestamps match on creation

def test_expense_update():
    expense = Expense("Groceries", 50.0)
    expense.update(title="Supermarket", amount=75.0)
    assert expense.title == "Supermarket"
    assert expense.amount == 75.0
   # assert expense.updated_at > expense.created_at  # Ensuring update timestamp is later

def test_expense_to_dict():
    expense = Expense("Rent", 1000.0)
    expense_dict = expense.to_dict()
    assert expense_dict["title"] == "Rent"
    assert expense_dict["amount"] == 1000.0
    assert "id" in expense_dict
    assert "created_at" in expense_dict
    assert "updated_at" in expense_dict

def test_expense_db_add():
    db = ExpenseDatabase()
    expense = Expense("Transport", 20.0)
    db.add_expense(expense)
    assert len(db.expenses) == 1
    assert db.expenses[0].title == "Transport"

def test_expense_db_remove():
    db = ExpenseDatabase()
    expense = Expense("Coffee", 5.0)
    db.add_expense(expense)
    db.remove_expense(expense.id)
    assert len(db.expenses) == 0

def test_get_expense_by_id():
    db = ExpenseDatabase()
    expense = Expense("Dinner", 30.0)
    db.add_expense(expense)
    found_expense = db.get_expense_by_id(expense.id)
    assert found_expense is not None
    assert found_expense.title == "Dinner"

def test_get_expense_by_title():
    db = ExpenseDatabase()
    expense1 = Expense("Lunch", 15.0)
    expense2 = Expense("Lunch", 18.0)
    db.add_expense(expense1)
    db.add_expense(expense2)
    results = db.get_expense_by_title("Lunch")
    assert len(results) == 2

def test_expense_db_to_dict():
    db = ExpenseDatabase()
    expense = Expense("Snacks", 10.0)
    db.add_expense(expense)
    db_dict = db.to_dict()
    assert isinstance(db_dict, list)
    assert len(db_dict) == 1
    assert db_dict[0]["title"] == "Snacks"

if __name__ == "__main__":
    main()