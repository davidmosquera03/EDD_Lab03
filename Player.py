from Nodo import Nodo,Propiedad,Servicio,Ferrocarril
from random import randint

class Inventory(dict):
    def __init__(self):
        """
        Constructor de clase de Inventorio

        inicializa con 4 claves
        + propiedades,ferrocarriles,servicios:
        almacenan Nodos de este tipo
        + pases: cartas de salir de prisión
        """
        self["propiedades"] = []
        self["ferrocarriles"] =[]
        self["servicios"] = []
        self["pases"] = 0
    @property
    def sellable(self):
        """
        Cantidad de recursos que se pueden
        vender
        """
        count = 0
        for value in self.values():
            if isinstance(value,list):
                count += len(value)
            elif isinstance(value,int):
                count += value
        return count
class Player:
    def __init__(self,name:str) -> None:
        """
        Constructor de clase Player

        + name: nombre del jugador
        + balance: dinero disponible
        + inventory: registro de cartas que posee
        + double_count: veces que ha sacado par seguidas
        + pos: Casilla en que se encuentra
        + on_jail: está o no encarcelado
        """
        self.name = name
        self.balance = 1500
        self.inventory =Inventory()
        self.double_count = 0
        self.pos:Nodo = None
        self.on_jail = False
        self.times_on_jail = 0

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

    def buy(self,sitio:Nodo):
        """
        Comprar Propiedad/Servicio/Ferrocarril
        """
        if isinstance(sitio,Propiedad):
            self.inventory["propiedades"].append(sitio)
        elif isinstance(sitio,Servicio):
            self.inventory["servicios"].append(sitio)
        elif isinstance(sitio,Ferrocarril):
            self.inventory["ferrocarriles"].append(sitio)

        self.withdraw(sitio.costo)
        sitio.owner = self.name
        print(self.inventory)

    def sell(self,key,name):
        """
        Vende Propiedad/Servicio/Ferrocarril
        """
        found = False
        for value in self.inventory[key]:
            value:Nodo
            if value.name == name:
                found = True
                self.deposit(value.costo)
                value.owner = None
                self.inventory[key].remove(value)
        if not found:
            print("No hallado")

    def sell_menu(self):
        """
        Menu iterativo para vender 
        """
        print("Vendibles ",self.inventory.sellable)
        if self.inventory.sellable !=0:
            print("1 Propiedades,2 Ferrocarriles,3 Servicios,4 Pases")
            valid =["1","2","3","4"]
            op = input()
            while op not in valid:
                print("Opcion inválida")
                op = input()
        else:
            op = 0
        if op =="1":
            if len(self.inventory["propiedades"])>0:
                print(self.inventory["propiedades"])
                print("Seleccione propiedad a vender")
                s = input()
                self.sell("propiedades",s)
            else:
                print("No tiene propiedades")

        elif op =="2":
            if len(self.inventory["ferrocarriles"])>0:
                print(self.inventory["ferrocarriles"])
                print("Seleccione ferrocarril a vender")
                s = input()
            else:
                print("No tiene ferrocarriles")

        elif op=="3":
            if len(self.inventory["servicios"])>0:
                print(self.inventory["servicios"])
                print("Seleccione servicio a vender")
                s = input()
                self.sell("servicios",s)
            else:
                print("No tiene servicios")

        elif op=="4":
            if self.inventory["pases"]>0:
                self.deposit(50)
                self.inventory["pases"] -= 1
            else:
                print("No tiene pases")
        if op==0:
            print("No tiene nada que vender")
        else:
            print(self.inventory)

    def broke(self):
        """
        El jugador vende del inventorio
        para evitar la quiebra
        """
        print("¡Está en riesgo de quiebra!")
        while self.balance<0 and self.inventory.sellable>0:
            print("¡A Vender!")
            self.sell_menu()

        if self.balance<0 and self.inventory.sellable==0:
            print("BANCARROTA!")
        else:
            print("Se ha salvado")

    def throw_die(self):
        """
        lanzamiento de dado

        + amount: suma de los dos dados
        + again: 0 si no sacó par, 1 si obtuvo
        """
        again = 0
        die1 = randint(1,6)
        die2 = randint(1,6)
        print(die1," ",die2)
        if die1==die2:
            again = 1
            self.double_count+=1
            print("Has sacado par ",self.double_count," veces")
        else:
            self.double_count=0
        amount = die1+die2
        return amount,again

    def jugar_turno(self):
        """
        tira dados
        
        + again: devuelve 1 si debe volver a jugar
        0 si no
        """
        amount,again = self.throw_die()

        for i in range(amount):
            self.pos = self.pos.next
            if self.pos.name == "salida":
                print("Ha pasado por salida y cobra 200")
                self.deposit(200)
        print(self.name," está en ",self.pos)
        return again

    def jugar_carcel(self):
        """
        turno de jugador en carcel

        -Tras tres turnos se paga multa
        -De tener pases se ofrece usarlos
        -Tira dado 3 veces esperando par
        """
        if self.times_on_jail==3:
            print("Multa de 50 para salir")
            self.withdraw(50)
            self.on_jail = False

        elif self.inventory["pases"]>0:
            print("Usar pase de salida? 1 si 2 no")
            op = input()
            if op =="1":
                self.inventory["pases"] -= 1
                self.on_jail = False
            if op =="2":
                self.times_on_jail += 1
        else:
            i =1
            while i<=3 and self.on_jail:
                print("Lanzamiento ",i)
                x,double = self.throw_die()
                if double == 1:
                    self.on_jail = False
                i+= 1
            if self.on_jail:
                self.times_on_jail += 1
            print("lleva ",self.times_on_jail," veces en la cárcel")
            self.double_count = 0
    


