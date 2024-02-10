import sys
import pygame
from random import randint
from setting import Settings
from snake import Snake
from snake import Body
from rabbit import Rabbit

class SnakeGame:
    def __init__(self):
        self.setting=Settings()
        self.screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.snake=Snake(self)
        self.rabbit=Rabbit(self)
        self.flag='horizontal'
        
    def run(self):
        while True:
            self._check_events()
            # self.snake.update()
            # self.create_rabbit()
            self._increase_body()
            self._check_movement()
            self.snake.automatic_update()
            self.update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_key_down(event)       
            elif event.type==pygame.KEYUP:
                self._check_key_up(event)     
                
    def _check_key_down(self, event):
        if event.key==pygame.K_RIGHT:
            # print('down')
            self.snake.right=True
            self.flag='horizontal'
            self.setting.flag='right'
    
        elif event.key==pygame.K_LEFT:
            self.flag='horizontal'
            self.setting.flag='left'
            self.snake.left=True
           
        elif event.key==pygame.K_UP:
            self.flag='vertical'
            self.setting.flag='up'
            self.snake.up=True
          
        elif event.key==pygame.K_DOWN:
            self.flag='vertical'
            self.setting.flag='down'
            self.snake.down=True
          
        elif event.key==pygame.K_q:
            sys.exit()
            
    def _check_key_up(self, event):
        if event.key==pygame.K_RIGHT:
            self.snake.right=False
        elif event.key==pygame.K_LEFT:
            self.snake.left=False
        elif event.key==pygame.K_UP:
            self.snake.up=False
        elif event.key==pygame.K_DOWN:
            self.snake.down=False
                    
    def _increase_body(self):
        self.body=Body(self)
        collision=self.rabbit.rect.colliderect(self.snake.rect)
        if collision:
            self.setting.body_size+=1
            self.rabbit.update()
            self.setting.number_of_rabbits+=1
            if self.setting.number_of_rabbits%5==0:
                self.setting.speed_up()
            
    def _check_movement(self):
        if self.snake.check_edge():
            sys.exit()
        else:
            # print('not edge')
            if self.flag=='horizontal':
                self.setting.body_width=self.setting.body_size
                self.setting.body_height=self.setting.body_width_static
            elif self.flag=='vertical':
                self.setting.body_width=self.setting.body_width_static
                self.setting.body_height=self.setting.body_size
            self.body.center()
           
    def update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.body.draw_body()
        self.snake.draw_snake()
        self.rabbit.draw_rabbit()
        pygame.display.flip()
                   
if __name__=='__main__':
    snakeobj=SnakeGame()
    snakeobj.run()
    