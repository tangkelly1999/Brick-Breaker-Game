'''Date : May 1 , 2016
Author: Kelly Tang
Description: module that contains the Bricks, Wall, Ball, Player, and Score_Keeper sprite classes'''

import pygame
pygame.init()

class Brick(pygame.sprite.Sprite):
    '''This class defines the sprite for the bricks.'''
    
    def __init__(self, screen, (r, g, b), x,y):
        '''Initializer method takes parameters of the screen surface, the tuple for the colour, and its (x,y) coordinates for its position. It initializes its image and rect attributes too'''
        
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes
        self.image=pygame.Surface ((30, 10))
        self.image.fill((r,g,b))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
class Wall(pygame.sprite.Sprite):
    '''This class defines the sprite for each Wall.'''
    
    def __init__(self,screen,(width,height),(x,y)):
        '''Initializer method takes in parameters of the screen surface, integers for the width and height of each wall, and its (x,y) position. It initializes its image and rect attributes too'''
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes
        self.image = pygame.Surface((width,height))
        self.image.fill((175,180,165))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
                          
class Ball(pygame.sprite.Sprite):
    '''This class defines the sprite for the Ball.'''
    
    def __init__(self, screen):
        '''This initializer takes parameters of the screen surface, and
       initializes the image and rect attributes, and x,y direction of the ball.'''
      
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.Surface((10, 10))
        self.image.fill((200, 0, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,screen.get_height()/2)
 
        # Instance variables to set difference in x and y coordinate the ball moves by 
        self.__screen = screen
        self.__dx = 10
        self.__dy = 10
 
    def change_ydirection(self):
        '''This method causes the y direction of the ball to reverse.'''
        self.__dy = -self.__dy
        
    def change_xdirection(self):
        '''This method causes the x direction of the ball to reverse.'''
        self.__dx = -self.__dx
             
    def update(self):
        '''This method called automatically to reposition the
        ball sprite on the screen.'''
        # Check if ball reached the left or right end of the screen.
        # Keep moving the ball in the same x direction if ball didnt reach the end
        if ((self.rect.left > 0) and (self.__dx < 0)) or\
           ((self.rect.right < self.__screen.get_width()) and (self.__dx > 0)):
            self.rect.left += self.__dx       
        # Reverse the x direction if ball reached end of screen
        else:
            self.__dx = -self.__dx
             
        # Check if the ball reached the top or bottom of the screen
        # If not, then keep moving the ball in the same y direction.
        if ((self.rect.top > 0) and (self.__dy > 0)) or\
           ((self.rect.bottom < self.__screen.get_height()-40) and (self.__dy < 0)):
            self.rect.top -= self.__dy
        # change y direction if ball reached top or bottom 
        else:
            self.__dy = -self.__dy  
            
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for the player'''
    
    def __init__(self, screen,width):
        '''This initializer takes a screen surface and initlialized image and rect attributes for it. '''
        
        pygame.sprite.Sprite.__init__(self)
     
        #the paddle the player uses to bounce the ball off of
        self.image = pygame.Surface((width, 10))
        self.image = self.image.convert()
        self.image.fill((200, 0, 200))
        self.rect = self.image.get_rect()
        

        # Center the player horizontally
        self.rect.top = screen.get_height() - 40
        self.rect.left = screen.get_width()/2 -50
       
        self.__screen = screen
        self.__dx = 0
        
    def change_width(self):
        '''this method called when half of the bricks are destroyed, so the paddle width is cut in half'''
        self.image = pygame.Surface((width, 10))
        self.image = self.image.convert()  
        
    def change_direction(self, x_change):
        '''This method takes an x value as a parameter to set the player's x direction'''
        self.__dx = x_change
         
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        # Check if we have reached the top or bottom of the screen.
        # If not, then keep moving the player in the same y direction.
        if ((self.rect.left > 0) and (self.__dx > 0)) or\
           ((self.rect.right < self.__screen.get_width()) and (self.__dx < 0)):
            self.rect.left -= (self.__dx*5)
        # If yes, then we don't change the y position of the player at all.
   
               
class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for the bottom endzone'''
    
    def __init__(self, screen):
        '''This initializer takes a screen surface, and sets image and rect attributes for the endzone sprite'''
     
        pygame.sprite.Sprite.__init__(self)
         
        # Endzone sprite will be a 1 pixel wide black line running horizontally
        self.image = pygame.Surface((screen.get_width(), 1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.bottom = screen.get_height()-40
        
        
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score, and the # of lives remaining'''
    
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0, and lives remaining as 3'''
     
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.SysFont("Arial", 30)
        self.__player_score = 0
        self.__lives_remaining = 3
        
    def lives_remaining(self):
        '''this method called whenever ball hits bottom endzone, and removes one life'''
        self.__lives_remaining -= 1
    
    def player_score1(self):
        '''this method adds one point per brick destroyed in the bottom row'''
        self.__player_score +=1
        
    def player_score2(self):
        '''this method adds 2 points per brick destroyed in the 2nd row from bottom '''
        self.__player_score +=2
        
    def player_score3(self):
        '''this method adds 3 points per brick destroyed in the 3rd row'''
        self.__player_score +=3 
        
    def player_score4(self):
        '''this method adds 4 points per brick destroyed in the 4th row from bottom'''
        self.__player_score +=4
        
    def player_score5(self):
        '''this method adds 5 points per brick destroyed in the 5th row'''
        self.__player_score +=5
        
    def player_score6(self):
        '''this method adds 6 points per brick destroyed in the top row'''
        self.__player_score +=6
        
    def loser(self):
        '''this method returns 1 if there's no more lives left when the player loses'''
        if self.__lives_remaining == 0:
            return 1
        
    def winner(self):
        if self.__player_score == 378:
            return 1
        
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        #message = "Player 1: %d vs. Player 2: %d" ,(self.__player1_score)
        message ="Score: %d   Lives Remaining: %d" %(self.__player_score, self.__lives_remaining)
        self.image = self.__font.render(message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 15)
