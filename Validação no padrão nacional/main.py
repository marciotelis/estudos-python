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

'''
#   Validando telefones com expressões regulares

import re
from TelefonesBr import TelefonesBr

telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
'''

'''
#   FORMATAÇÃO DE DATAS

from datas_br import DatasBr

cadastro = DatasBr()
print(cadastro)
'''

from datetime import datetime, timedelta
from datas_br import DatasBr

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1, hours=20)

print(amanha - hoje)