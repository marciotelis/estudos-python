class Conta:
    
    def __init__(self, numero, titular, saldo, limite): #Função construtora, para construir o objeto (self é a referência)
        print("construindo objeto ... {}".format(self))
        self.__numero = numero  #__transforma o atributo numero privado, para não poder acessá-lo diretamente e sim através dos métodos apenas
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
        
    def extrato(self):
        print("O Saldo do titular {} é {}".format(self.__titular, self.__saldo))
        
    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_saque

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do seu limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        print(self.__limite)
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite