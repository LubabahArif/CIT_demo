#question
l=int(input("enter the triangle lenght:"))
m=int(input("enter the triangle lenght:"))
n=int(input("enter the triangle lenght:"))
if l==m==n:
    print("equilateral triangle")
elif l==m or m==n or n==l:
    print("isosceles triangle")
else:
    print("scalene triangle")