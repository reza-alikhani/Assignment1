import math
a = float(input("Enter the first number: "))
op = input("Enter the operation: ")
b = float(input("Enter the second number: "))

if op == "+":
    result = a + b
if op == "-":
    result = a - b
if op == "*":
    result = a * b
if op == "/":
    if b == 0 :
        result = "Not a Number"
    else:
        result = a / b
if op == "sin":
    d = a * math.pi / 180
    result = math.sin(d)
if op == "cos":
    d = a * math.pi / 180
    result = math.cos(d)
if op == "tan":
    d = a * math.pi / 180
    result = math.tan(d)
if op == "cot":
    d = a * math.pi / 180
    result = 1 / math.tan(d)
if op == "sqrt":
    result = math.sqrt(a)

print("result =", result)
