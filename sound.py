import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import time

mixer.init()

def theme():
    sound1=mixer.Sound("img\\drwho_theme.wav")
    sound1.set_volume(0.1)
    sound1.play(1)

def die_sound():
    die = mixer.Sound("img\\tirar_dado.wav")
    die.set_volume(0.4)
    die.play()
    time.sleep(1.5)

def buy_sound():
    die = mixer.Sound("img\\comprar.wav")
    die.play()

def jail_sound():
    die = mixer.Sound("img\\jail.wav")
    die.play()