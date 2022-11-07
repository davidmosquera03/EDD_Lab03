class Nodo:
    def __init__(self,loc:int, name:str,) -> None:
        """
        Casilla básica

        loc: posición en lista
        name: nombre de la casilla
        """
        self.loc = loc
        self.name = name
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.name}"

class Propiedad(Nodo):
    def __init__(self, loc: int, name: str,costo:int,renta:int,color:str) -> None:
        super().__init__(loc, name)
        """
        Casilla que representa propiedad adquirible

        costo: precio para comprarla
        renta: cantidad que recibe el dueño cuando alguien cae
        color: grupo de color al que pertenece
        owner: nombre de Jugador que lo posee
        """
        self.costo = costo
        self.renta = renta
        self.color = color
        self.owner = None

class Servicio(Nodo):
    def __init__(self, loc: int, name: str) -> None:
        """
        Casilla que representa un servicio
        """
        super().__init__(loc, name)
        self.owner = None
          
        self.costo = 150

class Ferrocarril(Nodo):
    def __init__(self, loc: int, name: str) -> None:
        """
        Casilla que representa un ferrocarril
        """
        super().__init__(loc, name)
        self.owner = None
        self.costo = 200

class Suerte(Nodo):
    pass

class Cofre(Nodo):
    pass

class Impuesto(Nodo):
    def __init__(self, loc: int, name: str,pago:int) -> None:
        """
        Casilla que representa un impuesto que pagar
        
        pago: valor a pagar en esa casilla
        """
        super().__init__(loc, name)
        self.pago = pago
    