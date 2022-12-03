#Write a python script to find next prime number of a given number
num=int(input("ENter a number: "))
def nextprime(num):
  while True:
   num=num+1
   for ele in range(2,num):
        if ele%num==0:
            break
   else:
     return num
print(nextprime(num))