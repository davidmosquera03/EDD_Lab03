from Board import Board
from Nodo import *
tablero = Board()

casillas = open('casillas.txt') 
line = casillas.readline()
while line != "":
    # print(line)
    data = line.split(',')
    #print(data[2])
    if data[2] == "0":
        #print("casilla corresponde a Nodo\n")
        P = Nodo(int(data[0]),data[1])
        tablero.add_node2(P)
    elif data[2] == "1":
        #print("casilla corresponde a propiedad\n")
        P = Propiedad(int(data[0]),data[1],int(data[3]),int(data[4]),data[5])
        tablero.add_node2(P)
    elif data[2] == "2":
        #print("casilla corresponde a servicio\n")
        P = Servicio(int(data[0]),data[1])
        tablero.add_node2(P)
    elif data[2] == "3":
        #print("casilla corresponde a ferrocarril\n")
        P = Ferrocarril(int(data[0]),data[1])
        tablero.add_node2(P)
    elif data[2] == "4":
        #print("casilla corresponde a suerte\n")
        P = Suerte(int(data[0]),data[1])
        tablero.add_node2(P)
    elif data[2] == "5":
        #print("casilla corresponde a cofre\n")
        P = Cofre(int(data[0]),data[1])
        tablero.add_node2(P)
    elif data[2] == "6":
        #print("casilla corresponde a impuesto\n")
        P = Impuesto(int(data[0]),data[1],int(data[3]))
        tablero.add_node2(P)
    line = casillas.readline()

def sort(list):
    """
    Ordena resultados de lanzamientos de dado
    de mayor a menor
    """ 
    for i in range(0,len(list)-1):  
        for j in range(len(list)-1):  
            if(list[j][0]<list[j+1][0]):  
                temp = list[j]  
                list[j] = list[j+1]  
                list[j+1] = temp  
    return list  

def add_by_turns(list,game):
    for sublist in list:
        game.add_player(sublist[1])
