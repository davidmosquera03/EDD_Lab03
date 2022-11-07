from Player import Player
from Board import Board
from random import randint
class Game:
    def __init__(self,tablero:Board) -> None:
        """
        Constructor de Juego
        que opera como banquero o administrador

        players: dict con jugadores
        tablero: lista doblemente enlazada circular 
        con posiciones
        """
        self.players = {}
        self.tablero = tablero

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

        origin: retira el dinero
        target: recibe el dinero
        amount: cantidad de dinero 
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
        self.players[name].force_broke()
        del self.players[name]
        print(name," ha sido eliminado")

    def imprison(self,player:Player):
        """
        Ubica a un jugador en la cárcel
        """
        print(player.name," ha sido enviado a la cárcel!")
        player.on_jail = True
        while player.pos.loc !=4:
            player.pos = player.pos.next

    def sacar_carta(self,file):
        """
        Obtiene información de carta Cofre o Suerte

        file: path del archivo con cartas

        data[1]: titulo
        data[2]: tipo de carta
        data[3]: argumento (depende de tipo)
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
