import pygame
from pygame.sprite import Sprite
from random import randint

class Rabbit(Sprite):
    def __init__(self, snakeobj):
        super().__init__()
        self.snakeobj=snakeobj
        self.setting=snakeobj.setting
        self.screen=snakeobj.screen
        self.image=pygame.image.load('C:\\Users\\User\\Desktop\\Python\\Snake\\Toy-576514_1280-_2_.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.center=self.screen_rect.center
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.x_temp=self.x
        self.y_temp=self.y
        
    def update(self):
        num_x=randint(-100,100)
        # num_y=randint(self.screen_rect.top+10, self.screen_rect.bottom-10)
        num_y=randint(-100,100)
        self.x+=num_x
        self.y+=num_y
        
        if self.x<self.screen_rect.right-30 and self.x>self.screen_rect.left+30:
            self.rect.x=self.x
        else:
            self.rect.x=self.x_temp
            
        if self.y<self.screen_rect.bottom-30 and self.y>self.screen_rect.top+30:
            self.rect.y=self.y
        else:
            self.rect.y=self.y_temp
            
    def draw_rabbit(self):
        self.screen.blit(self.image, self.rect)
        