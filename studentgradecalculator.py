marks=[]
n= int(input("Enter how many subjects you have: "))
for i in range(n):
    score= float(input(f"Enter the mark for the subject {i+1}:  "))
    marks.append(score)
avg= sum(marks)/n
print("Average marks is",avg)

if avg>=90:
     print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")
elif avg>=60:
    print("Grade D")
elif avg>=50:
    print("Grade E")
else:
    print("Grade F")