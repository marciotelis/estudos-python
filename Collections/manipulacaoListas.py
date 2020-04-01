idades = [20, 39, 18]
print(idades)
idades.append(20)       #Adiciona ao final da lista
print(idades)
idades.remove(20)       #remove o primeiro numero 20
print(idades)
idades.append([27, 19]) #adiciona uma lista dentro da lista, e não os valores separadamente cada um em um índice
print(idades)
idades.clear()          #limpa a lista
print(idades)
idades = [20, 39, 18]
print(idades)
idades.extend([27, 19]) #assim adiciona cada elemento do iterável (lista) em cada índice da lista separadamente
print(idades)

# ESTE CÓDIGO PODE SER ESCRITO DE FORMA MAIS SIMPLES E DIRETA CONFORME ABAIXO DELE
idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade+1)
print(idades_no_ano_que_vem)
# FORMA MAIS SIMPLES E DIRETA
idades_no_ano_que_vem2 = [(idade + 1) for idade in idades]
print(idades_no_ano_que_vem2)

print()
print([(idade) for idade in idades if idade > 21])  #print de todas as idades da lista idades que são maiores de 21


