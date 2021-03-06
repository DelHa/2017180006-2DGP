import game_framework
from pico2d import *
from ball import Ball
from ghost import Ghost
import math
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
#애니메이션 프레임수
FRAMES_PER_ACTION = 8

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE

}

current_time = 0
save_time = 0

# Boy States

enter_ghost = False

class IdleState:
    global current_time
    global save_time

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.timer = 1000



    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.timer -= 1

        if get_time() >= 10: #딱 10초에 눕는다.
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        # fill here
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)

        pass

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        # fill here
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)

        boy.x += boy.velocity * game_framework.frame_time

        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)

ghost = None

class SleepState:
    global enter_ghost
    global ghost

    @staticmethod
    def enter(boy, event):
        boy.frame = 0
        enter_ghost = False
        boy.move_x = 0
        boy.move_y = 0
        boy.degree = 270
        boy.rand_opaf_ =1
        #들어왔을때 시간 체크
        boy.new_Ghost()

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if(boy.t <= 3.141592/2):
            boy.t += 0.02
            boy.pivot_x += 0.2
            boy.pivot_y += 0.5
            boy.rand_opaf_ -= 0.01

        if(boy.t >= 3.141592 / 2):
            boy.start = True


        if boy.start == True:
            boy.degree = (boy.degree  + 720 * game_framework.frame_time) % 360
            boy.rand_opaf_ = random.randint(1, 9) / 10

        boy.move_x = 200 * math.cos((boy.degree) * (3.141592 / 180))
        boy.move_y = 200 * math.sin((boy.degree) * (3.141592/ 180)) + 200


    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.opacify(1)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)


            if(boy.degree % 180 == 0):
                print("1234")

        else:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
            boy.image.opacify(0.5)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, -3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
            boy.image.opacify(1)




next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState },
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        # fill here
        self.font = load_font('ENCR10B.TTF' , 16) #폰트 업로드

        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

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


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)

    def new_Ghost(self):
        ghost = Ghost(self.x, self.y, self.dir * 1)
        game_world.add_object(ghost , 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # 폰트 렌더링
        self.font.draw(self.x - 60 , self.y + 50 , '(Time : %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

