'''
Closure

'''


def make_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}!'
    return greet


good_morning_greet = make_greeting('Good morning')
good_night_greet = make_greeting('Good night')

for nome in ['Ana', 'Banana', 'Pedro']:
    print(good_morning_greet(nome))
