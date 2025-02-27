def check_numeric(prompt):
    valid_input =False
    while not valid_input:
        user_input = input(f"Enter your {prompt}:")
        if user_input.isnumeric():
            valid_input = True
        else:
            print("You must enter a number")
    return int(user_input)

bmi = check_numeric("weight in kg")/(check_numeric("height in cm")/100)**2
print(f"your BMI IS {bmi}")