#Killing Floor tribute game

import arcade
import random
import os

blocksize = 72


myBlocksdict = dict()
myBlocksdict.update ({"cratebox":arcade.load_texture(":resources:images/tiles/boxCrate_double.png")})
myBlocksdict.update ({"lockbox":arcade.load_texture(":resources:images/tiles/lockRed.png")})
myBlocksdict.update ({"grassbox":arcade.load_texture(":resources:images/tiles/grassMid.png")})
myBlocksdict.update ({"spawnhole":arcade.load_texture(":resources:images/tiles/doorClosed_mid.png")})
myBlocksdict.update ({"cactus":arcade.load_texture(":resources:images/tiles/cactus.png")})

myCharsdict = dict()
myCharsdict.update ({"GF":arcade.load_texture(":resources:images/animated_characters/zombie/zombie_idle.png")})
myCharsdict.update ({"mrfoster":arcade.load_texture(":resources:images/animated_characters/robot/robot_idle.png")})


def blockadder_inlines (orgX, orgY, destX, destY, blockType):
    if (orgX==destX):
        start=min(orgY,destY)
        end=max(orgY, destY)
        for i in range(start,end):
            addblock(orgX,i,blockType)
    if (orgY==destY):
        start=min(orgX,destX)
        end=max(orgX, destX)
        for i in range(start,end):
            addblock(i,orgY, blockType)
        
            

def addblock(x,y,blockType):
    arcade.draw_lrwh_rectangle_textured(x*blocksize,y*blocksize,blocksize,blocksize,myBlocksdict.get(blockType))
def addchar (x,y,blockType):
    arcade.draw_lrwh_rectangle_textured(x*blocksize,y*blocksize,blocksize,blocksize,myCharsdict.get(blockType))


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Killing Zeds"

MAIN_MENU0 = 0
OPTIONS_MENU1 = 1
GAME_RUNNING2 = 2
GAME_OVER3 = 3

class myZedGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location (150,100)
        arcade.set_background_color(arcade.color.WHEAT)
        self.list_of_zeds=None
        self.foster = None
        self.bullet_list=None
        self.weapon_list=None
        self.frame_count=0
        self.headShotCharge=0
        self.kill_score=0
        self.zeds_that_are_spawning=58
        
        
        
    def on_draw(self):
        arcade.start_render()
    
        blockadder_inlines(1,2,1,8,"cratebox")
        blockadder_inlines(1,8,17,8,"cratebox")
        blockadder_inlines(16,2,16,9,"cratebox")
        blockadder_inlines(1,2,17,2,"cratebox")
        blockadder_inlines(2,4,2,7,"lockbox")
        blockadder_inlines(3,6,15,6,"grassbox")
        blockadder_inlines(3,5,15,5,"grassbox")
        blockadder_inlines(3,4,15,4,"grassbox")
        blockadder_inlines(3,3,15,3,"cactus")
        blockadder_inlines(3,7,15,7,"cactus")
        blockadder_inlines(15,4,15,7,"spawnhole")
        
        self.list_of_zeds.draw() 
        self.foster.draw()
        self.bullet_list.draw()
        self.foster.equippedWeapon.draw()
        
        output = f"Health: {self.foster.HP} "
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 20)
        output = f"Kills: {self.kill_score} "
        arcade.draw_text(output, 13*blocksize, 1*blocksize, arcade.color.BLACK, 14)
        output = f"DOSH: {self.dosh_count} "
        arcade.draw_text(output, 13*blocksize, 0.5*blocksize, arcade.color.BLACK, 14)
        
        if self.syringe_count>=1:
            output = f"Syringe CD: {self.syringe_count} "
            arcade.draw_text(output, 4*blocksize, 9.2*blocksize, arcade.color.BLACK, 25)
        if self.syringe_count<=0:
            output = f"Syringe Charged "
            arcade.draw_text(output, 4*blocksize, 9.2*blocksize, arcade.color.BLACK, 25)
            
        zedsNum=self.zeds_that_are_spawning+len(self.list_of_zeds)
        if zedsNum>0:
            output = f"ZEDS: {int(zedsNum)} "
            arcade.draw_text(output, 1.5*blocksize, 9.2*blocksize, arcade.color.BLACK, 22)   
        if self.trader_minute<10 and zedsNum<=0:
            output = f"00:0{self.trader_minute} "
            arcade.draw_text(output, 1.5*blocksize, 9.2*blocksize, arcade.color.BLACK, 22)
        elif zedsNum<=0:
            output = f"00:{self.trader_minute} "
            arcade.draw_text(output, 1.5*blocksize, 9.2*blocksize, arcade.color.BLACK, 22) 
        
        output = f" {self.wave_number}/10 "
        arcade.draw_text(output, 16*blocksize, 9.2*blocksize, arcade.color.BLACK, 22)
        
        if self.character_weight>=10:
            output = f"{self.character_weight}/15 "
            arcade.draw_text(output, 2.1*blocksize, 20, arcade.color.BLACK, 20)
        elif self.character_weight>=1:
            output = f"0{self.character_weight}/15 "
            arcade.draw_text(output, 2.1*blocksize, 20, arcade.color.BLACK, 20) 
        
        
            
        
        
        
    def setup(self):
        self.list_of_zeds=arcade.SpriteList()
        self.bullet_list=arcade.SpriteList()
        self.weapon_list=arcade.SpriteList()
        
        self.wKeyPressed=False
        self.sKeyPressed=False
        self.headShotCharge=0
        self.kill_score=0
        self.dosh_count=250
        self.dosh_for_headhshot_count=False
        self.syringe_count=0
        self.wave_number=1
        self.trader_minute=20
        self.character_weight=1
        self.syringe_shot_Qpress=False
        
        self.foster=myPlayer()
        self.foster.setVals(100,0.73)
        
        
    def on_update (self,delta_time):
        self.list_of_zeds.update()
        self.bullet_list.update()
        self.weapon_list.update()
        self.foster.update()
        self.frame_count+=1
        

            
        for iZed in self.list_of_zeds:
            #check if clot reached player
            if iZed.center_x<=3.05*blocksize:
                iZed.kill()
                self.foster.HP-=iZed.AP                
                
            #check if bullet and clot colides    
            for iBullet in  self.bullet_list: 
                
                if arcade.check_for_collision(iBullet,iZed)==True:
                    
                    iZed.HP-=iBullet.AP
                    
                    if iZed.HP<=0:
                        iZed.kill()
                        if iBullet.kind=="headshot":
                            self.dosh_count+=random.randrange(0,3)
                        else:
                            self.dosh_count+=random.randrange(4,7)
                        self.kill_score+=1
                        
                    iBullet.kill()
    
    #waves progressing   
        if self.zeds_that_are_spawning==0 and len(self.list_of_zeds)==0:
            
            
            if self.frame_count%60==0:
                self.trader_minute-=1
                
                if self.trader_minute==0:                                                                                       
                    self.wave_number+=1                                                                                    
                    self.zeds_that_are_spawning=((self.wave_number*self.wave_number)*0.6+57.5)//1
                    self.trader_minute=20

                #clots respawn rate
        elif self.zeds_that_are_spawning>0:
            if self.frame_count%30==0:
                clot=myZed()
                clot.setVals(1,random.randrange(10,13),4,0)
                self.list_of_zeds.append(clot)
                self.zeds_that_are_spawning-=1
            
        
            #gorefasts respawn rate    
            if self.frame_count%65==0:
                gorefast=myZed()
                gorefast.setVals(2,random.randrange(14,17),7,1)
                self.list_of_zeds.append(gorefast)
                self.zeds_that_are_spawning-=1
        

                
        #if headshot-charge is not used within the next 69 frames then lose the charge
        if self.headShotCharge>=1:
            if self.headShotCharge>=1:
                self.headShotCharge=1
            if self.frame_count%69==0:
                self.headShotCharge=0
                        
                    
        
        #syringe-shot Cooldown reset
        if self.syringe_count<=0:
            self.syringe_count=0

        if (self.frame_count%60==0):
            self.syringe_count-=1
        if self.syringe_shot_Qpress<=0:
            self.syringe_shot_Qpress = False
        
                
        #foster's death
        if self.foster.HP<=0:
            self.foster.kill()
            self.syringe_shot_Qpress=True
            arcade.MOUSE_BUTTON_LEFT = None
            
        if self.foster.HP<=0:
            self.foster.HP=0
        if self.foster.HP>=100:
            self.foster.HP=100
        

          
            
            
    def on_key_press (self, key, modifiers):      
            
        #moving the player up and down    
        if key == arcade.key.W:
            self.wKeyPressed=True
        if key == arcade.key.S:
            self.sKeyPressed=True
            
        if key == arcade.key.SPACE and self.wKeyPressed==True and self.foster.laneNum<=1:
            self.foster.laneNum+=1
        if key == arcade.key.SPACE and self.sKeyPressed==True and self.foster.laneNum>0:
            self.foster.laneNum-=1
            
            
        #pressing Q=healing syringe activated    
        if key == arcade.key.Q and self.syringe_shot_Qpress==False and self.foster.HP<=99 and self.syringe_count<1:
            self.foster.HP+=50
            self.syringe_count=10
            
            
    #Weapon Switch    
        
        #knife
        if key == arcade.key.KEY_1:
            self.foster.equip("knife")
            
        #M9_handgun    
        if key == arcade.key.KEY_2:
            self.foster.equip("M9_handgun")
        

                
       
    def on_key_release (self, key, modifiers):
        
        if key == arcade.key.W:
            self.wKeyPressed=False
        if key == arcade.key.S:
            self.sKeyPressed=False
    
    def on_mouse_press(self,x,y,button,modifiers):
   
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.headShotCharge+=1
        print (self.headShotCharge)
