from validate_docbr import CPF, CNPJ
from Documentos import Documento

cnpj = "10346913000118"
cpf = "01165447916"

pessoa_1 = Documento.cria_documento(cpf)
empresa_2 = Documento.cria_documento(cnpj)

print(pessoa_1)
print(empresa_2)