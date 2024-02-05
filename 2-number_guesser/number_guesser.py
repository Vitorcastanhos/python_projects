import random

number = random.randint(1, 10)
guesses = 0

while True:
    guesses += 1
    user_input = input("Pick a number between 1 and 10: ")
    number = random.randint(1, 10)
    print(number)

    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Please, type a number next time.")
        continue
    if user_input == number:
        print("You are right!")
        break
    else:
        print("Try again.")

if guesses == 1:
    print("You got it in", guesses, "guess!")
else:
    print("You got it in", guesses, "guesses!")
