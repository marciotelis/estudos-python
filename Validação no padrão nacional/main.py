'''
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

from Cpf import Cpf


cpf = Cpf("00562952004")
print(cpf)