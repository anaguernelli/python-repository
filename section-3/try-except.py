'''
try -> try to execute the code
except -> error trying to execute the code

As soon as it get an error, it will 'jump' to except

'''

num_str = input('Digite um numero: ')

try:
    num_float = float(num_str)
    print(f'Float: {num_float}')
    print(f'The double of {num_str} is {num_float * 2:.2f}')

# do not use bare 'except'!!
# If you don't have a specific exception you're expecting,
# at least use Exception, which is the base type for all
# "Regular" exceptions.

except Exception:
    print('It is not a number.')

# or

except Exception as error:
    # so you can see what type of error
    print(error)
