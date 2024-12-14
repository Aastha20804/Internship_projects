#Create a basic calculator that can perform basic arithmetic operations
print("1 - Addition")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("What you want to do?: "))

if(option in [1,2,3,4]):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
if(option == 1):
        result = num1 + num2
elif(option == 2):
        result = num1 - num2
elif(option == 3):
        result = num1 * num2
elif(option == 4):
        result = num1 // num2
else:
    print("Invalid operation entered")

print("The result of the calculation is {}".format(result))