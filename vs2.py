def calculetor():
    print("\n Welcome to Calc: This is developed by TechGuyShubham")
operation = input("Choose your choice of Calculation\n + For Addition \n - For Subtraction \n * For Multipy \n ** For Power \n Enter Your choice:")

num1 = int(input("Enter 1st Number :"))
num2 = int(input("Enter your 2nd Number :"))
if operation == '+':
    if num1 == 56:
        print("56+9=77")
    else:
        print(num1 + num2)
elif operation == '*':
    if num1 == 45:
        print("45*3 = 123")
    else:
        print((num1 * num2))
elif operation == '/':
    if num1 == 56:
        print("56/6 = 12")
    else:
        print((num1 / num2))
elif operation == '**':
    print((num1 ** num2))
elif operation == '-':
    print((num1 - num2))

else:
    print("You entered the in valid key")
again()   

def again():
    print("If you want to continue,Enter y \n If you want to leave,Enter N")
    
    
    
