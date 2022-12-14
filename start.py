from tkinter import *
from sound import die_sound
from random import randint
from generador import sort  
from Nodo import Propiedad
i = 0
def asignar():
    """
    Recibe los nombres de los jugadores
    tiran dados y segun el orden jugarán
    """
    root = Tk()
    root.geometry("500x250+550+100")
    root.resizable(False, False)
    root.title("Monopoly X Dr. Who")

    nombres_usados = []
    turns = []
    def next():
        global i
        name = receiver.get()
        if name == "":
            label.config(text="Se necesita un nombre")
        elif name in nombres_usados:
            label.config(text="No repita nombres")
        else:
            die_sound()
            die = randint(1,12)
            label.config(text=f"{name}, ha sacado {die}")
            nombres_usados.append(name)
            turns.append([die,name])
            receiver.delete(0, END)
            i += 1
            label1.config(text=f"Jugadores {i}")
            if i==4:
                begin()

    def begin():
        global i
        if i<2:
            print(i)
            label.config(text="minimo 2 jugadores")
        elif i>=2 and i<=4:
            root.destroy()


    label = Label(root,text="Escriba su nombre",
                    font=("Times",20,"bold"),fg="red")
    label.place(x=125,y=5) # Etiqueta principal

    receiver = Entry(root,font=("Times",15),justify="center")
    receiver.place(x=100,y=100)  # Caja de Texto

    sig = Button(root,text="Tirar dado",font=("Times",12),command=next)
    sig.place(x=100,y=125)  #Insertar nombre

    start = Button(root,text="Comenzar ",font=("Times",12),command=begin)
    start.place(x=200,y=125)    # Empezar juego

    label1 = Label(root,text=f"Jugadores {i}",
                    font=("Times",15),fg="red")
    label1.place(x=0,y=200) #Número de jugadores

    root.mainloop()

    return sort(turns)

