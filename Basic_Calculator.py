#my project (01)

a = int(input("Enter 1st number: "))
x = input("Enter the operator: ")
b = int(input("Enter 2nd number: "))

if x == "+":
    print(a+b)
    
elif x == "-":
    print(a-b)   
    
elif x == "*":
    print(a*b)    
    
elif x == "/":
    print(a/b)
else:
    print("Invalid")

