# Interactive Calculator Command-Line Application

A simple command-line calculator implemented in Python. The application supports basic arithmetic operations and includes automated tests using `pytest`.

## Features

* Interactive REPL calculator
* Supported operations:
  * add
  * subtract
  * multiply
  * divide
  * power
* Input validation and error handling
* Unit tests and parameterized tests for the calculator and operations

## Project Structure

```
app/
├── __init__.py
├── calculation/
    └── __init__.py
├── calculator/
    └── __init__.py
├── operations/
    └── __init__.py
tests/
├── __init__.py
├── test_calculation.py
├── test_calculator.py
└── test_operations.py
```

## Requirements

* `Git`
* `Python 3.10` or newer
* `pytest`

## Setup

Clone the repository:

```bash
git clone https://github.com/thejps92/is601-module3-assignment.git
cd is601-module3-assignment
```

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> [!NOTE]
> The previous commands are for **Windows PowerShell.** On macOS or Linux, the commands to activate the virtual environment may differ.

## Running the Calculator

Run the application using:

```bash
python main.py
```

You will be prompted to enter an operation and two numbers:

```
add 2 3
```

Type `exit` to exit the calculator.

## Running Tests

Run all tests with:

```bash
pytest
```