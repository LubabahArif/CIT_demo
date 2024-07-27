#question 1
name=input("enter your name:")
father_name=input ("enter your father name:")
marks=int(input("enter your marks:"))
if (marks >= 90):
    grade ="A"
elif (marks >= 70):
    grade= "B"
elif (marks >= 60):
    grade= "C" 
elif (marks >= 50) :
    grade= "D" 
else:
    grade = "f"
print("grade:", grade)    