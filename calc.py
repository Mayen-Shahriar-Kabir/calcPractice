def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    print("Cannot divide by zero. Try again...")
    return Calculate()
  return round(x / y, 2)

def Calculate():
  s = input()
  lst = s.split(" ")
  lst[0], lst[2] = int(lst[0]), int(lst[2])

  if lst[1] == "+":
    print(add(lst[0], lst[2]))
  elif lst[1] == "-":
    print(subtract(lst[0], lst[2]))
  elif lst[1] == "*":
    print(multiply(lst[0], lst[2]))
  elif lst[1] == "/":
    print(divide(lst[0], lst[2]))

Calculate()
