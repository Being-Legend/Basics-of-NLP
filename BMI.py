height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
BMI = (weight/(height*height))*703
print(BMI)
if(BMI<=18.5):
    print("Underweight")
elif(BMI>18.5 or BMI<=24.9):
    print("Normal Weight")
elif(BMI>24.9 or BMI <=29.9):
    print("Ovweweight")
elif(BMI>=30):
    print("Obesity")