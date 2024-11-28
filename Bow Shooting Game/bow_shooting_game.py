#working title 'Bow Shooting Game' by Karpo

import pygame
from random import randint

pygame.init()


# Basic stuff with game launch
background = pygame.transform.flip(pygame.image.load(r"images\working_title_bg.jpg"),True,False)

# importing characters images
default_player_resolution = (130,130)
default_player_img_scaled = pygame.transform.flip(pygame.transform.scale(pygame.image.load(r"images\working_title_player.png"),default_player_resolution),True,False)

small_snail_resolution = (125,125)
small_snail_mob_img_scaled = pygame.transform.scale(pygame.image.load(r"images\working_title_small_snail.png"),small_snail_resolution)

red_snail_resolution = (148,1000)
red_snail_mob_img_scaled = pygame.transform.scale(pygame.image.load(r"images\working_title_red_snail.png"), red_snail_resolution)

blue_snail_resolution = (100,100)
blue_snail_mob_img_scaled = pygame.transform.scale(pygame.image.load(r"images\working_title_blue_snail.png"), blue_snail_resolution)

mushroom_resolution = (100,100)
mushroom_mob_img_scaled = pygame.transform.scale(pygame.image.load(r"images\working_title_mushroom_mob.png"),mushroom_resolution)


# importing objectile
default_arrow_sprite = pygame.image.load(r"images\working_title_arrow.png")
default_arrow_sprite_scaled = default_arrow_sprite

# setting the window's resolution
width = 1200
height = 800

# setting colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

myWindow = pygame.display.set_mode((width,height))
# setting the game's window caption
pygame.display.set_caption ("Bow Shooting Game")

clock = pygame.time.Clock()
# setting up keys list
keys = pygame.key.get_pressed()

def draw_game_window():
    # drawing background ingame
    myWindow.blit(background, (0,0))
    # drawing the player
    player.draw(myWindow)

    mobs.draw(myWindow)
    for mob in mobs.mobs_list:
        mob.move()
    
    #showing score
    score_text = font.render(f"Score: {str(game.score)}", 1, BLACK)
    myWindow.blit(score_text,(10,10))
    
    pygame.display.update()
    
class Game:
    def __init__(self):
        self.score = 0
    
    def main_menu(self):
        pass
    
    def options_menu(self):
        pass
    
    def update_score(self,add_decrease, damage):
        if add_decrease == "add":
            self.score += damage
        elif add_decrease == "decrease":
            self.score -= damage

class Player(object):
    def __init__(self,skin,skin_res):
        self.skin = skin
        
        self.x_pos = 65
        self.y_pos = 530
        self.hitbox = (self.x_pos,self.y_pos,skin_res[0]-5,skin_res[1]-10)
    
    def draw(self,myWindow):
        myWindow.blit(self.skin,(self.x_pos , self.y_pos))
        pygame.draw.rect(myWindow,RED,self.hitbox,2)
    

class Mobs:
    def __init__(self):
        self.mobs_names = {
        "Small Snail": ("Small Snail",1.2,1,small_snail_mob_img_scaled,small_snail_resolution,930,555),
        "Mushroom": ("Mushroom",2.5,5,mushroom_mob_img_scaled,mushroom_resolution,930,555)
                            }
        self.mobs_list = []
        
    def draw(self,myWindow):
        if len(self.mobs_list) > 0:
            for mob in self.mobs_list:
                myWindow.blit(mob.skin, (mob.x_pos , mob.y_pos))
                #print(type(mob.hitbox))
                pygame.draw.rect(myWindow,RED,mob.hitbox,2)
    
    def spawn_mob(self):
        random_num = randint(0,len(self.mobs_names))
        add = 0
        for name,value in self.mobs_names.items():
            mob_to_add = name
            mobs_value = value
            add += 1
            if add == random_num:
                mob_to_add = Mob(*mobs_value)
                self.mobs_list.append(mob_to_add)
                break
        

class Mob(object):
    def __init__(self,name,velocity,damage,skin,skin_res,x_value,y_value):
        self.name = name
        self.velocity = velocity
        self.damage = damage
        self.skin = skin
        self.x_pos = x_value
        self.y_pos = y_value
        
        self.alive = True
        self.mobs_hitboxes = {
        "Small Snail": (mobs.mobs_names["Small Snail"][4],mobs.mobs_names["Small Snail"][5], small_snail_resolution[0],small_snail_resolution[1]),
        "Mushroom": (mobs.mobs_names["Mushroom"][4],mobs.mobs_names["Mushroom"][5],mushroom_resolution[0],mushroom_resolution[1])
                        }
        #self.hitbox = self.mobs_hitboxes[self.name]
        #self.hitbox = (mobs.mobs_names[self.name][4],mobs.mobs_names[self.name][5],skin_res[0],skin_res[1])
        self.hitbox = (self.x_pos,self.y_pos,skin_res[0],skin_res[1])
    
    # def draw(self,myWindow):
        # if self.alive:
            # drawing the mob on the screen
            # myWindow.blit(self.skin, (self.x_pos , self.y_pos))
            # showing the mob's hitbox
            # pygame.draw.rect(myWindow,RED,self.hitbox,2)
            
            # mushroom.move()
        
    def move(self):
        if self.alive:
            # moving the Mob to the left according to its velocity
            self.x_pos -= self.velocity
            self.hitbox = (self.x_pos,self.y_pos,100,100)
            
            #print(f"this is the mob's hitbox: {self.hitbox[0] + self.hitbox[2]}")
            #print(f"this is the player's hitbox: {player.hitbox[0] + player.hitbox[2]}")
            if self.hitbox[0] <= player.hitbox[0] + player.hitbox[2]:
                self.death()
        
    def death(self):
        print("Death!")
        self.alive = False
        game.update_score("decrease",self.damage)
        mobs.mobs_list.pop(mobs.mobs_list.index(self))
        

class Arrow(object):
    def __init__(self,skin):
        self.skin = skin
        
        self.arrow_x_pos = player.x_pos
        self.arrow_y_pos = player.y_pos
        
        
# setting a font
font = pygame.font.SysFont("comicsans", 50, True)

game = Game()
player = Player(default_player_img_scaled,default_player_resolution)
mobs = Mobs()
arrow = Arrow(default_arrow_sprite_scaled)

x = 0
# main loop
main_loop = True
while main_loop:
    clock.tick(50)
    x += 1
    if x>=50:
        x = 0
    if x == 0:
        mobs.spawn_mob()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False
            
    draw_game_window()
    


pygame.quit()