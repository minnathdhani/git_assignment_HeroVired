import math

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
           raise ValueError("Cannot divide by zero.")

        return a / b

    # TODO: Implement the following function to calculate the square root of a number.
    def square_root(self, x):
	if x < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      num3 = float(input("Enter a number to find its square root: "))	

      print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
      print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
      print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
      print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
      print(f"The square root of {num3} = {calculator.square_root(num3)}")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
