def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def float_input(msg):
    try:
        return float(input(msg))
    except ValueError:
        print("That's not a valid number.")
        return float_input(msg)


def operator_input():
    try:
        operator = input("Enter operator (+, -, *, /): ")

        if operator in {"+", "-", "*", "/"}:
            return operator
        else:
            raise ValueError("Invalid operator.")
    except ValueError:
        print("Invalid operator. Please enter valid operator.")
        return operator_input()


def main():
    print("Simple Calculator")
    print("------------------")

    num1_default = None

    while True:
        num1 = num1_default or float_input("Enter first number: ")
        if num1_default is not None:
            print(f"Enter first number: {num1}")

        operator = operator_input()
        num2 = float_input("Enter second number: ")

        while num2 == 0 and operator == "/":
            print("Error: Cannot divide by zero.")
            num2 = float_input("Enter second number: ")

        if operator == "+":
            result = sum(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)

        print(f"Result: {num1} {operator} {num2} = {result}")

        print("\n")
        again = input("Calculate again? (y/n): ")
        print("\n")
        if again != "y":
            print("Goodbye!!!")
            break

        default_num1 = input(f"Use result ({result}) as first number? (y/n): ")
        if default_num1 == "y":
            num1_default = result
        else:
            num1_default = None


if __name__ == "__main__":
    main()
