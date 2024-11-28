#Polar Trials/Polar game in the making by Karpo
import pygame
import random
pygame.init()

myWindow = pygame.display.set_mode ((1280,720))
myWindowWidth = 1280
myWindowHeight = 720

pygame.display.set_caption("POLAR")
bg = pygame.image.load("bg.png")



clock = pygame.time.Clock()



class polarPlayer(object):


    #walking animation images of polar
    walkLeftAnimation = []
    walkRightAnimation = []
    attackLeftAnimation = []
    attackRightAnimation = []
    dirWalking = "Characters-Sprites_folder\Polar\polar{}L.png"
    dirAttacking = "Characters-Sprites_folder\Polar\polarAttack{}L.png"
    
    #walking animation
    for i in range (1,5):
        
        #left
        curImg = pygame.image.load(dirWalking.format(i))
        curScaledImg = pygame.transform.scale(curImg,(145,145))
        walkLeftAnimation.append(curScaledImg)

        #right
        curImg = pygame.image.load(dirWalking.format(i))
        curScaledImg = pygame.transform.flip(pygame.transform.scale(curImg,(145,145)),True,False)
        walkRightAnimation.append(curScaledImg)
        
    #Attacking animation    
    for i in range (1,4):
    
        #left
        curImg = pygame.image.load(dirAttacking.format(i))
        curScaledImg = pygame.transform.scale(curImg,(145,145))
        attackLeftAnimation.append(curScaledImg)
        
        #right
        curImg = pygame.image.load(dirAttacking.format(i))
        curScaledImg = pygame.transform.flip(pygame.transform.scale(curImg,(145,145)),True,False)
        attackRightAnimation.append(curScaledImg)
    
    killScore = 0
    XP = 0
    

    def __init__(self,x,y,width,height,HP):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.HP = HP
        self.velocity = 5
        self.walkCount = 0
        self.attackCount = 0
        self.standing = True
        self.left = False
        self.right = False
        self.rollingatm = False
        #self.rollCount = 0
        self.alive = True
        self.hitbox = (self.x + 17, self.y + 5, 28, 91)
        
    def draw(self,myWindow):
    
        
        #player animation
        if self.alive:
            if self.walkCount>=len(self.walkLeftAnimation) *3 or self.walkCount>=len(self.walkRightAnimation) *3:
                self.walkCount=0
                
            #if self.rollCount>=9:
                #self.rollCount=0
                
            if not (self.standing):
            
                #animation of running left
                if self.left:
                    myWindow.blit(self.walkLeftAnimation[self.walkCount //3], (self.x, self.y))
                    self.walkCount += 1
                    
                #animation of running right
                elif self.right:
                    myWindow.blit(self.walkRightAnimation[self.walkCount //3], (self.x, self.y))
                    self.walkCount += 1
            else:
                #heading left
                if self.left:
                    myWindow.blit(self.walkLeftAnimation[0],(self.x,self.y))
                #heading right
                else:
                    myWindow.blit(self.walkRightAnimation[0],(self.x,self.y))
                    
        elif self.alive and axeWeapon.attackClick:
            if self.attackCount>=len(self.attackLeftAnimation) *3 or self.attackCount>=len(self.attackRightAnimation) *3:
                self.attackCount=0
                
            if self.left:
                myWindow.blit(self.attackLeftAnimation[self.attackCount //3], (self.x, self.y))
                self.attackCount += 1
            
            elif self.right:
                myWindow.blit(self.attackRightAnimation[self.attackCount //3], (self.x, self.y))
                self.attackCount += 1
                    



            #hitbox of player
            self.hitbox = (self.x + 54, self.y + 5, 35, 100)
            
            #showing the hitbox on screen
            #pygame.draw.rect (myWindow ,(255,0,0), self.hitbox,2)
            
                
    def hitFromMob(self):
        
        self.HP -= axeWeaponENEMY.DMG
        print("Ouch!")
        if self.HP<=0:
            self.alive = False


            

        
        
class polarWeapons(object):

    #animation images of weapon
    axeSwingAnimationLeft = []
    axeSwingAnimationRight = []
    axeStandingAnimationLeft = []
    axeStandingAnimationRight = []
    
    diraxeattack="Characters-Sprites_folder\Polar\\AxeAttack{}L.png"
    diraxestanding="Characters-Sprites_folder\Polar\\AxeStanding{}L.png"
    
    for i in range(1,4):
    
        #left
        curImg = pygame.image.load(diraxeattack.format(i))
        curScaledImg = pygame.transform.scale(curImg,(145,145))
        axeStandingAnimationLeft.append(curScaledImg)
        
        #right
        curImg = pygame.image.load(diraxeattack.format(i))
        curScaledImg = pygame.transform.flip(pygame.transform.scale(curImg,(145,145)), True,False)
        axeSwingAnimationRight.append(curScaledImg)
    
    #standing
    for i in range (1,2):
        
        #left
        curImg = pygame.image.load(diraxestanding.format(i))
        curScaledImg = pygame.transform.scale(curImg,(145,145))
        axeStandingAnimationLeft.append(curScaledImg)
        
        #right
        curImg = pygame.image.load(diraxestanding.format(i))
        curScaledImg = pygame.transform.flip(pygame.transform.scale(curImg,(145,145)),True,False)
        axeStandingAnimationRight.append(curScaledImg)
    
    def __init__(self,x,y,width,height,DMG): #,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.DMG = DMG
        #self.speed = speed
        self.weaponCount = 0
        self.standingCount = 0
        self.attackClick = False
        self.hitbox = (self.x + 12, self.y + 5, 29, 31)
        self.hitboxSide = 0
        self.alive = True
        self.collision = False
        
        
    def draw(self,myWindow):
    
        
        self.x = polar.x + 0
        self.y = polar.y + 0
        

        #weapon swing
        if polar.alive and self.alive:
        
            
            if  self.weaponCount>=len(self.axeSwingAnimationLeft *3) or self.weaponCount>=len(self.axeSwingAnimationRight *3):
                self.weaponCount=0
                self.attackClick=False
                
            
            #swing left
            if self.attackClick and polar.left:
                myWindow.blit(self.axeSwingAnimationLeft[self.weaponCount //3], (self.x - 0, self.y))
                self.weaponCount += 1
                self.hitboxSide = 1
                
            #swing right
            elif self.attackClick and polar.right:
                myWindow.blit(self.axeSwingAnimationRight[self.weaponCount //3], (self.x, self.y))
                self.weaponCount += 1
                self.hitboxSide = 0
                
                
            #weapon changing sides according to player
            else:
                
                if self.standingCount>=len(self.axeStandingAnimationLeft) *1 or self.standingCount>= len(self.axeStandingAnimationRight) *1 :
                    self.standingCount=0
                
                #weapon heading left
                if polar.left:
                    myWindow.blit(self.axeStandingAnimationLeft[self.standingCount//1], (self.x, self.y))
                #weapon heading right
                else:
                    myWindow.blit(self.axeStandingAnimationRight[self.standingCount//1], (self.x, self.y))
        
            
            
            
        #hitbox of player
        #right side
        if self.hitboxSide == 0:
            self.hitbox = (self.x + 36, self.y + 25, 50, 50)
        #left side
        if self.hitboxSide == 1:
            self.hitbox = (self.x + 36-105, self.y + 25, 50, 50)
            
        #showing the hitbox on screen
        #pygame.draw.rect (myWindow ,(255,0,0), self.hitbox,2)
            
            
            
    def hit(self):

        pass
        
        
        
class enemyMobs(object):

    #walking animation images of enemy
    walkLeftAnimation = []
    walkRightAnimation = []
    dirWalking = "Characters-Sprites_folder\garbage\POLAR\L{}.png"
    
    for i in range (1,4):
        walkLeftAnimation.append(pygame.image.load(dirWalking.format(i)))
        walkRightAnimation.append(pygame.transform.flip(pygame.image.load(dirWalking.format(i)),True,False))
        
        
    spawn_rate = 0

    
    def __init__(self,x,y,width,height,DMG,HP):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height
        self.DMG = DMG
        self.HP = HP
        self.velocity = 5
        self.walkCount = 0
        self.left = True
        self.right = False
        self.hitbox = (self.x + 17, self.y + 5, 28, 91)
        self.alive = True

        
        
    def draw(self,myWindow):
        self.move()
        
        if self.alive:
        
            if self.walkCount + 1 >= len(self.walkLeftAnimation) *3:
                self.walkCount=0
            
            if self.left:
                
                myWindow.blit(self.walkLeftAnimation[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
                
            elif self.right:

                myWindow.blit(self.walkRightAnimation[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
                    
            #hitbox of enemy
            self.hitbox = (self.x + 17, self.y + 5, 28, 91)
            
            #showing the hitbox on screen
            pygame.draw.rect (myWindow ,(255,0,0), self.hitbox,2)
        pygame.display.update()
            
    def move(self):
    
        self.x -= self.velocity
        
        #turning right
        if self.x <= 0:
            self.left = False
            self.right = True
            self.velocity *= -1
        #turning left
        elif self.x >= myWindowWidth - self.width + self.velocity: #+ mob.velocity:
            self.left=True
            self.right=False
            self.velocity *= -1
            
        
        
    def hitFromPlayer(self):
        self.HP -= axeWeapon.DMG
        self.x += 150
        if self.HP <=0:
            mob_list.pop(mob_list.index(mob))
            self.alive = False
            polar.killScore += 1
            polar.XP += random.randrange(34,39)

            
            
            
    def spawn(self):
        
        mob = enemyMobs(1200,610,64,64,DMG=1,HP=10)
        mob_list.append(mob)
        enemyWeps_list.append(axeWeaponENEMY)
        

        
class enemiesWeapons(object):
    
    #animation images of weapon
    axeSwingAnimationRight = []
    axeSwingAnimationLeft = []
    diraxeE="Characters-Sprites_folder\WEAPONS\enemiesweapons\\axe{}E.png"
    for i in range(1,7):
        axeSwingAnimationRight.append(pygame.image.load(diraxeE.format(i)))
        axeSwingAnimationLeft.append(pygame.transform.flip(pygame.image.load(diraxeE.format(i)), True, False))
        
        
    enemyWepTimer = 0
       
    def __init__(self,x,y,width,height,DMG): #,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.DMG = DMG
        #self.speed = speed
        self.weaponCount = 0
        self.attackPlayer = False
        self.hitbox = (self.x + 12, self.y + 5, 29, 31)
        self.hitboxSide = 0
        self.alive = True
        self.collision = False
    
    def draw(self,myWindow):
    
        
        self.x = mob.x + 25
        self.y = mob.y + -20
        

        #weapon swing
        if mob.alive and self.alive:
        
            
            if self.weaponCount>=len(self.axeSwingAnimationRight * 3):
                self.weaponCount=0
                self.attackPlayer=False
                
            if self.attackPlayer and mob.right:
                myWindow.blit(self.axeSwingAnimationRight[self.weaponCount //3], (self.x, self.y))
                self.weaponCount += 1
                self.hitboxSide = 0
                
            elif self.attackPlayer and mob.left:
                myWindow.blit(self.axeSwingAnimationLeft[self.weaponCount //3], (self.x - 75, self.y))
                self.weaponCount += 1
                self.hitboxSide = 1
                
            #weapon changing sides according to player
            else:
                
                #weapon heading left
                if mob.left:
                    myWindow.blit(self.axeSwingAnimationLeft[0], (self.x - 75, self.y))
                #weapon heading right
                else:
                    myWindow.blit(self.axeSwingAnimationRight[0], (self.x, self.y))
        
            
            
            
        #hitbox of player
        #right side
        if self.hitboxSide == 0:
            self.hitbox = (self.x + 36, self.y + 25, 50, 50)
        #left side
        if self.hitboxSide == 1:
            self.hitbox = (self.x + 36-105, self.y + 25, 50, 50)
            
        #showing the hitbox on screen
        pygame.draw.rect (myWindow ,(255,0,0), self.hitbox,2)
        
    def hit(self):

        if axeWeaponENEMY.enemyWepTimer > 0:
            axeWeaponENEMY.attackPlayer=False
            axeWeaponENEMY.enemyWepTimer += 1
        if axeWeaponENEMY.enemyWepTimer>=42:
            axeWeaponENEMY.enemyWepTimer=0  
            
            

def redrawGameWindow():
    myWindow.blit(bg, (0,0))
    #killscore and XP output
    textKillScore = font.render("Kills:  " + str(polar.killScore), 1, (0,0,0))
    textXP = font.render("XP:  " + str(polar.XP), 1, (0,0,0))
    textHP = font.render("HP:  " + str(polar.HP), 1 , (0,0,0))
    textDEAD = font.render("Polar Is Dead",1,(0,0,0))
    myWindow.blit (textKillScore, (10,10))
    myWindow.blit (textXP,(1150,10))
    if polar.alive:
        myWindow.blit (textHP, (10,30))
    else:
        myWindow.blit(textDEAD,(10,30))
    
    #display of sprites
    polar.draw(myWindow)
    axeWeapon.draw(myWindow)
    for mob in mob_list:
        mob.draw(myWindow)
        for axeWeaponENEMY in enemyWeps_list:
            axeWeaponENEMY.draw(myWindow)

    
    pygame.display.update()







#MAIN LOOP
#setting a font
font = pygame.font.SysFont("comicsans", 30, True)

polar = polarPlayer(300,570,32,32,HP=100)
mob = enemyMobs(1200,610,64,64,DMG=1,HP=10)
mob_list = []
enemyWeps_list = []
axeWeapon = polarWeapons(polar.x + 10, polar.y + 10, 32,32,DMG=7)
axeWeaponENEMY = enemiesWeapons(mob.x + 10, mob.y + 10,90,90,DMG=1)

run = True

while run:

    clock.tick(50)
    print (axeWeapon.weaponCount)
    

    
    
            
    #spawn of mobs
    
    mob.spawn_rate += 1
    if mob.spawn_rate >=100 and len(mob_list) <3:
        mob.spawn()
        mob.spawn_rate=0
    
    
    
    #quit using the X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            

    #mouse & keyboard press variables
    keys = pygame.key.get_pressed()
    keys_mouse = pygame.mouse.get_pressed()



    #directions and wall blocks
    
    #GO LEFT
    if keys[pygame.K_a] and polar.x > polar.velocity:
        polar.x -= polar.velocity
        polar.left = True
        polar.right = False
        polar.standing = False
        polar.rollingatm = False

    #GO RIGHT
    elif keys[pygame.K_d] and polar.x < myWindowWidth - polar.width - polar.velocity:
        polar.x += polar.velocity
        polar.left = False
        polar.right = True
        polar.standing = False
        polar.rollingatm = False

            
    #Standing
    else:
        polar.standing = True
        polar.walkCount = 0
        
        
    #Rollover/dodge
    #if polar.rollingatm==False:
        #if keys[pygame.K_SPACE]:
            #axeWeapon.weaponCount=0
            #polar.rollingatm=True
            
            #if polar.right:
                ##polar.right=False
                #if polar.rollCount < 9:
                    #polar.x += polar.velocity*2.5
                    #polar.rollCount += 1
                    
            #elif polar.left:
                ##polar.left = False
                #if polar.rollCount < 9:
                    #polar.x -= polar.velocity*2.5
                    #polar.rollCount += 1
                
            #else:
                #if polar.rollCount>= 9:
                    #polar.rollingatm = False
        
        
    #Attacking with mouse
    if keys_mouse[0] and axeWeapon.weaponCount==0:
        
        
        axeWeapon.attackClick = True
        axeWeapon.draw(myWindow)

    #collision of weapons with enemies
    for mob in mob_list:
        if polar.alive and mob.alive: 
            if axeWeapon.attackClick:
                if axeWeapon.hitbox[0] + axeWeapon.hitbox[2] >= mob.hitbox[0] + mob.hitbox[2]:
                
                    axeWeapon.collision = True

                    if axeWeapon.collision:
                        axeWeapon.hit()
                        mob.hitFromPlayer()
                        axeWeapon.collision=False
                    

                
                
    #collision of player with enemies
    for mob in mob_list:
        if polar.alive and mob.alive: 
            if polar.hitbox[1] < axeWeaponENEMY.hitbox[1] + axeWeaponENEMY.hitbox[3] and polar.hitbox[1] + polar.hitbox[3] > axeWeaponENEMY.hitbox[1]:
                if polar.hitbox[0] + polar.hitbox[2] > axeWeaponENEMY.hitbox[0] and polar.hitbox[0] < axeWeaponENEMY.hitbox[0] + axeWeaponENEMY.hitbox[2]:
                    if axeWeaponENEMY.enemyWepTimer==0:
                        axeWeaponENEMY.attackPlayer=True
                        polar.hitFromMob()
                        axeWeaponENEMY.enemyWepTimer += 1
                    #else: 
    axeWeaponENEMY.hit()
                    











    redrawGameWindow()




pygame.quit()