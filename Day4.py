# OPERATORS IN PYTHON 
# 1. Arithmetic operators : +,-,*,/,%,//,**
# 2. Assignment operators : =,+=,-=,*=,/=,%=,//
# 3. Comparison operators : ==,!=,>,<,>=,<=
# 4. Logical operators : and,or,not
# 5. Bitwise operators : &,|,^,~,<<,>>
# 6. Identity operators : is,is not
# 7. Membership operators : in,not in
# 8. Operator precedence : () , ** , *,/,% , +,- , <<
# 9. Operator associativity : left to right or right to left
# 10.Floor division : // , it returns the quotient of the division and discards the fractional part
# 11. Modulo operator : % , it returns the remainder of the division
# 12. Exponentiation operator : ** , it returns the result of raising the first operand to the power of the second operand
a = int(input("Enter first number: "))
b = int(input("Enter second number:"))
print("+,-,*,/,%,//,**")
operator = input("Enter the operator you want to perform: ")
print("The sum of a and b is: ",a+b)
print("The difference of a and b is: ",a-b)
print("The product of a and b is: ",a*b)
print("The quotient of a and b is: ",a/b)
print("The remainder of a and b is: ",a%b)
print("The floor division of a and b is: ",a//b)
print("The exponentiation of a and b is: ",a**b)