""" DAY 2
TIP CALCULATOR PROJECT
this program will calculate the tip we should give 
input - 1. Total bill
        2. how much tip would you like to give
        3. how many people to split the bill
"""
print("WELCOME TO THE TIP CALCULATOR")
total_bill = float(input("What is your total bill?"))
tip = float(input("How much tip would you like to give? 10, 12 or 15 ?"))
people = int(input('How many people to split the bill?'))
total_tip = (total_bill * tip) / 100
PerPerson = round(((total_bill + total_tip) / people),2)
print(f"total payment per person is {PerPerson}")
                   
