from Nodo import Nodo
from random import randint

class Player:
    def __init__(self,name) -> None:
        """
        Constructor de clase Player

        name: nombre del jugador
        balance: dinero disponible
        inventory: registro de cartas que posee
        double_count: veces que ha sacado par seguidas
        pos: Casilla en que se encuentra
        on_jail: está o no encarcelado
        """
        self.name = name
        self.balance = 100
        self.inventory ={"propiedades":[],
                        "servicios":[],
                        "ferrocarriles":[],
                        "pases":0}
        self.double_count = 0
        self.pos:Nodo = None
        self.on_jail = False

    def withdraw(self,amount: int):
        """
        Retira dinero del jugador
        """
        
        self.balance = self.balance-amount
        print(self.name," tiene ",self.balance)

    def deposit(self,amount:int):
        """
        Agrega dinero al jugador
        """
        self.balance+=amount
        print(self.name," tiene ",self.balance)
    
    def buy(self, property:Nodo):
        """
        Adquiere una propiedad sin dueño

        property: Propiedad a adquirir
        """
        self.inventory["propiedades"].append(property.name)
        self.withdraw(property.costo) 
        print("new balance: ",self.balance)
        property.owner = self.name
        print(self.inventory["propiedades"])
    
    def sell(self,property:Nodo):
        """
        Vende una propiedad
        La retira del inventario
        """
        self.inventory["propiedades"].remove(property.name)
        self.deposit(property.costo)
        print(self.inventory["propiedades"])



