class Conta:
    
    def __init__(self, numero, titular, saldo, limite): #Função construtora, para construir o objeto (self é a referência)
        print("construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print("O Saldo do titular {} é {}".format(self.titular, self.saldo))
        
    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor
