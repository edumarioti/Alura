usuarios_data_science = [23, 15, 56, 21, 18]
usuarios_machine_learning = [23, 48, 17, 56]

assitiram = usuarios_data_science.copy()
assitiram.extend(usuarios_machine_learning)
print()
print(usuarios_data_science)
print(usuarios_machine_learning)
print(assitiram)
print(set(assitiram))
print()
print('~'*50)


usuarios_data_science = {23, 15, 56, 21, 18}
usuarios_machine_learning = {23, 48, 17, 56}

assitiram = usuarios_data_science | usuarios_machine_learning # UNIÃO
assitiram_os_dois = usuarios_data_science & usuarios_machine_learning # INTERSECÇÃO
somente_data_science = usuarios_data_science - usuarios_machine_learning 
somente_machine_learning = usuarios_machine_learning - usuarios_data_science 
exclusivo = usuarios_data_science ^ usuarios_machine_learning
print()
print(f'Usuários de Data Science: {usuarios_data_science}')
print(f'Usuários de Machine Learning: {usuarios_machine_learning}')
print(f'Assistiram (união): {assitiram}')
print(f'Assistiram os dois (intersecção): {assitiram_os_dois}')
print(f'Assistiram somente Data Science:{somente_data_science}')
print(f'Assistiram somente Machine Learning:{somente_machine_learning}')
print(f'Assitiram um ou outro (Ou Exclusivo): {exclusivo}')
print()
print('~'*50)

print()
usuarios = {50, 24, 15, 43, 68, 42}
print(f'set: {usuarios} tamanho:{len(usuarios)}')
usuarios.add(59)
usuarios.add(50)
print(f'set: {usuarios} tamanho:{len(usuarios)}')
usuarios = frozenset(usuarios) #Congela
print(f'set: {usuarios} tamanho:{len(usuarios)}')
print()
print('~'*50)


print()
#retira a duplicidade das palavras do texto
meu_texto = "Bem vindo meu nome é Eduardo eu gosto de nomes e tenho meu cachorro e gosto muito de cachorro"
meu_texto_quebrado = set(meu_texto.split()) 
print(meu_texto_quebrado)
print()
print('~'*50)
