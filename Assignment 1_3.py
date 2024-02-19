name = input("enter your name: ")
family = input("enter your family: ")

a = float(input("enter your first grade: "))
b = float(input("enter your second grade: "))
c = float(input("enter your third grade: "))

average = (a + b + c) / 3

if average < 12:
    print("Fail")
if 12 <= average < 17:
    print("Normal")
if average > 17 :
    print("Great!")
