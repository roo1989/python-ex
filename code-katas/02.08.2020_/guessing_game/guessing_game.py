import random

def number_guessing_game():
    # Get a range limit from an input
    limit = input('Please enter a numerical limit for the guessing game: ')
    
    if not limit.isdigit():
        raise ValueError('Invalid numerical type!')

    # Generate a number from input.
    answer = random.randint(0, int(limit))

    # Set a count variable
    count = 0

    while True:
        if count == 3:
            print('You didn\'t guess in time!')
            break
        count += 1
        guess = int(input('What is your guess? '))

        if guess == answer:
            print(f'Correct! The answer is {guess}!')
            break
        if guess < answer:
            print(f'Your guess: {guess} is too low!')
        else:
            print(f'Your guess: {guess} is too hight!')



def word_guessing_fame():
    # Create a dictionary of words.
    words = {'Obi': 'Wan', 'Luke': 'Skywalker', 'Master': 'Yoda', 'Darth': 'Vader'}

    # Choose a random word from the dictionary
    first, last = random.choice(list(words.items()))

    # While true, ask the user for an input
    while True:
        guess = input('Guess a Star Wars character, either first name or last name: ')

        if guess in [first, last]:
            print(f'Correct! The answer is {first} {last}')
            break
        else:
            print('Incorrect!')



word_guessing_fame()
# number_guessing_game()
