from art import logo

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  next_calculation = "y"
  
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  
  while next_calculation == "y":
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
  
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    next_calculation = input(f"Type 'y' to continue calculating with {answer}, " 
       "or type 'new' to start a new calculation or type 'n' to exit.: ")  
    if next_calculation == "y":
      num1 = answer
    elif next_calculation == "new":
      calculator()
    else:
      next_calculation = input(f"Type 'y' to continue calculating with {answer}, " 
                         "or type 'new' to start a new calculation or type 'n' to exit.: ")
      next_calculation = "n"
      print("Goodbye")

calculator()