##################################################
'''
Q1: 
'''

weight = int(input("Weight: "))
height = int(input("Height: "))

BMI = weight / (height * height)

if  BMI < 18.5 :
    print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5 <= BMI < 25 :
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI < 30 :
    print(f"Your BMI is {BMI}, you are overweight.")
elif 30 <= BMI < 35 :
    print(f"Your BMI is {BMI}, you are in obesity class I.")
elif 35 <= BMI < 40 :
    print(f"Your BMI is {BMI}, you are in obesity class II.")
else:
    print(f"Your BMI is {BMI}, you are in obesity class III.")


##################################################
'''
Q2:
'''

size = input("Size (S, M, L):").upper()
pepperoni = input("Add pepperoni (Y/N):").upper()
extra_cheese = input("Extra cheese (Y/N):").upper()

if size ==  "S":
    bill = 45
    if pepperoni == "Y":
        bill += 5
elif size == "M":
    bill = 50
    if pepperoni == "Y":
        bill += 5
else:
    bill = 55
    if pepperoni == "Y":
        bill += 8

if extra_cheese == "Y":
    bill += 3

print(f"Your final bill is {bill}.")

##################################################
