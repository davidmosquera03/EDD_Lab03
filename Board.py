from Nodo import Nodo,Propiedad,Servicio
# Ideas: 
# Se puede usar el patrón de fabrica para las casillas
# en add_node2 se recibe el nodo ya instanciado, falta fabrica

class Board:
    def __init__(self) -> None:
        """
        Crea una Lista
        Doblemente Enlazada Circular

        + PTR: pointer,head,primer elemento
        + ULT: tail,cola, ultimo elemento
        """
        self.PTR = None
        self.ULT = None   

    def add_node2(self, node:Nodo):
        """
        Añade nodo ya instanciado
        """
        if self.PTR ==None:
            self.PTR = self.ULT = node
            self.PTR.next = node
        else:
            self.ULT.next = node
            node.prev = self.ULT
            self.ULT = node
            self.ULT.next = self.PTR
        self.PTR.prev = self.ULT

    def add_node(self, loc: int, name:str):
        """
        Añade una casilla básica
        """
        Q = Nodo(loc, name)
        if self.PTR ==None:
            self.PTR = Q
            self.ULT = Q
            self.PTR.next = Q
        else:
            self.ULT.next = Q
            Q.prev = self.ULT
            self.ULT = Q
            self.ULT.next = self.PTR
        self.PTR.prev = self.ULT

        
    def add_property(self,loc:int, name:str, value:int,hipoteca:int,color:str) -> None:
        """
        Añade un nodo como ULT
        """
        Q = Propiedad(loc, name, value, hipoteca,color)
        if self.PTR ==None:
            self.PTR = Q
            self.ULT = Q
            self.PTR.next = Q
        else:
            self.ULT.next = Q
            Q.prev = self.ULT
            self.ULT = Q
            self.ULT.next = self.PTR
        self.PTR.prev = self.ULT

    def recorrer_PTR(self):
        """
        Muestra elementos desde el PTR
        """
        P = self.PTR
        while P !=self.ULT:
            print(P,end="<->")
            P = P.next
        print(P,"<->",P.next,"(PTR)")
    
    


# a = Board()
# s = Nodo(0,"Salida")
# a.add_node2(s)
# a.add_property(1,"Brown",10,5,"brown")
# a.add_node(2,"Carcel")
# a.add_property(3,"Brown1",12,6,"brown")
# a.recorrer_PTR()
