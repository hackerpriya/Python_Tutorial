#Make a grading system
grade=int(input('Enter your marks:'))
if grade>=90:
    print('Grade A')
elif grade>=80:
    print('Grade B')
elif grade>=70:
    print('Grade C')
elif grade>=60:
    print('Grade D')
else:
    print('Fail')