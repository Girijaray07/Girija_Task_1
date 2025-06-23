class Calculator:
    def __init__(self) -> None:
        pass
    def sum(self):
        total = 0; arr = []
        count = int(input("Enter no. of Inputs: "))
        for _ in range(count):
            n = int(input("Enter: "))
            arr.append(n)
            total += n
        print(f"The Sum of {arr}  is: {total}")
    def sub(self):
        n1 = int(input("Enter 1st Num: "))
        n2 = int(input("Enter 2nd Num: "))
        print(f"The Substract of {n1} and {n2} is: {n1-n2}")
    def multiply(self):
        n1 = int(input("Enter 1st Num: "))
        n2 = int(input("Enter 2nd Num: "))
        print(f"The Multiply of {n1} and {n2} is: {n1*n2}")
    def division(self):
        n1 = int(input("Enter 1st Num: "))
        n2 = int(input("Enter 2nd Num: "))
        try:
            print(f"The Division of {n1} and {n2} is: {n1/n2}")
        except Exception as e:
            print(f"Error: {e}")
    def expression(self):
        stringInput = input("Enter the Expression: ")
        try:
            print(f"The Answer is: {eval(stringInput)}")
        except Exception as e:
            print(f"Expression as {e}")      

if __name__ == "__main__":
    print("          *****Welcome to Calculator Command Line Interface*****          ")
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
        print("2. Substract (-)")
        print("3. Multiply (*)")
        print("4. Division (/)")
        print("5. Expression (+, -, *, /)")
        print("6. Exit\n")

        choice = int(input("Enter your Choice: "))

        switchCase.get(choice, lambda: print("Invalid Choice, Try again..."))()