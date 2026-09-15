

# num = int(input("Enter number: "))
# if(num%2==0):
#     print("Positive")
# else:
#     print("Negative")

# num = int(input("Enter number: "))
# if(num%7==0):
#     print("Multiple of 7")
# else:
#     print("Not")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if(num1>num2 & num1>num3):
    print("num1 is greater")
elif(num2>num3 & num2>num1):
    print("num2 is greater")
else:
    print("num2 is greater")