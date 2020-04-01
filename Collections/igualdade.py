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

conta1 = ContaSalario(37)
print(conta1)
conta2 = ContaSalario(37)
print(conta2)

print(conta1 == conta2)
conta2.deposita(100)
print(conta1 == conta2)