#question 2
year= int(input("enter your year:"))
if (year% 4==0)and(year%100==0):
    print(year, "is a leap year ")
elif(year% 4==0)or(year%100!=0):
    print(year, "is a leap year ")
else:
    print(year, "is not a leap year ")