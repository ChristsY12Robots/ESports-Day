import pygame
import os
import subprocess
import profile

width, height = 800,600
pygame.init()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Main Menu')

fps = pygame.time.Clock()
MainMenu = pygame.image.load('MainMenu.jpg')
#editted by Miles Burne 1/2/18 to add reciver functionality in the launching and closing of tetris and pacman
import getpass #to get the user's name

#ADDED
#function to recieve the file on the other end, needs an input of the game name ("pacman","tetris")
#FUNCTION TAKES LOWER CASE NAMES
def reciever(game):
    username = (getpass.getuser()).lower() #I found an issue where if the user logs in with caps enabled, the username will be all caps in program. Not a big deal but may as well solve it.
    user_profile = profile.User_Profile(username) #getting user profile
    filename = (str(username)+"_"+str(game)+".esp") #getting filename
    f = open(filename, "r")
    content = f.read()
    content = content.split("\n") #file now split into number of records
    content.pop(len(content)-1) #removing the '\n' character
    for x in content:
        x = x.split(",") #now split into [score, game]
        user_profile.update_score(x[0])# updating the score
        user_profile.add_game_record(game)
        user_profile.save()
        
    

def pacman():
    '''RUN game'''
    #ADDED 1/2/18
    reciever('pacman')
    pass
    

def run():   
    subprocess.call('main.py', shell = True)
    '''os.system('main.py')'''

def space_invaders():
    print('SpaceInvaders')
    pass

def tetris():
    '''RUN game'''
    #ADDED 1/2/18
    reciever('tetris')
    pass

while True:    
    fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #x + width > mouse_x > x and y + height > mouse_y > y
    #pacman
    if 228 + 352 > mouse[0] > 228 and 55 + 60 > mouse[1] > 55:
        #display translucent logo with text
        if click[0] == 1:
            pacman()

    #tetris
    if 228 + 352 > mouse[0] > 228 and 171 + 104 > mouse[1] > 171:
        #display translucent logo with text
        if click[0] == 1:
            tetris()        
    #run   
    if 228 + 352 > mouse[0] > 228 and 305 + 105 > mouse[1] > 305:
        #display translucent logo with text
        if click[0] == 1:
            run()
            
    #spaceinvasders 
    if 228 + 352 > mouse[0] > 228 and 427 + 60 > mouse[1] > 427:
        #display translucent logo with text
        if click[0] == 1:
            space_invaders()    
        
    window.blit(MainMenu, [0,0])
    pygame.display.update()

    

    
    
    
