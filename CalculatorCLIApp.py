class Calculator:
    def __init__(self) -> None:
        pass
    def sum(self):
        sum = 0
        count = int(input("Enter no. of Inputs: "))
        for _ in range(count):
            n = int(input("Enter: "))
            sum += n
        return sum
    def sub(self):
        n1 = int(input("Enter 1st Num: "))
        n2 = int(input("Enter 2nd Num: "))
        return n1-n2
    def multiply(self):
        n1 = int(input("Enter 1st Num: "))
        n2 = int(input("Enter 2nd Num: "))
        return n1*n2
    def division(self):
        n1 = int(input("Enter 1st Num: "))
        n2 = int(input("Enter 2nd Num: "))
        return n1/n2
    def expression(self):
        stringInput = input("Enter the Expression: ")
        return eval(stringInput)        

if __name__ == "__main__":
    print("          *****Welcome to Calculator Command Line Interface*****          ")
    obj = Calculator()
    switchCase = {
        1: obj.sum()
    }

    print("Select the option below:")
    print("1. Summation (+)")
    print("2. Substract (-)")
    print("3. Multiply (*)")
    print("4. Division (/)")
    print("5. Expression (+, -, *, /)")
    print("6. Exit")

    choice = int(input("Enter your Choice: "))