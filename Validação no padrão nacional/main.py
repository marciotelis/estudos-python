'''
#   Final do curso, utilizando a API viacep e manipulando json

from acesso_cep import BuscaEndereco

cep = 96090230
objeto_cep = BuscaEndereco(cep)

'''
'''
a = objeto_cep.acessa_via_cep()
print(a.json())                     # já me retorna em dicionário
print(a.json()['bairro'])           # posso buscar direto o valor de uma chave
'''
'''

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

'''

'''
#   validação de cpf e cnpj

from cpf_cnpj import Documento
from validate_docbr import CNPJ

cnpj_exemplo = "35379838000112"
cpf_exemplo = "00562952004"

documento = Documento.cria_documento(cnpj_exemplo)
print(documento)
documento2 = Documento.cria_documento(cpf_exemplo)
print(documento2)
'''

#   Validando telefones com expressões regulares

import re
from TelefonesBr import TelefonesBr

telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)

# padrao = "([0-9]{2,3})([0-9]{4,5})([0-9]{4})"
# resposta = re.findall(padrao, telefone)

print(telefone_objeto)




