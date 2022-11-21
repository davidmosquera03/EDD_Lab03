from pygame import *
import pygame as pg
import sys
from Nodo import *
from start import asignar,Receiver,notificar
from Player import Player
from generador import tablero,add_by_turns
from Game import Game,Player
from sound import theme
pg.init()

g = Game(tablero)
data = Receiver()
turns = asignar()

add_by_turns(turns, g)

actualplayer = []
for player in g.players.copy().values():  
    # Añade jugadores a lista para referirse a ella en Pygame
    actualplayer.append(player.name)



ventana = pg.display.set_mode((1000, 740))
pg.display.set_caption("Monopoly X Dr. Who")

# colores
black = (0, 0, 0)
white = (255, 255, 255) 
pink = (255, 112, 193)
blue = (112, 174, 255)
orange = (255, 114, 48)

#Posiciones iniciales de jugadores
one = (710, 700)
two = (710, 670)
three = (680, 700)
four = (680, 670)


def draw_button(ventana, boton, palabra):
    """
    ventana: superficie donde se dibuja
    boton: rectangulo con dimensiones 
    palabra: texto a mostrar
    """
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(ventana, (237, 128, 19), boton, 0)
        # superficie,(r,g,b),boton,0 rellena
    else:    
        draw.rect(ventana, (70, 189, 34), boton, 0)
    texto = myfont.render(palabra, True, (255, 255, 255))
    ventana.blit(texto, (boton.x+(boton.width-texto.get_width())/2, 
                        boton.y+(boton.height-texto.get_height())/2))
                        # Centra

def draw_player(ventana, color, number):
    draw.circle(ventana, color, number , radius=12)


def draw_label(ventana,texto): #Resultado dado
    text_surface = myfont.render(texto, False, (100, 24, 45))
    ventana.blit(text_surface, (800,20))

def draw_name(ventana,texto): #Nombre
    text_surface = myfont.render(texto, False, (100, 24, 45))
    ventana.blit(text_surface, (900,20))


def comprar(sitio:Nodo,player:Player):
    data.menu_compra(sitio,player)
    if data.answer == 1:
        player.buy(sitio)
    
    data.answer = 0

framerate = 60

fondo = pg.image.load("img\\tablero.jpeg")
layer = pg.image.load("img\\layer.jpg")

layer = transform.scale(layer,(260,740))
fondo = transform.scale(fondo, (740,740))

myfont = font.SysFont("Calibri", 30)
timer = pg.time.Clock()

die_button = Rect(800,100,150,50)
sell_button = Rect(800,200,150,50)
inv_button = Rect(800,300,150,50)
# Forma de botones

posiciones = {0: (711, 699), 1: (613, 702), 2: (551, 699), 3: (491, 700),
            4: (430, 699), 5: (372, 693), 6: (305, 694), 7: (246, 689), 8: (188, 691),
            9: (122, 691), 10: (47, 683), 11: (43, 613), 12: (29, 554), 13: (38, 492),
            14: (39, 431), 15: (32, 372), 16: (33, 311), 17: (38, 246), 18: (37, 187),
            19: (41, 129), 20: (41, 50), 21: (133, 52), 22: (190, 53), 23: (236, 51), 
            24: (306, 57), 25: (370, 61), 26: (428, 55), 27: (481, 54), 28: (549, 57), 
            29: (601, 54), 30: (687, 64), 31: (687, 126), 32: (697, 181), 33: (689, 247),
            34: (694, 311), 35: (691, 374), 36: (697, 423), 37: (695, 492), 38: (697, 550), 
            39: (703, 613)}
# Diccionario de posiciones en pantalla con base a loc de Nodos           
i = 0
v = 0
w = 0
z = 0
j = 0
g.start()

def update_place(numero,new):
    ventana.blit(layer,(740,0))
    ventana.blit(fondo, (0,0))
    if numero == 0:
        global i
        i = new
        one = posiciones[i]
        draw_player(ventana, pink, one)   
    elif numero == 1:
        global v
        v = new
        two = posiciones[v]
        draw_player(ventana, black, two)
    elif numero == 2:
        global w
        w = new
        three = posiciones[w]
        draw_player(ventana, blue, three)
    elif numero == 3:
        global z
        z = new
        four = posiciones[z]
        draw_player(ventana, orange, four)

