height = float(input("Please enter your height in cm: "))
weight = float(input("Please enter your weight in kg: "))
height1 = height/100 #converting height from centimeter to meter
bmi = weight/(height1**2)
print("%.2f" % bmi)

if bmi < 18.5:
    print(bmi)
    print("You are under weight")
elif bmi > 18.5 and bmi < 25:
    print(bmi)
    print("You are a Normal Weight")
elif bmi > 25 and bmi < 30:
    print(bmi)
    print("You are a over weight ")
elif bmi > 30 and bmi < 35:
    print(bmi)
    print("You are obese")
else:
    print(bmi)
    print("You are clinically Obese")