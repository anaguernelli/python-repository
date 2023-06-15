phrase = 'This is too good to be true'

i = 0
qty_letter = 0
letter_appear_more_times = ''

while i < len(phrase):
    actual_letter = phrase[i]

    if actual_letter == ' ':
        i += 1
        continue

    # How much times the actual letter appeared
    actual_qty = phrase.count(actual_letter)

    # We want to know what letter appeared more times
    if qty_letter <= actual_qty:
        qty_letter = actual_qty
        # Like if it's counting the letter 'a',
        # letter_appear_more_times will be equal 'a'
        letter_appear_more_times = actual_letter

    i += 1

print(f'The letter more appeared is "{letter_appear_more_times}" '
      f'and it appears {qty_letter} times')
