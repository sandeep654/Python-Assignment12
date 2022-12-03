#Write a python script to print first N terms of a Fibonacci series
Term=int(input("Enter nth term: "))
x,y,z=0,1,0
while Term!=0:
    print(x)
    z=y
    y=x
    x=y+z
    Term-=1