idades = [39, 30, 27, 18]

print(f'lista otiginal: {idades}')
idades.append(35)
print(f'lista append:   {idades}')
idades.insert(0, 20)
print(f'lista insert:   {idades}')
idades.extend([20, 25, 65])
print(f'lista extend:   {idades}')

idades_mais_um = [(idade + 1) for idade in idades]
print(f'lista mais um:  {idades_mais_um}')

idades_mais_um = [(idade + 1) for idade in idades if idade > 21]
print(f'lista condição: {idades_mais_um}')

test = ('Paulo', 15