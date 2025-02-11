valid_input = False
while not valid_input:
    user_input = input("Enter a number: ")
    if (user_input. isnumeric()):
        valid_input = True
    else:
        print("You must enter a number")

user_input = int(user_input)*2
print(user_input)
