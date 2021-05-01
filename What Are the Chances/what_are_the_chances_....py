# 'What Are the Chances...' game by Karpo

from random import randint
import pygame
import csv

pygame.init()

# setting the width and the height resolution of the game
WIDTH,HEIGHT = 1280,720

# RGB colors
BLACK = (0,0,0)
BROWN = (139,69,19)
CHOCOLATE = (210,105,30)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
DARKER_RED = (153,0,0)
YELLOW = (255,255,0)
BACKGROUNDCOLOR = CHOCOLATE

# displaying the game window using the WIDTH and HEIGHT variables
win = pygame.display.set_mode((WIDTH, HEIGHT))

# setting the window's name
pygame.display.set_caption("What Are the Chances...")

# setting the frames clock variable
clock = pygame.time.Clock()

# initializing pygame's mixer
# pygame.mixer.music.load("")
# pygame.mixer.music.play()

# setting the FPS
FPS = 60

# setting up keys list
keys = pygame.key.get_pressed()

# loading images
check_mark_image = pygame.transform.scale(pygame.image.load(r"Stuff\checkmark.png"), (150,150))
wrong_mark_image = pygame.transform.scale(pygame.image.load(r"Stuff\WRONG.png"), (125,125))

# achievments file path
achievements_file_path = r'Stuff\Achievements.csv'

# setting a font
font = pygame.font.SysFont("comicsans", 100, True)

# The WIDTH and HEIGHT of Buttons
BUTTON_WIDTH = 225
BUTTON_HEIGHT = 62.5

# the WIDTH and HEIGHT of the ROLL button
ROLL_BUTTON_WIDTH = 250
ROLL_BUTTON_HEIGHT = 125

# setting a variable to distinguish the space between buttons
SPACE_BETWEEN_BUTTONS = 105

# The X of the buttons for the center of the screen
X_CENTER_OF_SCREEN = WIDTH / 2 - (BUTTON_WIDTH/2)

# The Y of the buttons for the center of the screen
Y_CENTER_OF_SCREEN = HEIGHT / 2 - (BUTTON_HEIGHT/2)

# the game's credits
CREDITS = "Credits:", "This game was made by Karpo", "Music by Karpo"


# creating the Button class
class Button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        
    # Call this method to draw a button on the screen
    def draw(self, win, outline=None):
        # if there's a 'request' for an outline it will create it
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        # drawing the button itself
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        # if there's text to write
        if self.text != "":
            # setting a font
            font = pygame.font.SysFont("comicsans", 40, True)
            text = font.render(self.text, 1, BLACK)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos):
        # pos is a mouse position / a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def draw_game_window():
    # drawing background ingame
    win.fill(BACKGROUNDCOLOR)
    
    if main_menu:
        text = font.render("What Are The Chances...", 1, GREEN)
        win.blit(text, (X_CENTER_OF_SCREEN-350, 71))
        
        for button in main_menu_buttons_list:
            button.draw(win, BLACK)
            
    if game_started_menu:
        roll_button.draw(win, BLACK)
            
        MARKS_X = 1100
        MARKS_Y = HEIGHT-200
        
        # if the user got it right: it will show the check_mark image and the amount of times he got it right in a row
        if right_or_wrong:
            win.blit(check_mark_image, (MARKS_X, MARKS_Y))
            win.blit(font.render(f"X{how_much_in_a_row}", 1, BLACK), (MARKS_X-110, MARKS_Y+70))
            
            
        # if the user got it wrong: it will show the wrong_mark image and will reset the amount of times the user got it right in a row
        elif right_or_wrong == False:
            win.blit(wrong_mark_image, (MARKS_X, MARKS_Y))
            
    if you_win_menu:
        text = font.render("YOU WIN!!!", 1, BLACK)
        win.blit(text, (X_CENTER_OF_SCREEN-100, Y_CENTER_OF_SCREEN))
        
    if achievements_menu:
        font_achievements = pygame.font.SysFont("comicsans", 50, True)
        dist_y = 85
        for row in achievements_list:
            text = font_achievements.render((f"{row[0]}: {row[1]}"), 1, BLACK)
            win.blit(text, (X_CENTER_OF_SCREEN-100, dist_y))
            dist_y += 50
        
    if credits_menu:
        x = X_CENTER_OF_SCREEN
        y = Y_CENTER_OF_SCREEN-200
        
        font2 = pygame.font.SysFont("comicsans", 50, True)
        for i in range(len(CREDITS)):
            if i == 1:
                x -= 215
                y += 169
            text = font2.render(CREDITS[i], 1, BLACK)
            win.blit(text, (x, y+i*40))
    
    # if it's not on main menu it shows the back to main menu button            
    if not main_menu:
        back_to_main_menu_button.draw(win, BLACK)
    
    pygame.display.update()
    
    
# takes the rows from the achievements file and returns it as a list of lists
def take_achievements_from_file():
    achievements_list = []
    
    try:
        with open(achievements_file_path, newline='') as f:
            content = csv.reader(f)
            for row in content:
                achievements_list.append([row[0],row[1]])
            return achievements_list
    
    # if it doesn't find the Achievements file, it creates one
    except FileNotFoundError as e:
        dict_o_nums = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
        for value in dict_o_nums.values():
            achievements_list.append([value + " In A Row", False])
        
        write_achievements_into_file(achievements_list)
        return achievements_list
        
        
