#Write a python script to print all Prime numbers between two given numbers (both
#values inclusive)
num1=int(input("Enter first num: "))
num2=int(input("Enter second num: "))
count=0
for e in range(num1,num2+1):
    if e>1:
      for i in range(2,e):
        if (e%i)==0:
            break
      else:
         print(e)
         count=count+1
print("total prime number between {} & {} are {}" .format(num1,num2,count))