import pygame, os, random
from pygame.locals import *
from array import *
import numpy as np 
pygame.init()

win=pygame.display.set_mode((500,590))
pygame.display.set_caption('FloopyBird')
icon=pygame.image.load(os.path.join('Assets','gfx','icon.jpeg'))
pygame.display.set_icon(icon)

bg=pygame.image.load(os.path.join('Assets','gfx','Background.png'))
base=pygame.image.load(os.path.join('Assets','gfx','base.png'))
bird1=pygame.image.load(os.path.join('Assets','gfx','y1.png'))
bird2=pygame.image.load(os.path.join('Assets','gfx','y2.png'))
bird3=pygame.image.load(os.path.join('Assets','gfx','y3.png'))
pipe2=pygame.image.load(os.path.join('Assets','gfx','gp.png'))
pipe1=pygame.transform.rotate(pipe2,180)

flap=pygame.mixer.Sound(os.path.join('Assets','sfx','wing.wav'))
hit=pygame.mixer.Sound(os.path.join('Assets','sfx','hit.wav'))
die=pygame.mixer.Sound(os.path.join('Assets','sfx','die.wav'))
point=pygame.mixer.Sound(os.path.join('Assets','sfx','point.wav'))
music=pygame.mixer.music.load(os.path.join('Assets','sfx','Background_Music.mp3'))
flap.set_volume(0.1)
point.set_volume(0.1)
hit.set_volume(0.1)
die.set_volume(0.1)
pygame.mixer.music.set_volume(0.2)

pipe_coordinates=[1]
del(pipe_coordinates[0])
bird_time=pygame.time.get_ticks()
jump_c=10
bg_cor=0
bs_cor=0
bird_y=250
bird_cor=[250,250]
bird_rect=0
score=0
bird_deg=0
b_col=0
p_col=0


def iteration():
    global bird_deg
    global bg_cor
    global bs_cor
    global jump_c
    global bird_cor
    global pipe_coordinates
    bird_flag=False
    normal_flag=False

    #Background Iteration
    bg_cor-=0.2
    if bg_cor<=-300:
        bg_cor=0
    bs_cor-=1.5
    if bs_cor<=-169.5:
        bs_cor=0

    #Jump/Gravity Iteration
    if jump_c<0:
        if jump_c<0:
            if bird_cor[1]-abs((jump_c**2)*0.125)>0:
                bird_cor[1]-=abs((jump_c**2)*0.125)
            else :
                normal_flag=True
            jump_c+=0.5
            bird_flag=True
    else:
        if bird_cor[1]+abs((jump_c**2)*0.05)<480:
            bird_cor[1]+=abs((jump_c**2)*0.05)
        else :
            normal_flag=True
        
        if jump_c<10:
            jump_c+=0.5
        else:
            jump_c+=0.1
        bird_flag=False
    
    if bird_flag:
        bird_deg=min(80,round(((abs((jump_c**2)*0.110))/12.5)*70,4))+5
    else:
        bird_deg=-min(90,round(((abs((jump_c**2)*0.03))/6.27)*70,4))+5

    #Pipe iteration
    for i in range(0,len(pipe_coordinates)):
        pipe_coordinates[i][2]-=1.5 
    display()
    return normal_flag


def display():
    global bird_rect
    global score
    global bird_deg

    win.fill((0,0,0))
    win.blit(bg,(bg_cor,0))

    newScore=str(score)
    scr_cor=[250,30]

    if len(newScore)%2==0:
        scr_cor[0]-=(len(newScore)/2)*26
    else:
        scr_cor[0]-=int(np.round(len(newScore)/2))*26+13


    for i in newScore:
        name=i+'.png'
        num=pygame.image.load(os.path.join('Assets','gfx',name))
        win.blit(num,scr_cor)
        scr_cor[0]+=26


    curr_time=pygame.time.get_ticks()
    if (curr_time-bird_time)%500>332:
        newbird=bird1
    elif (curr_time-bird_time)%500>166:
        newbird=bird2
    else:
        newbird=bird3
    rotated_bird=pygame.transform.rotate(newbird,bird_deg)


    for i in pipe_coordinates:
        win.blit(pipe1,(i[2],i[0]))
        win.blit(pipe2,(i[2],i[1]))
    bird_rect=rotated_bird.get_rect()
    bird_rect.center=bird_cor
    win.blit(rotated_bird,bird_rect)

    win.blit(base,(bs_cor,500))



def spawn(spawn_timer):
    global pipe_coordinates
    
    cordinates=random.randint(200,480)
    pipe_coordinates.append([cordinates-650,cordinates,501])
    for i in range(len(pipe_coordinates)-1,-1,-1):
        if pipe_coordinates[i][2]<-80:
            del(pipe_coordinates[i]) 
    return(max(spawn_timer-10,1500))


def check():
    global bird_cor
    global pipe_coordinates
    global score
    flag=False


    for i in pipe_coordinates:
        if (i[2]==250.5):
            pygame.mixer.Sound.play(point)
            score+=1
        if (bird_cor[1]+17.5>i[1] and i[2]<=270 and i[2]>=174):
            #Down
            flag=True
            break
        if (bird_cor[1]<i[1]-152.5 and i[2]<=270 and i[2]>=174):
            #Up
            flag=True
            break
    return flag

