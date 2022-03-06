"""input electricity units by user"""
'''(1)- For 1st 50 units,Rupees 50 paise per unit'''
'''(2)- For next 100 units,Rupees 75 paise per unit'''
'''(3)- For next 100 units,Rupees 1.20 rupee per unit'''
'''(1)- For above 250 units,Rupees 1.50 rupee per unit'''

unit=int(input("Enter the unit of electricity"))
total_bill=0
if(unit<=50):
    total_bill=total_bill+unit*0.5
    print(total_bill)
elif(unit>50 and unit<=150):
    total_bill=total_bill+unit*0.75
    print(total_bill)
elif(unit>150 and unit<=250):
    total_bill=total_bill+unit*1.20
    print(total_bill)
elif(unit>250):
    total_bill=total_bill+unit*1.50
    print(total_bill)
