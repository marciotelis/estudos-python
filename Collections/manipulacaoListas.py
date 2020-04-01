# idades = [20, 39, 18]
# print(idades)
# idades.append(20)       #Adiciona ao final da lista
# print(idades)
# idades.remove(20)       #remove o primeiro numero 20
# print(idades)
# idades.append([27, 19]) #adiciona uma lista dentro da lista, e não os valores separadamente cada um em um índice
# print(idades)
# idades.clear()          #limpa a lista
# print(idades)
# idades = [20, 39, 18]
# print(idades)
# idades.extend([27, 19]) #assim adiciona cada elemento do iterável (lista) em cada índice da lista separadamente
# print(idades)

# # ESTE CÓDIGO PODE SER ESCRITO DE FORMA MAIS SIMPLES E DIRETA CONFORME ABAIXO DELE
# idades_no_ano_que_vem = []
# for idade in idades:
#     idades_no_ano_que_vem.append(idade+1)
# print(idades_no_ano_que_vem)
# # FORMA MAIS SIMPLES E DIRETA
# idades_no_ano_que_vem2 = [(idade + 1) for idade in idades]
# print(idades_no_ano_que_vem2)

# print()
# print([(idade) for idade in idades if idade > 21])  #print de todas as idades da lista idades que são maiores de 21


# #-------------empacotando lista de tuplas e desempacotando-----------------------
# lista = [
#     ("Guilherme", 37, 1981),
#     ("Daniela", 31, 1987),
#     ("Paulo", 39, 1979)
# ]

# for nome, idade, nascimento in lista:   # percorre por todo mas utiliza apenas o primeiro (desempacotando)
#     print(nome)

# for nome, _, _, in lista:               #só percorre pelo primeiro de cada tupla, não gastando tempo percorrendo o restante
#     print(nome)

#-----------------------ordenação------------------------------
'''
O método sorted não modifica o valor no local, o valor original, retornando uma lista. Assim podemos usar o valor original em outras classes e métodos sem modificá-lo
também podemos utilizar o key e acessar um método para dizer que por aí será ordenado. Ou ainda utilizanodo o attrgetter buscar um atributo
'''
from functools import total_ordering

@total_ordering     #da a possibilidade de verificar o __eq__  o __lt__ em uma comparação
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"

    def __eq__(self, outro):    #define qual é o parametro de igualdade, quando fizer uma comparação entre uma instancia desta classe e outra. Se não compara o espaço de memória da instanciação
        if type(outro) != ContaSalario:
            return False
        else:
            return (self._codigo == outro._codigo and self._saldo == outro._saldo)
            
    def __lt__(self, outro):        #lower than
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        else:
            return self._codigo < outro._codigo
    

from operator import attrgetter

conta16 = ContaSalario(16)
conta16.deposita(100)
#print(conta16)

conta17 = ContaSalario(17)
conta17.deposita(1500)
#print(conta17)

conta18 = ContaSalario(18)
conta18.deposita(100)
#print(conta17)

contas = [conta16, conta17, conta18]

# for conta in sorted(contas, key=attrgetter("_saldo")):
#     print(conta)

# print(conta16 < conta17)    # ta implementado no __lt__
# print(conta16 > conta17)    # não precisa implementar o __gt__ porque ja entende que é o contrario de __lt__

# for conta in sorted(contas):    # Agora podemos ordenar sem ter que utilizar um atributo "privado" fora da classe (por causa que tem o lt)
#     print(conta)

# for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):       #ordenando com camadas de prioridade (criterio de desempate)
#     print(conta)

#modificando o __lt__ podemos fazer também essa ordem
for conta in sorted(contas):   
    print(conta)

print(conta16 < conta18)
print(conta16 > conta18)
print(conta16 == conta18)
print(conta16 <= conta18)
