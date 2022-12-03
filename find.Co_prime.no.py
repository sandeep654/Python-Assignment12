#Write a python script to check whether a given pair of numbers are co-Prime
#numbers or not.
x,y=int(input("Enter first number")),int(input("Enter Second number"))
for e in range(2,x):
   if x%e==0 and y%e==0:
    print(x,"and",y,"are not co-prime numbers")
    break
else: 
    print(x,"and",y, "are co-prime numbers")