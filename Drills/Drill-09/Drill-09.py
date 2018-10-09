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
        self.x , self.y = random.randint(100,700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1)% 8
        self.frame = random.randint(1,8)
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
small_ball = Small_Ball()
big_ball = Big_Ball()
grass = Grass()

running = True;

rand_num = random.randint(2,19)

team = [Boy() for i in range(11)]
#
#랜덤 공 생성
_samll_ball_num = [Small_Ball() for i in range(rand_num)]
_blg_ball_num = [Big_Ball() for i in range(20-rand_num)]


# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()

    for small_ball in _samll_ball_num:
        small_ball.update()

    for big_ball in _blg_ball_num:
        big_ball.update()

    clear_canvas()
    grass.draw()

    # 소년들 출력


    for boy in team:
        boy.draw()

    # 공 출력
    # 작은공 #

    for small_ball in _samll_ball_num:
        small_ball.draw()
    # 큰공

    for big_ball in _blg_ball_num:
        big_ball.draw()

    update_canvas()

    delay(0.05)
# finalization code

close_canvas()