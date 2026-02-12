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


pygame.init()

clock = pygame.time.Clock()

canvas = pygame.display.set_mode((500, 500))
canvas_color = (255, 255, 255)
pygame.display.set_caption("Kača")


pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)






def igra():
    ex=False
    izguba=False
    game_over_text = my_font.render('Game over', False, (255, 69, 69))
    barva="rdeča"
    
    
    glava=pygame.Rect(240, 240, 20, 20)
    smer="gor"
    while not ex:
        clock.tick(5)
        if barva=="rdeča":
            canvas.fill((255, 255, 255))
        else:
            canvas.fill((0, 255, 0))
            
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
        elif pygame.key.get_pressed()[pygame.K_SPACE]:
            if barva=="rdeča":
                barva="zelena"
            else:
                barva="rdeča"
        
        if smer=="gor":
            glava.y-=20
        elif smer=="dol":
            glava.y+=20
        elif smer=="levo":
            glava.x-=20
        elif smer=="desno":
            glava.x+=20
            
        if barva=="rdeča":
            canvas.fill((255, 255, 255))
        else:
            canvas.fill((0, 255, 0))
        
        
        
        if glava.y<0 or glava.y>480 or glava.x<0 or glava.x>480:
            ex=True
            izguba=True
            
            canvas.blit(game_over_text, (170,220))
            
            

        
        
        
        
        if barva=="rdeča":
            pygame.draw.rect(canvas, (0, 255, 0), glava)
        else:
            pygame.draw.rect(canvas, (255, 69, 69), glava)
        
        pygame.display.update()
    if izguba:
        time.sleep(5)
    
    

press_space_text = my_font.render('Pritisni presledek za začetek.', False, (255, 69, 69))

izhod=False
while not izhod:
    clock.tick(5)
    canvas.fill(canvas_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            izhod = True
    
    if pygame.key.get_pressed()[pygame.K_SPACE]:
            igra()
            
            
            
    canvas.blit(press_space_text, (75,220))
    pygame.display.update()

        