#
#        if button == arcade.MOUSE_BUTTON_LEFT and self.headShotCharge>=1:
#            headshot=myBullet()
#            headshot.setVals(self.foster,"headshot")
#            self.bullet_list.append(headshot)
#            self.headShotCharge=0
#            
#        elif button == arcade.MOUSE_BUTTON_LEFT:# and self.weapon=="M9_handgun":
#            bullet=myBullet()
#            bullet.setVals(self.foster,"bullet")
#            self.bullet_list.append(bullet)
#            self.headShotCharge=0
#"""
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.foster.attack(self)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.foster.specialAttack(self)
        

class myZed(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.textures=[]
        self.append_texture(arcade.load_texture("Skins\Clot.png", mirrored=True))
        self.append_texture(arcade.load_texture("Skins\GF.png"))
        self.set_texture(0)

    def setVals(self,HP,AP,speed,kindOFZED):
        self.HP = HP
        self.AP=AP
        laneNum=random.randrange(0,3)
        self.center_y = (4.58+laneNum)*blocksize
        self.center_x = 15.5*blocksize
        self.scale=0.137
        self.change_x=-speed
        if kindOFZED==0:
            self.set_texture(0)
        if kindOFZED==1:
            self.set_texture(1)
            self.scale = 0.3
            self.center_y =(4.55+laneNum)*blocksize
        
        
    def update (self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y        
        
        
    
class myPlayer (arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.textures=[]
        self.append_texture(arcade.load_texture("Skins\Mr.Foster.png",))
        self.set_texture(0)
        
    def setVals(self,HP,laneNum):
        self.HP=HP
        self.laneNum=laneNum
        self.center_y = (8+laneNum)*blocksize
        self.center_x = 2.5*blocksize
        self.scale = 0.20
        
        self.weapon_list=arcade.SpriteList()
        weapon=myWeapon()
        weapon.setVals("knife")
        self.weapon_list.append(weapon)
        weapon=myWeapon()
        weapon.setVals("M9_handgun")
        self.weapon_list.append(weapon)
        
        self.equippedWeapon=self.weapon_list[1]
        ###############
    def update (self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        self.center_y = (4.67+self.laneNum)*blocksize
        
        if self.equippedWeapon==self.weapon_list[0]:
            self.equippedWeapon.center_x=self.center_x+26
            self.equippedWeapon.center_y=self.center_y+37
        
        if self.equippedWeapon==self.weapon_list[1]:
            self.equippedWeapon.center_x=self.center_x+4.1
            self.equippedWeapon.center_y=self.center_y+8.9
            
        

        
    def equip(self,weaponName):
        if weaponName=="knife":
            self.equippedWeapon=self.weapon_list[0]
        if weaponName=="M9_handgun":
            self.equippedWeapon=self.weapon_list[1]
            
    def attack(self,game):
        if self.equippedWeapon.kind=="M9_handgun":
            if game.headShotCharge>=1:
                headshot=myBullet()
                headshot.setVals(self,"headshot")
                game.bullet_list.append(headshot)

            else:
                bullet=myBullet()
                bullet.setVals(self,"bullet")
                game.bullet_list.append(bullet)
    #def specialAttack(self,game):
        
        
        
class myBullet (arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.textures=[]
        self.append_texture(arcade.load_texture("Skins\headshotbullet.png"))
        self.append_texture(arcade.load_texture("Skins\GF.png"))
        self.set_texture(0)
            
    def setVals(self,shooter,kind):
        self.center_x = (shooter.center_x+50)
        self.center_y = (shooter.center_y+25)
        self.kind=kind
        if kind=="bullet":
            self.set_texture(0)
            self.AP=1
            self.change_x=40
            self.scale = 0.15
            
        if kind=="headshot":
            self.set_texture(1)
            self.AP=4
            self.change_x=42
            self.scale = 0.10
        
    
    def update (self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y    
        
        
class myWeapon (arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.textures=[]
        self.append_texture(arcade.load_texture("Skins\knife.png", mirrored=True))
        self.append_texture(arcade.load_texture("Skins\M9.png"))
        self.set_texture(0)
        
    def setVals(self,kind):
        self.kind=kind
        if kind=="knife":
            self.set_texture(0)
            #self.center_x = (shooter.center_x+50)
            #self.center_y = (shooter.center_y+25)
            self.scale=0.17
            self.ammo=50
            self.AP=1
        if kind=="M9_handgun":
            self.set_texture(1)
            #self.center_x = (shooter.center_x+50)
            #self.center_y = (shooter.center_y+25)
            self.scale=0.20
            self.AP=1
            self.ammo=49
            
    def update (self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y 
            
        
        
def draw_game_over(self):
    output = "YOU DID NOT SURVIVE"
    arcade.draw_text(output, 240, 400, arcade.color.BLACK, 54)
    
    output = "PRESS 'R' TO TRY AGAIN"
    arcade.draw_text(output, 310, 300, arcade.color.BLACK, 24)
    


game = myZedGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