# writes the new updated achievements given in a form of a list of lists into the file where each list is a row
def write_achievements_into_file(achievements_list):
    with open(achievements_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(achievements_list)


# takes the current list of achievements and updates it according to the achievement index given
def update_achievements(achievements_list, index):
    for i in range(len(achievements_list)):
        if i+1 == index:
            achievements_list[i][1] = True
            write_achievements_into_file(achievements_list)
            return achievements_list
        
        
# Creating buttons using the Button class
# main menu buttons
start_game_button = Button(YELLOW, X_CENTER_OF_SCREEN, HEIGHT-180-(SPACE_BETWEEN_BUTTONS*3), BUTTON_WIDTH, BUTTON_HEIGHT, text="Start Game")
achievements_button = Button(YELLOW, X_CENTER_OF_SCREEN, HEIGHT-180-(SPACE_BETWEEN_BUTTONS*2), BUTTON_WIDTH, BUTTON_HEIGHT, text="Achievements")
credits_button = Button(YELLOW, X_CENTER_OF_SCREEN, HEIGHT-180-SPACE_BETWEEN_BUTTONS, BUTTON_WIDTH, BUTTON_HEIGHT, text="Credits")
quit_game_button = Button(YELLOW, X_CENTER_OF_SCREEN, HEIGHT-180, BUTTON_WIDTH, BUTTON_HEIGHT, text="Exit")

# other menus buttons
roll_button = Button(DARKER_RED, X_CENTER_OF_SCREEN, Y_CENTER_OF_SCREEN, BUTTON_WIDTH, BUTTON_HEIGHT, text="ROLL")
back_to_main_menu_button = Button(YELLOW, 100, HEIGHT-100, BUTTON_WIDTH, BUTTON_HEIGHT, text="Main Menu")

# a list containing all of the buttons in the main menu
main_menu_buttons_list = [start_game_button, achievements_button, credits_button, quit_game_button]

# a list of all the menu's button lists
menus_of_buttons_lists = [main_menu_buttons_list, [roll_button], [back_to_main_menu_button]]

# menu's variables in order to keep track on which menu should be shown
main_menu = True
game_started_menu = False
achievements_menu = False
credits_menu = False
you_win_menu = False

# creating the how_much_in_a_row variable
how_much_in_a_row = 0

# creating a variable to which i will tell by if the user got it right or wrong when he rolls
right_or_wrong = None


# MAIN LOOP
main_loop = True
if __name__ == "__main__":
    achievements_list = take_achievements_from_file()
    while main_loop:
        # setting the frames
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # getting the positioning of the mouse and implementing it in the variable 'pos'
            mouse_pos = pygame.mouse.get_pos()
        
            # checks if the user presses the X button to exit the game
            if event.type == pygame.QUIT:
                main_loop = False
                
            # checks if the user presses the Mouse Button
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                # main menu:
                # Start Game button
                if start_game_button.isOver(mouse_pos) and main_menu:
                    main_menu = False
                    game_started_menu = True
                # Achievements button
                if achievements_button.isOver(mouse_pos) and main_menu:
                    main_menu = False
                    achievements_menu = True
                # Credits button
                if credits_button.isOver(mouse_pos) and main_menu:
                    main_menu = False
                    credits_menu = True
                # Exit button
                if quit_game_button.isOver(mouse_pos) and main_menu:
                    #mouse_click_sound.play()
                    main_loop = False
                
                # game started menu:
                # Roll button
                if roll_button.isOver(mouse_pos) and game_started_menu:
                    # rolls the 'dice' 1 = the correct answer, 0 = wrong
                    if randint(0,1) == 1:
                        how_much_in_a_row += 1
                        right_or_wrong = True
                        achievements_list = update_achievements(achievements_list, how_much_in_a_row)
                    else:
                        how_much_in_a_row = 0
                        right_or_wrong = False
                        
                    # when user has won
                    if how_much_in_a_row == 10:
                        how_much_in_a_row = 0
                        right_or_wrong = None
                        game_started_menu = False
                        you_win_menu = True
                        
                # back to Main Menu button
                if back_to_main_menu_button.isOver(mouse_pos) and not main_menu:
                    game_started_menu = False
                    achievements_menu = False
                    credits_menu = False
                    you_win_menu = False
                    main_menu = True
                    how_much_in_a_row = 0
                    right_or_wrong = None
            
            # checks if the user is hovering its mouse over certain buttons and if it does it changes their color
            if event.type == pygame.MOUSEMOTION:
                # going over each menu's buttons
                for menu_buttons in menus_of_buttons_lists:
                    # going over each button of each menu
                    for button in menu_buttons:
                        # temp_color = button.color
                        if button.isOver(mouse_pos):
                            button.color = RED
                        else:
                            # button.color = temp_color
                            button.color = YELLOW

                
        draw_game_window()
                
    pygame.quit()
