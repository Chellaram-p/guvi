num=int(input("Enter a number"))
k=0
n=num
while num!=0:
	s=num%10
	k=k*10+s
	num=num/10
if k==n:
	print("The given number is palindrome")
else:
	print("The given number is not a palindrome")
