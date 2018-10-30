import game_framework
from pico2d import *
import game_world
import random

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3 ) #10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km/Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

#move



class Ghost:
    image = None
    def __init__(self, x = 1600 // 2 , y = 90, velocity = 1):
        if Ghost.image == None:
            self.image = load_image('animation_sheet.png')

        # fill here
        self.x  = 1600 // 2
        self.y  = 90
        self.velocity = velocity
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []

        #Drill 12 관련 함수
        # 캐릭터 원운동
        self.move_x = 0
        self.move_y = 0
        #캐릭터 일어나기
        self.pivot_x = 0
        self.pivot_y = 0
        # 각도
        self.degree = 0
        self.t = 0
        self.start = False
        self.rand_opaf_ = 0.1


    def update(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if (self.t <= 3.141592 / 2):
            self.t += 0.02
            self.pivot_x += 0.2
            self.pivot_y += 0.5
            self.rand_opaf_ -= 0.01

        if (self.t >= 3.141592 / 2):
            self.start = True

        if self.start == True:
            self.degree = (self.degree + 720 * game_framework.frame_time) % 360
            self.rand_opaf_ = random.randint(1, 9) / 10

            self.move_x = 100 * math.cos((self.degree) * (3.141592 / 180))
            self.move_y = 100 * math.sin((self.degree) * (3.141592 / 180)) + 100


    def draw(self):
        # fill here
        self.image.opacify(self.rand_opaf_)
        self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, 3.141592 / 2 - self.t, '',
                                      self.x - 25 + self.move_x + self.pivot_x, self.y - 25 + self.move_y + self.pivot_y,
                                      100, 100)

