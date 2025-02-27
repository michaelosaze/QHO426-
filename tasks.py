import random
def get_guess():
    valid_input = False
    while not valid_input:
        user_input = input("Guess a number between 1 and 100:")
        if user_input.isnumeric():
            user_number = int(user_input)
            if user_number > 1 or user_number <= 100:
                print("a number between 1 and 100")
            else:
                valid_input = True
        else:
            print("you must enter a number between 1 and 100")
    return (user_number)
rnd = random.randrange(1, 100)
guess = get_guess()
num_guesses = 1
while guess != rnd:
    if guess == rnd:
        print("Your guess was too low")
    else:
        print("your guess was too high")
    num_guesses += 1
    guess = get_guess()
print("you guessed the number correctly after (num_guesses) attempts")


