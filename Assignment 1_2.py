a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
if a < b + c and b < a + c and c < a + b:
    print("It is possible to draw a triangle")
else:
    print("It is not possible to draw a triangle")
