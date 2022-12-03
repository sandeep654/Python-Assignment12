#Write a python script to check whether a given number is Prime or not.
num=int(input("Enter a number"))
flag=True
for e in range(2,num):
    if num%e==0:
        flag=False
if flag==True:
    print("it is prime number")
else:
    print("it is not prime number")
    