class Receiver:
    
    def __init__(self) -> None:
        """
        Clase para guardar variables de ventanas 
        de tkinter

        + answer = resultado
        """
        self.answer = 0

    def menu_compra(self,sitio,player):
        root = Tk()
        root.geometry("500x250+550+100")
        root.resizable(False, False)
        root.overrideredirect(True)
        def buy():
            sig.destroy()
            comprar.destroy()
            label.config(text=f"Lo ha comprado por {sitio.costo}")
            label1.config(text=f"Costo:{sitio.costo} Dueño:{player.name}")
            self.answer = 1
            money.config(text = f"Dinero: {player.balance-sitio.costo}")
            root.after(1500,continuar)
            

        def continuar():
            root.destroy()

        label = Label(root,text=f"Ha aterrizado en {sitio.name}",
                        font=("Times",20),fg="red")
        label.place(x=0,y=5) # Etiqueta principal
        
        label1 = Label(root,text=f"Costo:{sitio.costo} Dueño:{sitio.owner}",
                        font=("Times",20),fg="blue")
        label1.place(x=0,y=50) # Etiqueta principal
        if isinstance(sitio,Propiedad):
            label2 = Label(root,text=f"Renta:{sitio.renta}",
                        font=("Times",20),fg="blue")
            label2.place(x=0,y=100) # Etiqueta principal

        comprar = Button(root,text="Comprar",font=("Times",12),command=buy)
        comprar.place(x=100,y=125)  

        sig = Button(root,text="No comprar ",font=("Times",12),command=continuar)
        sig.place(x=200,y=125)  

        money = Label(root,text = f"Dinero: {player.balance}",
        font=("Times",12,"bold"),fg="green")
        money.place(x=0,y=200)  

        root.mainloop()
    
    def menu_inventorio(self,player):
        root = Tk()
        root.geometry("800x250+0+0")
        root.resizable(False, False)
        root.title("Monopoly X Dr. Who")

        def mostrar():
            prop = Label( root,text=f"Propiedades: {player.inventory['propiedades']}",
            font=("Times",12),fg="blue")
            prop.place(x=0,y=0)

            serv = Label(root,text =f"Servicios: {player.inventory['servicios']}",
            font=("Times",12),fg="blue")
            serv.place(x=0,y=30)

            ferr = Label(root,text = f"Ferrocarriles: {player.inventory['ferrocarriles']}",
            font=("Times",12),fg="blue")
            ferr.place(x=0,y=60) 

            pas = Label(root,text = f"Pases {player.inventory['pases']}",
            font=("Times",12),fg="blue")
            pas.place(x=0,y=90)

            colors = Label(root,text = f"Colores {player.inventory.colores}",
            font=("Times",12),fg="blue")
            colors.place(x=0,y=120)

            money = Label(root,text = f"Dinero: {player.balance}",
            font=("Times",12,"bold"),fg="green")
            money.place(x=0,y=150)

        def seguir():
            root.destroy()

        vend = Label(root,text = f"Vendibles: {player.inventory.sellable}",
        font=("Times",15),fg="blue")
        vend.place(x=650,y=200)

        btn = Button(root,text="ver inventorio",font=("Times",12),command=mostrar)
        btn.place(x=0,y=200)  

        btn3 = Button(root,text="Jugar",font=("Times",12),command=seguir)
        btn3.place(x=300,y=200) 

        

        root.mainloop()

    def menu_venta(self,player):
        """
        Menu gráfico de venta de elementos
        """
        root = Tk()
        root.geometry("500x250+550+100")
        root.resizable(False, False) # Dimensiones
        root.title("Monopoly X Dr. Who")

        def vender():
            type = tipo.get()
            s = entry.get()
            if s == "" or type == "":
                error.config(text="Faltan datos")
            elif type not in ["1","2","3"]:
                error.config(text="Opción no valida en entrada superior")
            else:
                done = player.tksell_menu(type,s)
                if done == 1:
                    error.config(text=f"Vendido {s}")
                else:
                    error.config(text=f"{s} no hallado")
            money.config(text = f"Dinero: {player.balance}")
            root.after(1000,reset)

        def reset():
            money.config(text = f"Dinero: {player.balance}")
            error.config(text="")

        def vender_pase():
            done = player.sell_pass()
            if done == 1:
                error.config(text="Vendido 1 Pase")
            else:
                error.config(text="No tiene pases")
            money.config(text = f"Dinero: {player.balance}")
            root.after(500,reset)
        
        def inv():
            self.menu_inventorio(player)
                

        tipo = Entry(root,font=("Times",12),justify="center")
        tipo.place(x=150,y=80) # Parametro 1

        entry = Entry(root,font=("Times",12),justify="center")
        entry.place(x=150,y=120) # Parametro 2 (Nombre)


        btn2 = Button(root,text="vender",font=("Times",12),command=vender)
        btn2.place(x=150,y=160)  # Vender

        btn3 = Button(root,text="vender 1 pase",font=("Times",12),command=vender_pase)
        btn3.place(x=210,y=160) #Vender pase de cárcel

        btn4 = Button(root,text="Inventorio",font=("Times",12),command=inv)
        btn4.place(x=310,y=160)

        vend = Label(root,text = f"Escriba 1 Propiedades 2 Ferrocarriles 3 Servicios \nen entrada superior",
        font=("Times",15),fg="blue")
        vend.place(x=50,y=0)

        info = Label(root,text = f"Luego el nombre en la otra entrada",
        font=("Times",15),fg="blue")
        info.place(x=100,y=50)

        error = Label(root,text = f"",
        font=("Times",12),fg="red")
        error.place(x=0,y=200)

        money = Label(root,text = f"Dinero: {player.balance}",
        font=("Times",12,"bold"),fg="green")
        money.place(x=400,y=200)

        vend = Label(root,text = f"Vendibles: {player.inventory.sellable}",
        font=("Times",15),fg="blue")
        vend.place(x=150,y=200)

        root.mainloop()
        
def notificar(info,wait=2,player=None):
    """
    Información basica para usuario
    + info: la información 
    + wait: duración en segundos de ventana
    + player: Jugador a mostrar info
    """
    root = Tk()
    root.geometry("500x250+550+100")
    root.resizable(False, False) # Dimensiones
    root.title("Monopoly X Dr. Who")

    def close():
        root.destroy()

    vend = Label(root,text =info,
    font=("Times",20),fg="black")
    if len(info)<20:
        vend.place(x=100,y=100)
    else:
        vend.place(x=0,y=100)
    root.after(wait*1000,close)
    if player is not None:
        label = Label(root,text =f"Jugador: {player.name}   Dinero:{player.balance}",
        font=("Times",20),fg="Green")
        label.place(x=0,y=200)
    root.mainloop()


def notificar_transfer(info,wait=4,player=None):
    """
    Muestra resultado de transacción
    """
    root = Tk()
    root.geometry("500x250+550+100")
    root.resizable(False, False) # Dimensiones
    root.title("Monopoly X Dr. Who")

    def close():
        root.destroy()
    tit = Label(root,text ="Debe pagarle a otro jugador",
    font=("Times",20),fg="red")
    tit.place(x=100,y=0)

    vend = Label(root,text =info,
    font=("Times",20),fg="black")
    if len(info)<20:
        vend.place(x=100,y=100)
    else:
        vend.place(x=0,y=100)
    root.after(wait*1000,close)
    if player is not None:
        label = Label(root,text =f"Jugador: {player.name}   Dinero:{player.balance}",
        font=("Times",20),fg="Green")
        label.place(x=0,y=200)
    root.mainloop()
    