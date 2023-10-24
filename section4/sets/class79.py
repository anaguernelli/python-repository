# Exemplo usando sets

letras = set()

while True:
    letra = input('Digite uma letra: ').lower()
    letras.add(letra)
    print(letras)
    # if letra == 'a':
    if 'a' in letras:
        print('Você achou a letra secreta!')
        break

print(letras)