def restart():
    global bird_cor
    global pipe_coordinates
    global jump_c
    global score
    global bird_deg

    bird_deg=0
    jc=-6
    y_offset=0
    deg_offset=10
    run=True
    ch=0
    jump_c=0
    rest_y=300
    rest_offset=-1
    rest_flag=False
    alpha=0
    while run:
        for event in pygame.event.get():
            if event.type==QUIT:
                run=False
                ch=1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                run=False
                ch=1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
                ch=2
                run=False
        
        
        if jc<0:
            y_offset=-abs((jc**2)*0.3)
            jc+=0.25
        else:
            y_offset=abs((jc**2)*0.05)
            jc+=0.4
    
        if bird_cor[1]+y_offset<480 and bird_cor[1]+y_offset>0:
            bird_cor[1]+=y_offset

        if deg_offset>0:
            deg_offset-=0.09
        else:
            deg_offset=0
        
        bird_deg-=deg_offset

        if rest_offset<-1:
            rest_flag=True
        elif rest_offset>1:
            rest_flag=False
        
        if rest_flag:
            rest_offset+=0.1
        else:
            rest_offset-=0.1
        
        rest_y+=rest_offset

        display()
        rest_png=pygame.image.load(os.path.join('Assets','gfx','gameover.png'))
        rest_png.set_alpha(alpha)
        rest_rect=rest_png.get_rect()
        rest_rect.center=[250,rest_y]
        if alpha<255:
            alpha+=2.5
        win.blit(rest_png,rest_rect)


        if ch==2:
            bird_cor=[250,250]
            pipe_coordinates=[1]
            del(pipe_coordinates[0])
            bird_deg=-5
            #spawn(2500)
        pygame.time.wait(8)
        pygame.display.update()
    score=0
    if ch==2:
        return True
    else:
        return False
            
def start():
    global bird_cor
    global jump_c

    jump_c=-1
    bird_offset=-1
    image_alpha=0
    y_image=210
    birdy_flag=False
    image_flag=True
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==QUIT:
                run=False
                ch=1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                run=False
                ch=1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                ch=2
                run=False
        if bird_offset<-1:
            birdy_flag=True
        elif bird_offset>1:
            birdy_flag=False
        
        if birdy_flag:
            bird_offset+=0.1
        else:
            bird_offset-=0.1

        bird_cor[1]+=bird_offset
        start_png=pygame.image.load(os.path.join('Assets','gfx','message.png'))
        start_png.set_alpha(image_alpha)
        start_rect=start_png.get_rect()
        start_rect.center=[250,y_image]
        if image_alpha<190:
            image_alpha+=10
        else:
            if image_alpha<200:
                image_flag=True
            elif image_alpha>250:
                image_flag=False
        
            if image_flag:
                image_alpha+=1
            else:
                image_alpha-=1


        display()
        win.blit(start_png,start_rect)
        pygame.time.wait(16)
        pygame.display.update()
    if ch==2:
        jump_c=-10
        return True
    else:
        return False



    
def main():
    win.fill((0,0,0))
    global jump_c
    global bird1
    global bird2
    global bird3
    global pipe1
    global pipe2
    global b_col
    global p_col

    pygame.mixer.music.play(-1)
    spawn_timer=2500
    spawn(spawn_timer)
    collision_flag=False
    run=True
    run=start()
    time_start=pygame.time.get_ticks()

    while run:
        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if event.type==QUIT:
                run=False
            if keys[pygame.K_ESCAPE]:
                run=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or event.type==MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(flap)
                jump_c=-10
            if event.type==pygame.KEYDOWN and event.key==pygame.K_c:
                if b_col%3==0:
                    bird1=pygame.image.load(os.path.join('Assets','gfx','r1.png'))
                    bird2=pygame.image.load(os.path.join('Assets','gfx','r2.png'))
                    bird3=pygame.image.load(os.path.join('Assets','gfx','r3.png'))
                elif b_col%3==1:
                    bird1=pygame.image.load(os.path.join('Assets','gfx','b1.png'))
                    bird2=pygame.image.load(os.path.join('Assets','gfx','b2.png'))
                    bird3=pygame.image.load(os.path.join('Assets','gfx','b3.png'))
                elif b_col%3==2:
                    bird1=pygame.image.load(os.path.join('Assets','gfx','y1.png'))
                    bird2=pygame.image.load(os.path.join('Assets','gfx','y2.png'))
                    bird3=pygame.image.load(os.path.join('Assets','gfx','y3.png'))
                b_col+=1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_p:
                if p_col%2==0:
                    pipe2=pygame.image.load(os.path.join('Assets','gfx','rp.png'))
                    pipe1=pygame.transform.rotate(pipe2,180)
                elif p_col%2==1:
                    pipe2=pygame.image.load(os.path.join('Assets','gfx','gp.png'))
                    pipe1=pygame.transform.rotate(pipe2,180)
                p_col+=1

        
        collision_flag=iteration() or check()

        
        end_time=pygame.time.get_ticks()
        if end_time-time_start>=spawn_timer:
            spawn_timer=spawn(spawn_timer)
            time_start=pygame.time.get_ticks()

        if collision_flag:
            pygame.mixer.Sound.play(hit)
            pygame.mixer.Sound.play(die)
            end_time=pygame.time.get_ticks()
            spawn(2500)
            spawn_timer=2500
            run=restart()
            if run:
                run=start()

            

        pygame.time.wait(8)
        pygame.display.update()

    pygame.quit()

main()