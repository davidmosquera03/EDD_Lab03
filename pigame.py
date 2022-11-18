from pygame import *
import pygame as pg
import sys
from random import randint
from start import Receiver
from Player import Player
pg.init()

ventana = pg.display.set_mode((1000, 740))
pg.display.set_caption("Monopoly X Dr. Who")

# colores

black = (0, 0, 0)
white = (255, 255, 255)
pink = (255, 112, 193)
blue = (112, 174, 255)
orange = (255, 114, 48)

#players beginning positions
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



def draw_all():
    draw_player(ventana, pink, one)
    draw_player(ventana, black, two)
    draw_player(ventana, blue, three)
    draw_player(ventana, orange, four)

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

x = 710




posiciones = {0: (711, 699), 1: (613, 702), 2: (551, 699), 3: (491, 700),
            4: (430, 699), 5: (372, 693), 6: (305, 694), 7: (246, 689), 8: (188, 691),
            9: (122, 691), 10: (47, 683), 11: (43, 613), 12: (29, 554), 13: (38, 492),
            14: (39, 431), 15: (32, 372), 16: (33, 311), 17: (38, 246), 18: (37, 187),
            19: (41, 129), 20: (41, 50), 21: (133, 52), 22: (190, 53), 23: (236, 51), 
            24: (306, 57), 25: (370, 61), 26: (428, 55), 27: (481, 54), 28: (549, 57), 
            29: (601, 54), 30: (687, 64), 31: (687, 126), 32: (697, 181), 33: (689, 247),
            34: (694, 311), 35: (691, 374), 36: (697, 423), 37: (695, 492), 38: (697, 550), 
            39: (703, 613)}
i = 0
receiver = Receiver()
jugadores = {pink:one,black:two,blue:three,orange:four}
from Nodo import Propiedad
dave = Player("david")
dave.buy(Propiedad(0,"Casa",100,20,"rojo"))

while True:
    timer.tick(framerate)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
        if event.type==pg.MOUSEBUTTONDOWN and BUTTON_LEFT:
            
            if die_button.collidepoint(mouse.get_pos()):
                
                
                die = randint(1,12)
                print(die)
                for x in range(die):
                    ventana.blit(fondo,(0,0))
                    i += 1
                    if i==len(posiciones):
                        i=0
                    one = posiciones[i]
                    time.delay(500)
                    draw_player(ventana, pink, one)

                    draw_label(ventana,str(die))

                    pg.display.flip()
                    
               

            if sell_button.collidepoint(mouse.get_pos()):
                receiver.menu_venta(dave)

            if inv_button.collidepoint(mouse.get_pos()):
                receiver.menu_inventorio(dave)




    ventana.blit(fondo, (0,0))
    ventana.blit(layer,(740,0))
    draw_button(ventana,die_button, "lanzar dado")
    draw_button(ventana,sell_button, "Vender")
    draw_button(ventana,inv_button,"Inventorio")

    draw_player(ventana, pink, one)
    draw_player(ventana, black, two)
    draw_player(ventana, blue, three)
    draw_player(ventana, orange, four)
    draw_name(ventana,"Carlos")
    pg.display.flip()
    