theme()
while True:
    timer.tick(framerate)

    for event in pg.event.get():
        if event.type == pg.QUIT or len(actualplayer)==1:
            notificar("Ha terminado el juego",4)
            pg.quit()
            sys.exit()
            
        if event.type==pg.MOUSEBUTTONDOWN and BUTTON_LEFT:
            
            if die_button.collidepoint(mouse.get_pos()):
                
                
                if k.on_jail:
                    print("Turno en carcel de ",k.name,"(encarcelado)")
                    k.jugar_carcel()


                if not k.on_jail:
                    print("Turno de ",k.name,"ubicado en: ",k.pos) #Nombre y casilla
                    amount,repeat = k.jugar_turno()
                    # mostrar(die,player)
                    for x in range(amount): #Animación de desplazamiento
                        ventana.blit(fondo,(0,0))
                    
                        if numero == 0:
                            i += 1
                        elif numero == 1:
                            v += 1
                        elif numero == 2:
                            w += 1
                        elif numero == 3:
                            z += 1
                    
                    
                        if i==len(posiciones):
                            i=0
                        elif v==len(posiciones):
                            v=0
                        elif w==len(posiciones):
                            w=0
                        elif z==len(posiciones):
                            z=0

                        time.delay(500)
                        
                        if numero == 0:
                            one = posiciones[i]
                            draw_player(ventana, pink, one)   
                        elif numero == 1:
                            two = posiciones[v]
                            draw_player(ventana, black, two)
                        elif numero == 2:
                            three = posiciones[w]
                            draw_player(ventana, blue, three)
                        elif numero == 3:
                            four = posiciones[z]
                            draw_player(ventana, orange, four)
                        draw_label(ventana,str(amount))
                        pg.display.flip()
                    sitio = k.pos 
                    #Validaciones de posición de jugador
                    if isinstance(sitio,Suerte):
                        tipo,goal = g.sacar_carta("suerte.txt")
                        res = g.jugar_suerte(k,tipo,goal)
                        sitio = k.pos
                        if res !=None:
                            update_place(numero,res)
                        pg.display.flip()    

                    if isinstance(sitio,Propiedad): # Propiedad
                        print("Costo ",sitio.costo,"Renta ",sitio.renta
                            ," Dueño ",sitio.owner,"color ",sitio.color)
                        if sitio.owner is None:
                            comprar(sitio,k)
                        elif sitio.owner!=k.name:
                            print("debe pagar ",sitio.renta)
                            g.transfer(k.name,sitio.owner,sitio.renta)
                        else:
                            notificar("Propiedad Propia",2,k)
                    
                    elif isinstance(sitio,Servicio): #Servicio
                        print("Costo ",sitio.costo," Dueño ",sitio.owner)
                        if sitio.owner is None:
                            comprar(sitio,k)
                        elif sitio.owner!=k.name:
                            g.pagar_servicio(k,sitio.owner)
                    
                    elif isinstance(sitio,Ferrocarril): # Ferrocarril
                        print("Costo ",sitio.costo," Dueño ",sitio.owner)
                        if sitio.owner is None:
                            comprar(sitio,k)
                        elif sitio.owner!=k.name:
                            g.pagar_ferrocarril(k,sitio.owner)
                        
                    elif isinstance(sitio,Cofre):
                        tipo,cant = g.sacar_carta("cofre.txt")
                        g.jugar_cofre(tipo,cant,k)

                    elif isinstance(sitio,Impuesto):
                        print("Debe pagar ",sitio.pago)
                        k.withdraw(sitio.pago)
                        notificar(f"Debe pagar {sitio.pago}")
                    
                    elif isinstance(sitio,Nodo):
                        print("sitio es",sitio," loc ",sitio.loc)
                        if sitio.loc==30:
                            notificar(f"Ha sido Encarcelado")
                            update_place(numero,10)
                            pg.display.flip()
                            g.imprison(k)  # Si Nodo es vayase a la carcel
                                         
                if k.balance<0:
                    notificar("Bancarrota posible",2,k)
                    while k.balance<0 and k.inventory.sellable>0:
                        print("¡A Vender!")
                        data.menu_venta(k)
                    if k.balance<0:
                        g.remove_player(k.name)
                        actualplayer.remove(k.name) # Remueve jugador

                if repeat == 0 or k.on_jail:
                        j += 1 # cambiar de jugador
                        
                if j == len(g.players):
                    j = 0
        

            if sell_button.collidepoint(mouse.get_pos()):
                data.menu_venta(k)
                print("vendiendo")

            if inv_button.collidepoint(mouse.get_pos()):
                data.menu_inventorio(k)
                print("inventario :D")




    ventana.blit(fondo, (0,0))
    ventana.blit(layer,(740,0))
    draw_button(ventana,die_button, "lanzar dado")
    draw_button(ventana,sell_button, "Vender")
    draw_button(ventana,inv_button,"Inventorio")
    if len(g.players) >= 1: # Dibujar numero de jugadores en juego
        draw_player(ventana, pink, one)
    if len(g.players) >= 2: 
        draw_player(ventana, black, two)
    if len(g.players) >= 3:
        draw_player(ventana, blue, three)
    if len(g.players) >= 4:
        draw_player(ventana, orange, four)
    numero = actualplayer.index(actualplayer[j]) #Numero de jugador es indice de lista de jugador
    k = g.players.get(actualplayer[j])  # Jugador actual
    draw_name(ventana, k.name)
    pg.display.flip()