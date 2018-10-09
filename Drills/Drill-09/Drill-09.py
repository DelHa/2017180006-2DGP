from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x , self.y = 0,90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1)% 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100 , 0,100,100,self.x, self.y)



class Small_Ball:
    def __init__(self):
        #랜덤하게 출력
        self.x , self.y = random.randint(100, 600),500
        self.image = load_image('ball21x21.png')
        self.frame = random.randint(3,10)

    def update(self):
        #frame random
        if (self.y > 70):
            self.y -= self.frame

    def draw(self):
        self.image.draw(self.x , self.y)

class Big_Ball:
    def __init__(self):
        #랜덤하게 출력
        self.x , self.y = random.randint(100, 700),500
        self.image = load_image('ball41x41.png')
        self.frame = random.randint(3,10)

    def update(self):
        #frame random
        if(self.y > 70):
            self.y -= self.frame

    def draw(self):
        self.image.draw(self.x , self.y)





def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
boy = Boy()
grass = Grass()

running = True


# game main loop code
while running:
    handle_events()
    boy.update()
    clear_canvas()

    grass.draw()
    boy.draw()
    update_canvas()

    delay(0.05)
# finalization code

close_canvas()