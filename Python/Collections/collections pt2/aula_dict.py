aparicoes = dict(eduardo = 10, cachorro = 25, teste = 13, olaola = 1)
print(f'Dicionário criado:\n{aparicoes}\n')

aparicoes["novo_item"] = 55
print(f'Adicionado um novo item:\n{aparicoes}\n')
del aparicoes["olaola"]
print(f'Removido o olaola:\n{aparicoes}\n')

print(f"Get eduardo: {aparicoes.get('eduardo', 0)}")
print(f"Get cauani: {aparicoes.get('cauani', 0)}\n")

print('for in dict:')
for elemento in aparicoes:
    print(elemento)

print('\nfor in dict.keys():')
for elemento in aparicoes.keys():
    print(elemento)

print('\nfor in dict.values():')
for elemento in aparicoes.values():
    print(elemento)

print('\nfor in dict.items():')
for key, value in aparicoes.items():
    print(key, value)
print