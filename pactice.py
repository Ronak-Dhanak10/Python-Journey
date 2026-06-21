# Practice Problem: Write a Python function that accepts two integer numbers.
# If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
def sum_of(a,b):
   prd = a*b
  
   if prd<= 1000:
      return(prd)
   else:
      return a+b
result =sum_of(5,60)
print(result)
      