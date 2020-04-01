class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Código {self.codigo} Saldo {self.saldo}<<]"

    

conta_do_gui = ContaCorrente(15)
print(conta_do_gui)

conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(1512)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
#print(contas)   #aqui vai printar o local armazenado da memória de cada conta
for conta in contas:
    print(conta)    #já aqui se está dando print das contas separadamente, portanto chamará o método especial __str__

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

deposita_para_todas(contas)
print(contas[0], contas[1])

#---------------------TUPLA------------------------
# A tupla é imutável e é muito importante a posição
guilherme = ("guilherme", 37, 1981)
daniela = ("Daniela", 31, 1987)