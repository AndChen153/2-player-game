=[]
y=[]
coordinates=[]
redpwup=[]
for i in range(250,501):
    x.append(i)
for i in range (150,226):
    y.append(i)
for i in range(0, 241):
    for j in range(0, 71):
        coordinates.append([x[i], y[0]])
        coordinates.append([x[i], y[1]])
        coordinates.append([x[i], y[2]])
        coordinates.append([x[i], y[68]])
        coordinates.append([x[i], y[69]])
        coordinates.append([x[i], y[70]])
        coordinates.append([x[0], y[j]])
        coordinates.append([x[1], y[j]])
        coordinates.append([x[2], y[j]])
        coordinates.append([x[238], y[j]])
        coordinates.append([x[239], y[j]])
        coordinates.append([x[240], y[j]])
for i in range(250, 326):
    x.append(i)
for i in range (225,476):
    y.append(i)
for i in range(0, 76):
    for j in range(0, 251):
        coordinates.append([x[i], y[0]])
        coordinates.append([x[i], y[1]])
        coordinates.append([x[i], y[2]])
        coordinates.append([x[i], y[248]])
        coordinates.append([x[i], y[249]])
        coordinates.append([x[i], y[250]])
        coordinates.append([x[0], y[j]])
        coordinates.append([x[1], y[j]])
        coordinates.append([x[2], y[j]])
        coordinates.append([x[73], y[j]])
        coordinates.append([x[74], y[j]])
        coordinates.append([x[75], y[j]])
x=[]
y=[]
for i in range(425, 501):
    x.append(i)
for i in range (225, 400):
    y.append(i)
for i in range(0, 76):
    for j in range(0, 171):
        coordinates.append([425, y[j]])
        coordinates.append([426, y[j]])
        coordinates.append([427, y[j]])
        coordinates.append([498, y[j]])
        coordinates.append([499, y[j]])
        coordinates.append([500, y[j]])
        coordinates.append([x[i], y[0]])
        coordinates.append([x[i], y[1]])
        coordinates.append([x[i], y[2]])
        coordinates.append([x[i], 398])
        coordinates.append([x[i], 399])
        coordinates.append([x[i], 400])
x=[]
y=[]
for i in range(325, 351):
    x.append(i)
for i in range (325, 401):
    y.append(i)
for i in range(0, 26):
    for j in range(0, 76):
        coordinates.append([x[0], y[j]])
        coordinates.append([x[1], y[j]])
        coordinates.append([x[2], y[j]])
        coordinates.append([x[23], y[j]])
        coordinates.append([x[24], y[j]])
        coordinates.append([x[25], y[j]])
        coordinates.append([x[i], y[0]])
        coordinates.append([x[i], y[1]])
        coordinates.append([x[i], y[2]])
        coordinates.append([x[i], y[73]])
        coordinates.append([x[i], y[74]])
        coordinates.append([x[i], y[75]])
x=[]
y=[]
for i in range(400, 476):
    x.append(i)
for i in range (325, 401):
    y.append(i)
for i in range(0, 76):
    for j in range(0, 76):
        coordinates.append([x[0], y[j]])
        coordinates.append([x[1], y[j]])
        coordinates.append([x[2], y[j]])
        coordinates.append([x[73], y[j]])
        coordinates.append([x[74], y[j]])
        coordinates.append([x[75], y[j]])
        coordinates.append([x[i], y[0]])
        coordinates.append([x[i], y[1]])
        coordinates.append([x[i], y[2]])
        coordinates.append([x[i], y[73]])
        coordinates.append([x[i], y[74]])
        coordinates.append([x[i], y[75]])
x=[]
y=[]
redpwup
for i in range(375, 426):
    x.append(i)
for i in range (275, 326):
    y.append(i)
for i in range(0, 51):
    for j in range(0, 51):
        redpwup.append([x[0], y[j]])
        redpwup.append([x[1], y[j]])
        redpwup.append([x[2], y[j]])
        redpwup.append([x[48], y[j]])
        redpwup.append([x[49], y[j]])
        redpwup.append([x[50], y[j]])
        redpwup.append([x[i], y[0]])
        redpwup.append([x[i], y[1]])
        redpwup.append([x[i], y[2]])
        redpwup.append([x[i], y[48]])
        redpwup.append([x[i], y[49]])
        redpwup.append([x[i], y[50]])

        
import pygame
import os
import random
import sys
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_blue = True
x=100
y=100
rp=False
lp=False
up=False
dp=False
rp2=False
lp2=False
up2=False
dp2=False
speedin=0
speedcheck=True
a=3
a2=3
q=0
attackleft=[]
attackright=[]
attackup=[]
attackdown=[]
p2x=650
p2y=100
attacktime=0
attacktime2=0
player1health=5
player2health=5
enemyx=25
enemyy=425
enemy2x=725
enemy2y=425
s=0
player1dmg=True
player2dmg=True
dmg1=1
dmg2=1

