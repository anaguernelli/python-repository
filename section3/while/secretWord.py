import os

secret_word = 'maluquice'
i = 0
# letters that are in secret word
right_letters = ''

while True:
    guess_letter = input('Guess a letter: ').lower()
    i += 1

    if len(guess_letter) > 1:
        print('Please, type just a letter.')
        continue

    if guess_letter in secret_word:
        right_letters += guess_letter

    if guess_letter not in secret_word:
        print('This letter is not in the secret word')

    formed_word = ''

    # will pass to each letter of the secret word
    for secret_letter in secret_word:
        if secret_letter in right_letters:
            formed_word += secret_letter
        else:
            formed_word += '*'
    print(f'Formed word: {formed_word}')

    if formed_word == secret_word:
        os.system('cls')
        print('Congratulations!!! You win!')
        print(f'The letter was "{secret_word}"')
        print(f'{i} attempts')

        i = 0
        right_letters = ''

        quit = input('Wanna quit? [y/n] ').lower().startswith('y')

        if quit is True:
            print('Turning off...')
            break
