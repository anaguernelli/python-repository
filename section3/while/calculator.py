from time import sleep

while True:
    num1 = input('Type the first value: ')
    num2 = input('Type the second value: ')

    operator = input('Choose an operatorerator ( + - * / ): ')

    validNumber = None

    try:
        num1Float = float(num1)
        num2Float = float(num2)

        validNumber = True
    except Exception:
        validNumber = None

        if validNumber is None:
            print('One or both values are invalid')
            continue

        numericsOperator = '+-*/'

        if operator not in numericsOperator:
            print('Please, choose a numeric operatorerator like ( + - * / )')
            continue

        if len(operator) > 1:
            print('Type only one operator')
            continue

    print('We are calculating your account... See the result')
    sleep(1)
    if operator == '+':
        print(f'{num1} + {num2} = {num1Float + num2Float}')

    elif operator == '-':
        print(f'{num1} - {num2} =  {num1Float - num2Float}')

    elif operator == '*':
        print(f'{num1} * {num2} = {num1Float * num2Float}')

    elif operator == '/':
        print(f'{num1} / {num2} = {num1Float / num2Float}')

    quit = input('Wanna quit? [Y] ').upper().startswith('Y')

    if quit is True:
        sleep(0.5)
        print('...turning off...')
        sleep(1)
        break
