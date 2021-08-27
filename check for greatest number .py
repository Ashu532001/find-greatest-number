#check for greatest number
def greatest(x, y, z):
    if x>y and y>z:
        return x
    elif y>z and z>x:
        return y
    else:
        return z

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter 3rd number: "))
print("greatest number is: ", greatest(a, b, c))
