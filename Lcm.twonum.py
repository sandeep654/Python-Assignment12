#Write a python script to calculate LCM of two numbers
a,b=int(input("Enter first num: ")),int(input("Enter Second num:"))
for m in range(1,a *b +1):
    if m%a==0 and m%b ==0:
        print("Lcm of two numbers: ",m)
        break