class Nodo:
    def __init__(self,loc:int, name:str,) -> None:
        self.loc = loc
        self.name = name
        self.prev = None
        self.next = None

class Propiedad(Nodo):
    def __init__(self, loc: int, name: str,costo:int,renta:int,color:str) -> None:
        super().__init__(loc, name)
        self.costo = costo
        self.renta = renta
        self.color = color
        self.owner = None
        self.owned = False
    def __repr__(self) -> str:
        return f"{self.name} {self.costo}"

class Servicio(Nodo):
    def __init__(self, loc: int, name: str) -> None:
        super().__init__(loc, name)
        self.owner = None
        self.owned = False

class Ferrocarril(Nodo):
    def __init__(self, loc: int, name: str) -> None:
        super().__init__(loc, name)
        self.owner = None
        self.owned = False

class Arca(Nodo):
    def __init__(self, loc: int, name: str,goal: int) -> None:
        super().__init__(loc, name)
        self.goal = goal

class Cofre(Nodo):
    def __init__(self, loc: int, name: str,tipo:int,money:int) -> None:
        super().__init__(loc, name)
        if tipo ==0:
            self.bono = money
        else:
            self.cobro = money