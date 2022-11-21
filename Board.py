from Nodo import Nodo
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

    def recorrer_PTR(self):
        """
        Muestra elementos desde el PTR
        """
        P = self.PTR
        while P !=self.ULT:
            print(P,end="<->")
            P = P.next
        print(P,"<->",P.next,"(PTR)")
    

