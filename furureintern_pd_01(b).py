import random
EASY_LEVEL_ATTEMPTS = 20
HARD_LEVEL_ATTEMPTS = 7

def set_difficulty(level_chosen):
    if level_chosen == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"your guess is right... The answer is {answer}.")


print("Welcome to the Number Guessing Game!")
print("Let me think of a number between 1 and 100")
answer = random.randint(1, 100)
print(answer)  # This was for testing and is generally removed
level = input("Choose level of difficuilty... Type 'easy' or 'hard': ")
attempts = set_difficulty(level)

# Define guessed_number before the loop starts
guessed_number = 0  

while guessed_number != answer: 
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))  # Use int directly for input

    attempts = check_answer(
        guess=guessed_number, answer=answer, turns=attempts
    )  # Call check_answer
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break  # Exit loop if attempts reach 0
    elif guessed_number != answer:
        print("Guess again.")