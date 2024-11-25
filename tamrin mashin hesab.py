num1 = int(input("pleas enter your num1:"))
num2 = int(input("pleas enter your num2:"))
amalgar = input("+ , - , * , ** , / , %")
if (amalgar == "+"):
    result = num1 + num2
elif (amalgar == "-" ):
    result = num1 - num2
elif (amalgar == "*"):
    result = num1 * num2
elif (amalgar == "**"):
    result = num1 ** num2 
elif (amalgar == "/"):
    result = num1 / num2
elif (amalgar == "%"):
    result = num1 % num2
else:
    print("lotfan adad vared konid!")
print(result)                           