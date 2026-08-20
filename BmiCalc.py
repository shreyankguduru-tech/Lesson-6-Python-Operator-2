

height = int (input ("How tall or you in cm?"))
weight = int(input("how much do you weigh in kg?"))

bmi = weight / (height/100)**2

if bmi <= 18.4:
    print ("You are underweight")
elif bmi <= 24.9:
    print ("you are healthy")
elif bmi <= 29.9:
    print ("You are overweight")
elif bmi <= 34.9:
    print ("You are severly overweight")
elif bmi <= 39.9:
    print ("You are obese")
else:
    print ("you are severly obese")