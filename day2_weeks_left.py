""" f string
this program will check how many weeks are left if you live upto 90 years of age
input age 
this program just trying to familiarize with f string"""
age = input()
years_left = 90 - int(age)
week_left = years_left * 52
print(f"You have {week_left} weeks left.")
