class Integrante:
    def __init__(self, nome, valor, email):
        self.__nome = nome
        self.__valor = valor
        self.__email = email

    def getNome(self):
        return self.__nome

    def getValor(self):
        return self.__valor

    def getEmail(self):
        return self.__email

    def setNome(self, nome):
        self.__nome = nome

    def setValor(self, valor):
        self.__valor = valor

    def setEmail(self, email):
        self.__email = email

    def __str__(self):
        return f"Nome: {self.__nome}, Valor: R${self.__valor}, Email: {self.__email}"