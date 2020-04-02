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

from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

#cpf = Cpf("00562952004")
#print(cpf)

cnpj_exemplo = "35379838000112"
cpf_exemplo = "00562952004"

documento = CpfCnpj(cnpj_exemplo, "cnpj")
print(documento)
documento2 = CpfCnpj(cpf_exemplo, "cpf")
print(documento2)