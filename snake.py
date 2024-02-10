import pygame
from pygame.sprite import Sprite

class Snake():
    def __init__(self, ai):
        super().__init__()
        self.ai=ai
        self.setting=ai.setting
        self.screen=ai.screen
        self.rect=pygame.Rect(0, 0, self.setting.snake_width, self.setting.snake_height)
        self.screen_rect=self.screen.get_rect()
        self.rect.center=self.screen_rect.center
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.left=False
        self.right=False
        self.up=False
        self.down=False


    def automatic_update(self):
        if self.setting.flag=='left':
            self.x-=self.setting.snake_speed
        if self.setting.flag=='right':
            self.x+=self.setting.snake_speed
        if self.setting.flag=='up':
            self.y-=self.setting.snake_speed
        if self.setting.flag=='down':
            self.y+=self.setting.snake_speed
        self.rect.x=self.x
        self.rect.y=self.y
            
        
    # def update(self):
    #     if self.left and self.rect.left>0:
    #         self.x-=self.setting.snake_speed
    #     if self.right and self.rect.right<self.screen_rect.right:
    #         self.x+=self.setting.snake_speed
    #     if self.up and self.rect.top>0:
    #         self.y-=self.setting.snake_speed
    #     if self.down and self.rect.bottom<self.screen_rect.bottom:
    #         self.y+=self.setting.snake_speed
    #     self.rect.x=self.x
    #     self.rect.y=self.y
        
    def check_edge(self):
        if self.rect.x>=self.screen_rect.right-15 or self.rect.x<=self.screen_rect.left+10 or self.rect.y<=self.screen_rect.top+10 or self.rect.y>=self.screen_rect.bottom-15:
            return True
        else:
            return False
        
    def draw_snake(self):
        pygame.draw.rect(self.screen, self.setting.snake_color, self.rect)
        # self.screen.blit(self.rect, self.rect)


class Body(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.ai=ai
        self.setting=self.ai.setting
        self.screen=self.ai.screen
        self.rect=pygame.Rect(0, 0, self.setting.body_width, self.setting.body_height)
        self.screen_rect=self.screen.get_rect()
        self.rect.midbottom=self.ai.snake.rect.midbottom
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        
    def center(self):
        if self.setting.flag=='left':
            self.rect.left=self.ai.snake.rect.left
        elif self.setting.flag=='right':
            self.rect.right=self.ai.snake.rect.right
        elif self.setting.flag=='down':
            self.rect.bottom=self.ai.snake.rect.bottom
        elif self.setting.flag=='up':
            self.rect.top=self.ai.snake.rect.top
            
        
    def draw_body(self):
        pygame.draw.rect(self.screen, self.setting.body_color, self.rect)

        