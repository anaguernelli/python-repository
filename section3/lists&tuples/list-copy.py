list_a = ['Ana', 'Oi', True, 3]

# list_b will just copy list_a til here

list_b = list_a.copy()

# so if we make a change, list_b won't get it

list_a[0] = 'Another'

print(list_a)
print(list_b)
