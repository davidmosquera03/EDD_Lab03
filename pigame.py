from pygame import *
import pygame as pg
import sys
import random

pg.init()

ventana = pg.display.set_mode((1000, 740))
pg.display.set_caption("Monopoly X Dr. Who")

# colores

black = (0, 0, 0)
white = (255, 255, 255)
pink = (255, 112, 193)
blue = (112, 174, 255)
orange = (255, 114, 48)

def draw_button(ventana, boton, palabra):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(ventana, (237, 128, 19), boton, 0)
    else:    
        draw.rect(ventana, (70, 189, 34), boton, 0)
    texto = myfont.render(palabra, True, (255, 255, 255))
    ventana.blit(texto, (boton.x+(boton.width-texto.get_width())/2, 
                        boton.y+(boton.height-texto.get_height())/2))
def draw_player(ventana, color, number):
    draw.circle(ventana, color, number , radius=12)

#players

one = (710, 700)
two = (710, 670)
three = (680, 700)
four = (680, 670)

framerate = 60
fondo = pg.image.load("tablero.png")
fondo = transform.scale(fondo, (740,740))
myfont = font.SysFont("Calibri", 30)
timer = pg.time.Clock()
die_button = Rect(800,100,150,50)
sell_button = Rect(800,200,150,50)
posiciones = {}
x = 710
while True:
    timer.tick(framerate)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.MOUSEBUTTONDOWN and BUTTON_LEFT:
            # print(mouse.get_pos())
        
            
            if die_button.collidepoint(mouse.get_pos()):
                draw.rect(ventana, (237, 128, 19), die_button, 0)
                x -= 20
                one = (x,700)
                #print("dado lanzado")
            if sell_button.collidepoint(mouse.get_pos()):
                draw.rect(ventana, (237, 128, 19), sell_button, 0)
                print("vendido")




    ventana.blit(fondo, (0,0))
    draw_button(ventana, die_button, "lanzar dado")
    draw_button(ventana, sell_button, "vender")
    draw_player(ventana, pink, one)
    draw_player(ventana, black, two)
    draw_player(ventana, blue, three)
    draw_player(ventana, orange, four)
    pg.display.flip()