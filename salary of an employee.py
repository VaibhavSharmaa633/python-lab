'''write a program to generaye sallery of an employee when the conditions are-
1. if the basic sallary is less than 10000 then HRA(house rent anounce) will be 80% of basic sallary and DA(daily anounce) will be 90% of basic sallery.
2. if the basic sallery  is greater then 10000 and less then 20000 then HRA is 85% of basic sallery and DA will be 90% of his basic sallery.
3. if basic sallery > 20000 then DSA will be 95% and DA will be 95%.
then calculate sallery of an employee.'''

salary=int(input("Enter the salary\n"))
total_salary=0
if(salary<10000):
                total_salary=salary+salary*0.85+salary*0.90
                print("salary of an emloyee:",total_salary)
elif(salary>10000 and salary<20000):
                total_salary=salary+salary*0.85+salary*0.90
                print("salary of an emloyee:",total_salary)
else:
                total_salary=salary+salary*0.95+salary*0.95
                
                print("salary of an emloyee:",total_salary)        