face = pygame.image.load('face.jpg')
cornright = pygame.image.load('cornright.jpg')
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
    
        
def background():
    screen.fill((166, 166, 166))                
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(0, 0, 800, 25))
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(0, 0, 25, 600))
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(775, 0, 25, 600))
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(0, 600, 800, 25))
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(0, 575, 800, 25))
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(300, 200, 200, 25))
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(300, 225, 25, 175))
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(475, 225, 25, 175))
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(325, 375, 25, 25))
    pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(450, 375, 25, 25))
    
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(375, 275, 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(25, 575, 125, 25))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(650, 575, 125, 25))


'''wtmiddleinside=[325]
wtmiddleinside.append()'''
poslast=[100,100]
poslast2=[650,100]
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        background()
        pressed = pygame.key.get_pressed()
        pos=[x,y]
        pos2=[p2x,p2y]
        #print (pos)
        if pos in redpwup and speedcheck==True:
            dmg=2
            speedcheck=False
        if pos2 in redpwup and speedcheck==True:
            dmg2=2
            speedcheck=False
        if pos not in coordinates:
            if pressed[pygame.K_w]:
                if y >= 25:
                    y -= a
                up=True
                rp=False
                lp=False
                dp=False
            if pressed[pygame.K_s]:
                if y <= 525:
                    y += a
                rp=False
                lp=False
                up=False
                dp=True
            if pressed[pygame.K_a]:
                if x >=25:
                    x -= a
                rp=False
                lp=True
                up=False
                dp=False
            if pressed[pygame.K_d]:
                if x <= 725:
                    x += a
                rp=True
                lp=False
                up=False
                dp=False
            #if pressed[pygame.K_D]:
            if is_blue: color = (0, 128, 255)
            else: color = (255, 100, 0)
            #pygame.draw.rect(screen, color, pygame.Rect(x, y, 25, 25))
            screen.blit(get_image('face.jpg'), pygame.Rect(x, y, 40,40))
            if rp==True:
                screen.blit(get_image('cornright.jpg'), (x+50, y+20))
                screen.blit(get_image('face.jpg'), (x, y))
            if lp==True:
                screen.blit(get_image('cornleft.jpg'), (x-30, y+20))
                screen.blit(get_image('faceleft.jpg'), (x, y))
            if dp==True:
                screen.blit(get_image('corndown.jpg'), (x+20, y+50))
                screen.blit(get_image('facedown.jpg'), (x, y))
            if up==True:
                screen.blit(get_image('cornup.jpg'), (x+20, y-30))
                screen.blit(get_image('faceup.jpg'), (x, y))
        elif dp==True:
            y=y-2
            screen.blit(get_image('corndown.jpg'), (x+20, y+50))
            screen.blit(get_image('facedown.jpg'), (x, y))
        elif up==True:
            y=y+2
            screen.blit(get_image('cornup.jpg'), (x+20, y-30))
            screen.blit(get_image('faceup.jpg'), (x, y))
        elif rp==True:
            x=x-2
            screen.blit(get_image('cornright.jpg'), (x+50, y+20))
            screen.blit(get_image('face.jpg'), (x, y))
        elif lp==True:
            x=x+2
            screen.blit(get_image('cornleft.jpg'), (x-30, y+20))
            screen.blit(get_image('faceleft.jpg'), (x, y))
        #print (pos)

            
        if pos2 in redpwup and speedcheck==True:
            a2=a2+10
            print("Wall Hacks Powerup Activated")
        if a2>8:
            a2=7
            speedcheck=False
        if pos2 not in coordinates:
            if pressed[pygame.K_UP]:
                if p2y >= 25:
                    p2y -= a2
                up2=True
                rp2=False
                lp2=False
                dp2=False
            if pressed[pygame.K_DOWN]:
                if p2y <= 525:
                    p2y += a2
                rp2=False
                lp2=False
                up2=False
                dp2=True
            if pressed[pygame.K_LEFT]:
                if p2x >=25:
                    p2x -= a2
                rp2=False
                lp2=True
                up2=False
                dp2=False
            if pressed[pygame.K_RIGHT]:
                if p2x <= 725:
                    p2x += a2
                rp2=True
                lp2=False
                up2=False
                dp2=False
            if is_blue: color = (0, 128, 255)
            else: color = (255, 100, 0)
            #pygame.draw.rect(screen, color, pygame.Rect(x, y, 25, 25))
            screen.blit(get_image('enemy.jpg'), pygame.Rect(p2x, p2y, 40,40))
            if rp2==True:
                screen.blit(get_image('cornright.jpg'), (p2x+50, p2y+20))
                screen.blit(get_image('enemy.jpg'), (p2x, p2y))
            if lp2==True:
                screen.blit(get_image('cornleft.jpg'), (p2x-30, p2y+20))
                screen.blit(get_image('enemy.jpg'), (p2x, p2y))
            if dp2==True:
                screen.blit(get_image('corndown.jpg'), (p2x+20, p2y+50))
                screen.blit(get_image('enemydown.jpg'), (p2x, p2y))
            if up2==True:
                screen.blit(get_image('cornup.jpg'), (p2x+20, p2y-30))
                screen.blit(get_image('enemyup.jpg'), (p2x, p2y))
        elif dp2==True:
            p2y=p2y-2
            screen.blit(get_image('corndown.jpg'), (p2x+20, p2y+50))
            screen.blit(get_image('enemydown.jpg'), (p2x, p2y))
        elif up2==True:
            p2y=p2y+2
            screen.blit(get_image('cornup.jpg'), (p2x+20, p2y-30))
            screen.blit(get_image('enemyup.jpg'), (p2x, p2y))
        elif rp2==True:
            p2x=p2x-2
            screen.blit(get_image('cornright.jpg'), (p2x+50, p2y+20))
            screen.blit(get_image('enemy.jpg'), (p2x, p2y))
        elif lp2==True:
            p2x=p2x+2
            screen.blit(get_image('cornleft.jpg'), (p2x-30, p2y+20))
            screen.blit(get_image('enemy.jpg'), (p2x, p2y))

        if attacktime <20:        
            attacktime =attacktime+1
        #print (attacktime)
        if attacktime==20:
            if x+85>p2x and x+85<p2x+50 and y+20>p2y and y+20 <= p2y+50 and rp==True and pressed[pygame.K_1]:
                player2health=player2health-dmg1
                attacktime=0
            elif x+85>p2x and x+85<p2x+50 and y+30>p2y and y+30 <= p2y+50 and rp==True and pressed[pygame.K_1]:
                player2health=player2health-dmg1
                attacktime=0
                
            elif x-35>p2x and x-35<p2x+50 and y+20>p2y and y+20 <= p2y+50 and lp==True and pressed[pygame.K_1]:
                player2health=player2health-dmg1
                attacktime=0
            elif x-35>p2x and x-35<p2x+50 and y+30>p2y and y+30 <= p2y+50 and lp==True and pressed[pygame.K_1]:
                player2health=player2health-dmg1
                attacktime=0
                
            elif x+20>p2x and x+20<p2x+50 and y+85>p2y and y+85 <= p2y+50 and dp==True and pressed[pygame.K_1]:
                player2health=player2health-dmg1
                attacktime=0
            elif x+30>p2x and x+30<p2x+50 and y+85>p2y and y+85 <= p2y+50 and dp==True and pressed[pygame.K_1]:
                player2health=player2health-dmg1
                attacktime=0
                
            elif x+20>p2x and x+20<p2x+50 and y-35>p2y and y-35 <= p2y+50 and up==True and pressed[pygame.K_1]:
                player2health=player2health-dmg1
                attacktime=0
            elif x+30>p2x and x+30<p2x+50 and y-35>p2y and y-35 <= p2y+50 and up==True and pressed[pygame.K_1]:
                player2health=player2health-dmg1
                attacktime=0
            
        if attacktime2 <20:
            attacktime2 =attacktime2+1
        #print (attacktime2)
            
        if attacktime2==20:
            if p2x+85>x and p2x+85<x+50 and p2y+20>y and p2y+20 <= y+50 and rp2==True and pressed[pygame.K_SLASH]:
                player1health=player1health-dmg2
                attacktime2=0
            elif p2x+85>x and p2x+85<x+50 and p2y+30>y and p2y+30 <= y+50 and rp2==True and pressed[pygame.K_SLASH]:
                player1health=player1health-dmg2
                attacktime2=0
                
            elif p2x-35>x and p2x-35<x+50 and p2y+20>y and p2y+20 <= y+50 and lp2==True and pressed[pygame.K_SLASH]:
                player1health=player1health-dmg2
                attacktime2=0
            elif p2x-35>x and p2x-35<x+50 and p2y+30>y and p2y+30 <= y+50 and lp2==True and pressed[pygame.K_SLASH]:
                player1health=player1health-dmg2
                attacktime2=0
                
            elif p2x+20>x and p2x+20<x+50 and p2y+85>y and p2y+85 <= y+50 and dp2==True and pressed[pygame.K_SLASH]:
                player1health=player1health-dmg2
                attacktime2=0
            elif p2x+30>x and p2x+30<x+50 and p2y+85>y and p2y+85 <= y+50 and dp2==True and pressed[pygame.K_SLASH]:
                player1health=player1health-dmg2
                attacktime2=0
                
            elif p2x+20>x and p2x+20<x+50 and p2y-35>y and p2y-35 <= y+50 and up2==True and pressed[pygame.K_SLASH]:
                player1health=player1health-dmg2
                attacktime2=0
            elif p2x+30>x and p2x+30<x+50 and p2y-35>y and p2y-35 <= y+50 and up2==True and pressed[pygame.K_SLASH]:
                player1health=player1health-dmg2
                attacktime2=0
                
        if player1health==4:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(125, 575, 25, 25))
        if player1health==3:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(100, 575, 50, 25))
        if player1health==2:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(75, 575, 75, 25))
        if player1health==1:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(50, 575, 100, 25))
        if player1health==0:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(25, 575, 125, 25))

        
        
        if player2health==4:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(650, 575, 25, 25))
        if player2health==3:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(650, 575, 50, 25))
        if player2health==2:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(650, 575, 75, 25))
        if player2health==1:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(650, 575, 100, 25))
        if player2health==0:
            pygame.draw.rect(screen, (38, 38, 38), pygame.Rect(650, 575, 125, 25))
            
        screen.blit(get_image('zach.jpg'), pygame.Rect(enemyx, enemyy, 40,40))
        if q<=35:
            enemyx=enemyx+4
            q=q+0.5
        elif q==72:
            q=0
        elif q>35:
            enemyx=enemyx-4
            q=q+0.5
        screen.blit(get_image('zach.jpg'), pygame.Rect(enemy2x, enemy2y, 40,40))
        if s<=35:
            enemy2x=enemy2x-4
            s=s+0.5
        elif q==72:
            s=0
        elif s>35:
            enemy2x=enemy2x+4
            s=s+0.5
            
        if player1dmg==True:    
            if enemyx>x and enemyx<x+50 and enemyy>y and enemyy <= y+50:
                player1health=player1health-1
                player1dmg=False
            elif enemyx+50>x and enemyx+50<x+50 and enemyy>y and enemyy <= y+50:
                player1health=player1health-1
                player1dmg=False
            elif enemyx+50>x and enemyx+50<x+50 and enemyy+50>y and enemyy+50 <= y+50:
                player1health=player1health-1
                player1dmg=False
            elif enemyx>x and enemyx<x+50 and enemyy+50>y and enemyy+50 <= y+50:
                player1health=player1health-1
                player1dmg=False
                
            elif enemyx>p2x and enemyx<p2x+50 and enemyy>p2y and enemyy <= p2y+50:
                player2health=player2health-1
                player1dmg=False
            elif enemyx+50>p2x and enemyx+50<p2x+50 and enemyy>p2y and enemyy <= p2y+50:
                player2health=player2health-1
                player1dmg=False
            elif enemyx+50>p2x and enemyx+50<p2x+50 and enemyy+50>p2y and enemyy+50 <= p2y+50:
                player2health=player2health-1
                player1dmg=False
            elif enemyx>p2x and enemyx<p2x+50 and enemyy+50>p2y and enemyy+50 <= p2y+50:
                player2health=player2health-1
                player1dmg=False
                
        if player2health>=0 and player2dmg==True:
            if enemy2x>x and enemy2x<x+50 and enemy2y>y and enemy2y <= y+50:
                player1health=player1health-1
                player2dmg=False
            elif enemy2x+50>x and enemy2x+50<x+50 and enemy2y>y and enemy2y <= y+50:
                player1health=player1health-1
                player2dmg=False
            elif enemy2x+50>x and enemy2x+50<x+50 and enemy2y+50>y and enemy2y+50 <= y+50:
                player1health=player1health-1
                player2dmg=False
            elif enemy2x>x and enemy2x<x+50 and enemy2y+50>y and enemy2y+50 <= y+50:
                player1health=player1health-1
                player2dmg=False
                
            elif enemy2x>p2x and enemy2x<p2x+50 and enemy2y>p2y and enemy2y <= p2y+50:
                player2health=player2health-1
                player2dmg=False
            elif enemy2x+50>p2x and enemy2x+50<p2x+50 and enemy2y>p2y and enemy2y <= p2y+50:
                player2health=player2health-1
                player2dmg=False
            elif enemy2x+50>p2x and enemy2x+50<p2x+50 and enemy2y+50>p2y and enemy2y+50 <= p2y+50:
                player2health=player2health-1
                player2dmg=False
            elif enemy2x>p2x and enemy2x<p2x+50 and enemy2y+50>p2y and enemy2y+50 <= p2y+50:
                player2health=player2health-1
                player2dmg=False
        if player2health==0:
            print ("Player 1 wins")
            screen.blit(get_image('lose.jpg'), (150, 150))
        if player1health==0:
            print ("Player 2 wins")
            screen.blit(get_image('lose.jpg'), (150, 150))
        pos=poslast
        clock.tick(120)
        pygame.display.flip()
        


