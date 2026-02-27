#simple calculator
a = int(input("enter number a : "))
b = int(input("enter number b : "))
operator = input("enter operator,( '+','*', '/', '-') ")

if(operator =='+'):
    print("result : " ,a+b)
elif(operator =='-'):
    print("result : " , a-b)
elif(operator =='*'):
    print("result : ", a*b)
elif(operator =='/'):
   if b!= 0:
    print("result : ", a/b)
   else:
    print("!!Error occurred!!, division by zero is not possible")
else:
    print("invalid operator")
