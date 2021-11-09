idades = [49, 51, 26, 68, 61, 31, 46]

for i in range(len(idades)):
    print(f'Valor {idades[i]} na posição {i}')

print()

for valor in enumerate(idades):
    print(valor)

print()

for key, value in enumerate(idades):
    print(f'Valor {value} na posição {key}')

print()
lista_com_key = list(enumerate(idades))
print(f'Lista com os index: {lista_com_key}')
print()
print(f'Lista ao contrário: {list(reversed(idades))}')
print(f'Lista ordenada: {sorted(idades)}')
print(f'Lista ordenada ao contrário: {sorted(idades, reverse=True)}')

idades.sort()
print(f'Lista com a variavel ordenada: {idades}')
