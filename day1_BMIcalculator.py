"""day 2
this program will help you to find the BMI of a person given the height and weight is known"""

height = input()

weight = input()
# height and weight could be a floating value
# bmi is taken as an integer
BMI = int(float(weight)/float(height)**2)
print(str(BMI))
