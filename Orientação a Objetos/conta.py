class Conta:
    
    def __init__(self, numero, titular, saldo, limite): #Função construtora, para construir o objeto (self é a referência)
        print("construindo objeto ... {}".format(self))
        self.__numero = numero  #__transforma o atributo numero privado, para não poder acessá-lo diretamente e sim através dos métodos apenas
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("O Saldo do titular {} é {}".format(self.__titular, self.__saldo))
        
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor

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