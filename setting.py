class Settings:
    def __init__(self):
        self.screen_width=1000
        self.screen_height=800
        self.bg_color=(255, 255, 150)
        
        self.body_height=15
        self.body_width=15
        self.body_color=(0, 255, 0)
        
        self.snake_height=15
        self.snake_width=15
        self.snake_speed=1
        self.snake_color=(255, 0, 0)
        
         
        self.body_height=10
        self.body_width_static=15
        self.body_size=15
        
        self.flag=''
      
        
        self.number_of_rabbits=0
        self.rate=1.1
        
    def speed_up(self):
        self.snake_speed*=self.rate