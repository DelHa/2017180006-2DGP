import random
from pico2d import *
import game_world
import game_framework
from background import InfiniteBackground
import main_state

background = InfiniteBackground


class Ball:
    global boy
    image = None

    def __init__(self):

        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(0, 1600-1), 0

        self.roll_x = 0
        self.roll_y = 0

        self.output_x = 0
        self.output_y = 0
        #

    def get_bb(self):
        return self.x - 10 - main_state.boy.x, self.y - 10 - main_state.boy.y, self.x + 10 - main_state.boy.x, self.y + 10 - main_state.boy.y

    def draw(self):
         #self.y = self.y + main_state.boy.text_y
         #self.output_x = (self.x + main_state.boy.x)

         self.image.draw((self.x - main_state.boy.x) , (self.y - main_state.boy.y))

         draw_rectangle(*self.get_bb())

    def update(self):
        #self.y -= self.fall_speed * game_framework.frame_time

        pass



