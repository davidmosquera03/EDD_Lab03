from tkinter import *
from sound import die_sound
from random import randint
from generador import sort  
from Player import Player

i = 0
def asignar():
    """
    Recibe los nombres de los jugadores
    tiran dados y segun el orden jugarán
    """
    root = Tk()
    root.geometry("500x250+550+100")
    root.resizable(False, False)

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
                    font=("Times,20"),fg="red")
    label.place(x=125,y=5) # Etiqueta principal

    receiver = Entry(root,font=("Times",15),justify="center")
    receiver.place(x=100,y=100)  # Caja de Texto

    sig = Button(root,text="Tirar dado",font=("Times",12),command=next)
    sig.place(x=100,y=125)  #Insertar nombre

    start = Button(root,text="Comenzar ",font=("Times",12),command=begin)
    start.place(x=200,y=125)    # Empezar juego

    label1 = Label(root,text=f"Jugadores {i}",
                    font=("Times,10"),fg="red")
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

    def menu_compra(self,sitio,player:Player):
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
            root.after(1500,continuar)
            

        def continuar():
            root.destroy()

        label = Label(root,text=f"Ha atterizado en {sitio.name}",
                        font=("Times,20"),fg="red")
        label.place(x=0,y=5) # Etiqueta principal
        
        label1 = Label(root,text=f"Costo:{sitio.costo} Dueño:{sitio.owner}",
                        font=("Times,20"),fg="blue")
        label1.place(x=0,y=50) # Etiqueta principal


        comprar = Button(root,text="Comprar",font=("Times",12),command=buy)
        comprar.place(x=100,y=125)  #Insertar nombre

        sig = Button(root,text="No comprar ",font=("Times",12),command=continuar)
        sig.place(x=200,y=125)    # Empezar juego

        root.mainloop()
    
    def menu_inventorio(self,player:Player):
        root = Tk()
        root.geometry("800x250+550+100")
        root.resizable(False, False)

        def mostrar():
            prop = Label( root,text=f"Propiedades: {player.inventory['propiedades']}",
            font=("Times,12"),fg="blue")
            prop.place(x=0,y=0)

            serv = Label(root,text =f"Servicios: {player.inventory['servicios']}",
            font=("Times,12"),fg="blue")
            serv.place(x=0,y=30)

            ferr = Label(root,text = f"Ferrocarriles: {player.inventory['ferrocarriles']}",
            font=("Times,12"),fg="blue")
            ferr.place(x=0,y=60) 

            pas = Label(root,text = f"Pases {player.inventory['pases']}",
            font=("Times,12"),fg="blue")
            pas.place(x=0,y=90)

            colors = Label(root,text = f"Colores {player.inventory.colores}",
            font=("Times,12"),fg="blue")
            colors.place(x=0,y=120)

        def seguir():
            root.destroy()

        vend = Label(root,text = f"Vendibles: {player.inventory.sellable}",
        font=("Times,15"),fg="blue")
        vend.place(x=650,y=200)

        btn = Button(root,text="ver inventorio",font=("Times",12),command=mostrar)
        btn.place(x=0,y=200)  

        btn3 = Button(root,text="Jugar",font=("Times",12),command=seguir)
        btn3.place(x=300,y=200) 

        

        root.mainloop()

    def menu_venta(self,player:Player):
        """
        Menu gráfico de venta de elementos
        """
        root = Tk()
        root.geometry("500x250+550+100")
        root.resizable(False, False) # Dimensiones

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
            root.after(1000,reset)

        def reset():
            error.config(text="")

        def vender_pase():
            done = player.sell_pass()
            if done == 1:
                error.config(text="Vendido 1 Pase")
            else:
                error.config(text="No tiene pases")
            root.after(500,reset)

        tipo = Entry(root,font=("Times",12),justify="center")
        tipo.place(x=100,y=80)

        entry = Entry(root,font=("Times",12),justify="center")
        entry.place(x=100,y=120)
    
       

        btn2 = Button(root,text="vender",font=("Times",12),command=vender)
        btn2.place(x=150,y=160) 

        btn3 = Button(root,text="vender 1 pase",font=("Times",12),command=vender_pase)
        btn3.place(x=210,y=160)

        vend = Label(root,text = f"Escriba 1 Propiedades 2 Ferrocarriles 3 Servicios \nen entrada superior",
        font=("Times,12"),fg="blue")
        vend.place(x=0,y=0)

        info = Label(root,text = f"Luego el nombre en la otra entrada",
        font=("Times,12"),fg="blue")
        info.place(x=100,y=50)

        error = Label(root,text = f"",
        font=("Times,10"),fg="red")
        error.place(x=0,y=200)

        root.mainloop()
        
def notificar(info,wait=2):
        root = Tk()
        root.geometry("500x250+550+100")
        root.resizable(False, False) # Dimensiones
        def close():
            root.destroy()

        vend = Label(root,text =info,
        font=("Times",20),fg="black")
        vend.place(x=100,y=100)
        root.after(wait*1000,close)
        root.mainloop()



