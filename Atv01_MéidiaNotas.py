def MediaNotas():
    n1 = float(input('Digite a Primeira Nota: '))
    n2 = float(input('Digite a Segunda Nota: '))
    n3 = float(input('Digite a Terceira Nota: '))
    media = (n1 + n2 + n3)/3
    return media
print(f'Média igual: {MediaNotas()}')
