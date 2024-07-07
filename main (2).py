def add(n1,n2):
  return n1+n2

def substract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

symbolls= {"+":add,"-":substract,"*":multiply,"/":divide}
num1=int(input("What is the first number? "))

for symboll in symbolls:
  print(symboll)
operator_symboll=input("Pick a operator from above: ")
num2=int(input("What is the first number? "))
calculation_function=symbolls[operator_symboll]
answer=calculation_function(num1,num2)
  
print(f"{num1}{operator_symboll}{num2}={answer}")