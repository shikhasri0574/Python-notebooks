num1=float(input("enter num1"))
num2 = float(input("enter num2"))

operation = input("enter operation(+,-,/,*):")

if operation == '+':
    result= num1+num2
elif operation == '-':
    result = num1-num2
elif operation == '/':
    if num2!=0:
     result = num1/num2
    else:
       result= "out of bound"
elif operation == '*':
    result = num1*num2

else:
   result= "invalid"
   print("result",result)
       

