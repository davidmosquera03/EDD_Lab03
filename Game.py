from Player import Player
from Board import Board
from Nodo import Ferrocarril,Servicio
from random import randint

class Game:
    def __init__(self,board:Board) -> None:
        """
        Constructor de Juego
        que opera como banquero o administrador

        + players: dict con jugadores
        + tablero: lista doblemente enlazada circular 
        con posiciones
        """
        self.players = {}
        self.board = board

    def start(self):
        """
        Ubica a todos los jugadores en Salida
        """
        a = self.board.PTR
        for p in self.players.values():
            p.pos = a

    def transfer(self, origin: str, target: str, amount:int):
        """
        Transfiere dinero entre jugadores

        + origin: retira el dinero
        + target: recibe el dinero
        + amount: cantidad de dinero 
        """
        self.players[origin].withdraw(amount)
        self.players[target].deposit(amount)  

    def add_player(self,name):
        """
        Añade un jugador al juego
        """
        P = Player(name)
        self.players.update({name:P})
        
    def remove_player(self,name:str):
        """
        Eliminar un jugador del juego
        """
        del self.players[name]
        print(name," ha sido eliminado")

    def imprison(self,player:Player):
        """
        Ubica a un jugador en la cárcel
        """
        print(player.name," ha sido enviado a la cárcel!")
        player.on_jail = True
        while player.pos.loc !=30:
            player.pos = player.pos.next

    def pagar_servicio(self,player:Player,target):
        """
        Asigna valor a pagar a player por caer
        en servicio con dueño
        """
        cantidad:Player = len(self.players[target].inventory["servicios"])
        amount,again = player.throw_die()
        if cantidad == 1:
            total = amount * 4
            print("debe pagar (*4) ",total)
            self.transfer(player.name,target,total)
        else:
            total = amount * 10
            print("debe pagar (*10) ",total)
            self.transfer(player.name,target,amount*10)

    def pagar_ferrocarril(self,player:Player,target):
        """
        Asigna valor a pagar a player por caer
        en ferrocarril con dueño
        """
        cantidad:Player = len(self.players[target].inventory["ferrocarriles"])
        guia = {1:25,2:50,3:100,4:200}
        total = guia[cantidad]
        print("Debe pagar ",total)
        self.transfer(player.name,target,total)

    def sacar_carta(self,file):
        """
        Obtiene información de carta Cofre o Suerte

        + file: path del archivo con cartas

        + data[1]: titulo
        + data[2]: tipo de carta
        + data[3]: argumento (depende de tipo)
        """
        select = randint(1,10)
        with open(file,"r") as f:
            for i in range(select):
                x = f.readline()
            data = x.split(",")
        print("titulo es ",data[1])
        if file == "cofre.txt" or (file=="suerte.txt" and int(data[2])==0 or int(data[2])==1  ):
            return int(data[2]),int(data[3])
        else:
            return int(data[2]),None
            
    def jugar_cofre(self,tipo, cant, player:Player):
        """
        Realiza acciones dependiendo del tipo
        de carta de cofre
        """
        if tipo ==1:
            player.deposit(cant)
        elif tipo ==2:
            player.withdraw(cant)
        elif tipo == 3:
            pass
        elif tipo == 4:
            self.all_pay_one(cant,player)

    def jugar_suerte(self,player:Player,tipo,goal=None):
        print("Tipo ",tipo,"Goal ",goal)
        if tipo == 0: # A sitio especifico
            while player.pos.loc != goal:
                player.pos = player.pos.next

        elif tipo ==1:   # x pasos
            if goal<0:  # hacia atrás
                for i in range(goal):
                    player.pos = player.pos.prev
            else:   # hacia adelante
                for i in range(goal):
                    player.pos = player.pos.next

        elif tipo ==2: # A carcel
            self.imprison(player)

        elif tipo == 3:
            player.inventory["pases"] += 1 # Pase carcel

        elif tipo == 4:
            # Hasta ferrocarril
            while not isinstance(player.pos,Ferrocarril): 
                player.pos = player.pos.next

        elif tipo == 5: # hasta servicio
            while not isinstance(player.pos,Servicio): 
                player.pos = player.pos.next


    def all_pay_one(self,amount,receiver:Player):
        """
        Para Cofre
        Todos los jugadores le pagan a uno
        """
        for player in self.players.values():
            player:Player
            if player!=receiver:
                self.transfer(player.name,receiver.name,amount)

    def one_pays_all(self,amount, payer: Player):
        """
        Para Cofre
        un jugador le paga a todos
        """
        for player in self.players.values():
            if player !=payer:
                self.transfer(payer.name,player.name,amount)