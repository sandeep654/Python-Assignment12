#Write a python script to print all Prime numbers under 100.
count=0
for e in range(2,101):
    if e>1:
      for i in range(2,e):
        if (e%i)==0:
            break
      else:
         print(e)  
         count=count+1 

print("total prime number under 100 are {}" .format(count))       