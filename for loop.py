num = int(input("enter a positive integer:"))
fact = 1
for i in range(1,num+1):
    fact*= i
    print("factorial:", fact)