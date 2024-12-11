class Integrante:
    def __init__(self, name, value, email):
        self.__name = name
        self.__value = value
        self.__email = email

    def getNome(self):
        return self.__name

    def getValor(self):
        return self.__value

    def getEmail(self):
        return self.__email

    def setNome(self, name):
        self.__nome = name

    def setValor(self, value):
        self.__valor = value

    def setEmail(self, email):
        self.__email = email

    def __str__(self):
        return f"Nome: {self.__name}, Valor: R${self.__value}, Email: {self.__email}"