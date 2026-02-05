#Napiši snake-game v pygamu
#koda od prej ti lahko sliži za inspiracijo (npr dolzina kace s kvadratki -> to pride prav)

#za projekt naredite github repo, in spremembe sproti comitatje addajte in pushajte
#na koncu morajo biti v repozitoriju vsaj 3 vecji commiti

#1. dodatna naloga:
#naredi branch "izgled"
#v tem brancu naredi logiko, da ko igra tece, lahko pritisnes gumb "space" kar celotni kaci nastavi nakljucno barvo

#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi megre obeh branchov 

import pygame
import time
import threading

ex=False

pygame.init()

clock = pygame.time.Clock()

canvas = pygame.display.set_mode((500, 500))
canvas_color = (255, 255, 255)
pygame.display.set_caption("Kača")


glava=pygame.Rect(240, 240, 10, 10)
smer="gor"

while not ex:
    clock.tick(10)

    canvas.fill(canvas_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ex = True

        if pygame.key.get_pressed()[pygame.K_w]:
            smer="gor"
        elif pygame.key.get_pressed()[pygame.K_s]:
            smer="dol" 
        elif pygame.key.get_pressed()[pygame.K_a]:
            smer="levo"
        elif pygame.key.get_pressed()[pygame.K_d]:
            smer="desno"
    
    if smer=="gor":
        glava.y-=10
    elif smer=="dol":
        glava.y+=10
    elif smer=="levo":
        glava.x-=10
    elif smer=="desno":
        glava.x+=10
    
    pygame.draw.rect(canvas, (0, 255, 0), glava)
    
    pygame.display.update()
    