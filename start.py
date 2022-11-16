from tkinter import *
from sound import die_sound
from random import randint
from generador import sort    


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


def menu():
    root = Tk()
    root.geometry("500x250+550+100")
    root.resizable(False, False)

    root.mainloop()