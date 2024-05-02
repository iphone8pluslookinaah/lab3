import math
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def bmi_range(bmi):
    if (bmi < 18.5):
        print("under weight")
        return -1
    elif (bmi > 25.0):
        print("over weight")
        return 1
    else:
        print("normal weight")
        return 0

def calc_bmi(height, weight):
    print("Height = ", height)
    print("Weight = ", weight)
    bmi = weight / pow(height, 2)
    print("bmi =", bmi)
    bmi_range(bmi)

calc_bmi(weight=57, height=1.73)