a=int(raw_input("enter the number1"))
b=int(raw_input("enter the second number"))
c=int(raw_input("enter the third number"))
if(a>=b) and (a>=c):
  print "the largest number is ",a
elif(b>=a) and (b>=c):
  print "the largest number is",b
else:
  print "the largest number is",c
