valid_input = False
while not valid_input:
    height = input("Enter yout height in cm: ")
    if height.isnumeric():
        valid_input = True
    else:
        print("You must enter a number")

valid_input = False
while not valid_input:
    weight = input("Enter your weight in Kg: ")
    if weight. isnumeric():
        valid_input =True
    else:
        print("You must enter a number")

bmi = int(weight)/(int(height)/100)**2
print(f"Your BMI is {bmi}")