# Calculator CLI

A **Command Line Interface (CLI) Calculator** written in Python. This application provides a simple and interactive way to perform basic arithmetic operations using standard input and output.

---

## ✅ Features

* **Summation** of multiple numbers
* **Subtraction** of two numbers
* **Multiplication** of two numbers
* **Division** with zero-division handling
* **Expression Evaluation** using Python's `eval()` function
* **Robust input handling** using `try-except`

---

## 🧾 How to Run

```bash
python -u CalculatorCLIApp.py
```

---

## 📋 Menu Options

When you run the application, you’ll see the following menu:

```
          ***** Welcome to Calculator Command Line Interface *****

Select the option below:
1. Summation (+)
2. Subtract (-)
3. Multiply (*)
4. Division (/)
5. Expression (+, -, *, /)
6. Exit
```

---

## 🧠 Internals

The application is built using a `Calculator` class that includes the following methods:

* `sum()` – Takes multiple inputs and returns their total.
* `sub()` – Takes two inputs and subtracts the second from the first.
* `multiply()` – Multiplies two inputs.
* `division()` – Divides first input by the second, handles division by zero.
* `expression()` – Evaluates user-inputted mathematical expression.

Each method includes proper exception handling to ensure graceful failure and user-friendly error messages.

---

## 🚀 Improvements

This version includes:

* ✅ Input validation (`try-except` blocks)
* ✅ Clean output formatting using f-strings
* ✅ Safe expression evaluation

---

## 🗂️ File Structure

```
CalculatorCLIApp.py       # Main Python file with the calculator implementation
README.md                 # Project overview and usage guide
```

---

## 📌 Notes

* Make sure Python 3 is installed.
* Use a terminal or command prompt to run the file.
* For expression evaluation, only enter safe arithmetic expressions (e.g., `3 + 5 * 2`).

---

## 📬 Contribution

Want to contribute improvements or new features? Feel free to fork the project, make changes, and submit a pull request!

---

**Happy Calculating!** 💻📈