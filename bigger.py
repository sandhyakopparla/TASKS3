num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))
if (num1>num2) and (num1>num3):
    largest=num1
elif (num2>num3) and(num2>num1):
    largest=num2
else:
    largest=num3
print("largest number is:",largest)


