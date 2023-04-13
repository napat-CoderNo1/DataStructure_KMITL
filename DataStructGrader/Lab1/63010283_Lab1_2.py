print("Enter your High and Weight : ", end='')
High, Weight = input().split()
High = float(High)
Weight = float(Weight)
BMI = Weight/(High**2)

if BMI >= 30 :
    print("Fat")
elif BMI < 30 and BMI >= 25 :
    print("Getting Fat")
elif BMI < 25 and BMI >= 23 :
    print("More than Normal Weight")
elif BMI < 23 and BMI >= 18.5 :
    print("Normal Weight")
elif BMI < 18.5 :
    print("Less Weight")
