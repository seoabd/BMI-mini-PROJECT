weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")

if bmi == 18.5 and bmi < 25:
    print("normal weight")

if bmi >= 25:
    print("overweight")