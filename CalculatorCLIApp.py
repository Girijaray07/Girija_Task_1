class Calculator:
    def sum(self):
        total, arr = 0, []
        try:
            count = int(input("Enter number of inputs: "))
            for _ in range(count):
                n = int(input("Enter: "))
                arr.append(n)
                total += n
            return f"The Sum of {arr} is: {total}"
        except Exception as e:
            return f"Error: {e}"

    def sub(self):
        try:
            n1 = int(input("Enter 1st Num: "))
            n2 = int(input("Enter 2nd Num: "))
            return f"The Subtract of {n1} and {n2} is: {n1 - n2}"
        except Exception as e:
            return f"Error: {e}"

    def multiply(self):
        try:
            n1 = int(input("Enter 1st Num: "))
            n2 = int(input("Enter 2nd Num: "))
            return f"The Multiply of {n1} and {n2} is: {n1 * n2}"
        except Exception as e:
            return f"Error: {e}"

    def division(self):
        try:
            n1 = int(input("Enter 1st Num: "))
            n2 = int(input("Enter 2nd Num: "))
            return f"The Division of {n1} and {n2} is: {n1 / n2}"
        except Exception as e:
            return f"Error: {e}"

    def expression(self):
        try:
            stringInput = input("Enter the Expression: ")
            return f"The Answer is: {eval(stringInput)}"
        except Exception as e:
            return f"Error in expression: {e}"


if __name__ == "__main__":
    print("          ***** Welcome to Calculator Command Line Interface *****")

    obj = Calculator()
    switchCase = {
        1: obj.sum,
        2: obj.sub,
        3: obj.multiply,
        4: obj.division,
        5: obj.expression,
        6: exit
    }

    while True:
        print("\nSelect the option below:")
        print("1. Summation (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Division (/)")
        print("5. Expression (+, -, *, /)")
        print("6. Exit\n")

        try:
            choice = int(input("Enter your Choice: "))
            results = switchCase.get(choice, lambda: print("Invalid Choice, Try again..."))()
            
            if (results):
                print(f"{results}")
        except ValueError:
            print("Please enter a valid number!")