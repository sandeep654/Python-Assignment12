# Write a python script to calculate HCF of two numbers
a,b=int(input("Enter first num: ")),int(input("Enter Second num:"))
if a>b:
    smaller=b
else:
    smaller=a
for e in range(1,smaller+1):
    if (a%e==0) and (b%e==0):
        Hcf=e
print(Hcf)