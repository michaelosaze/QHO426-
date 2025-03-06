import random
def get_valid_number():
    valid_input =False

    while not valid_input:
        user_input = input("enter a number between 1 and 6: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input>6 or user_input<1:
                print("a number between 1 and 6")
            else:
                valid_input = True
        else:
            print("a number between 1 and 6")
    return (user_input)

score=0
for i in range (1,11):
    guess=get_valid_number()
    rnd=random.randrange(1,6)
    if guess == rnd:
        score =+ 1
        print(rnd,"you guessed right")
        print("your score is", score)
    else:
        print(rnd,"you guessed wrong")

print("your total score is", score)


