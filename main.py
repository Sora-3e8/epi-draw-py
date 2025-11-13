#!.venv/bin/python
import pygame
import math

# pygame setup
controls=["Controls: ","    F1=show/hide controls","    SPACE=pause","    TAB=select arm","    ARROW_UP=increase arm speed","    ARROW_DOWN=lower arm speed","    ARROW_LEFT=shorten_arm","    ARROW_RIGHT=prolong_arm","    KEY_PAGEUP=increase step","    KEY_PAGEDOWN=decrease step","    R=zero arm angle" ,"    DELETE=clears drawn lines"]
angle=0.0
ang=0.0
ang2=0.0
pygame.init()
pygame.display.set_caption('Epicycle drawing')
add_ang_t=""
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
mouse_down=False
key_down=False
events=[]
pause=True
point0=(1280/2,720/2)
point=(0,0)
ang_step1=1.00
ang_step2=2.00
arm_sel=0
to_add=0
speed_step=(1/1000)
point2=(0,0)
point3=(0,0)
center=[(1280/2),(720/2)]
arm1_length=100
arm2_length=100
dx=10
dy=10
controls_visible=True
font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 10)
points=[]

def vec2_dx(vec2,vec2_1):
    dx=vec2[0]-vec2_1[0]
    dy=vec2[1]-vec2_1[1]
    return [dx,dy]
    
def vector_angle(vec2):
    dx=vec2[0]
    dy=vec2[1]
    if dx<0 and dy>0:
        angle=90-math.atan(-dy/dx)*(180/math.pi)

    if dx<0 and dy<0:
        angle=90+(-math.atan(-dy/dx)*(180/math.pi))

    if dx>0 and dy<0:
        angle=180+(math.atan(dx/-dy)*(180/math.pi))

    if dx>0 and dy>0:
        angle=270+math.atan(dy/dx)*(180/math.pi)

    if dx==0:
        if dy>0:
            angle=0
        if dy<0:
            angle=180

    if dy==0:
        if dx>0:
            angle=270
        if dx<0:
            angle=90
    return angle

def render_controls():
    if controls_visible==True:
        y_pos=20
        for i in range(0,len(controls)):
            controls_lbl = font.render(controls[i],True, (180, 180, 180))
            screen.blit(controls_lbl, dest=(20,y_pos))
            y_pos=y_pos+25
        y_pos=20
        
def angle_vector(angle_in,arm_length):
    vector=[0,0]
    angle_input=angle_in

    vector[0]=math.cos(angle_input/(180/math.pi))*arm_length
    vector[1]=math.sin(angle_input/(180/math.pi))*arm_length
    if angle_input>360:
        angle_input=angle_input-((angle_input//360)*360)
    return vector

def main():
    global controls
    global ang
    global ang2
    global angle
    global pygame
    global add_ang_t
    global screen
    global clock
    global running
    global mouse_down
    global key_down
    global events
    global pause
    global point2
    global point3
    global to_add
    global speed_step
    global center
    global arm1_length
    global arm2_length
    global dx
    global dy
    global controls_visible
    global font
    global font2
    global points
    global arm_sel
    global point
    global ang_step1
    global ang_step2
    start_ticks=pygame.time.get_ticks()
    while running:
        if pygame.time.get_ticks()-start_ticks>=10:
            start_ticks-100
            if pause==False:
                ang=ang+ang_step1
                ang2=ang2+ang_step2
            arm_vector=angle_vector(ang,arm1_length)
            point=(point0[0]+arm_vector[0],point0[1]+arm_vector[1])
            point2=(point[0]+angle_vector(ang2,arm2_length)[0],point[1]+angle_vector(ang2,arm2_length)[1])
            angle=vector_angle(vec2_dx(point0,point))
            print(point)

        events = pygame.event.get()
        for event in events:

            if event.type == pygame.KEYDOWN:
                key_down=True
                if event.key == pygame.K_F1:
                    if controls_visible==True:
                        controls_visible=False
                    else:
                        controls_visible=True
                if event.key == pygame.K_r:
                    if arm_sel==0:
                        ang=0
                    else:
                        ang2=0
                if event.key == pygame.K_SPACE:
                    if pause==True:
                        pause=False
                    else:
                        pause=True
                if event.key == pygame.K_PAGEUP:
                    if speed_step==(1/1000):
                        speed_step=(5/1000)
                    else:
                        speed_step=speed_step+(5/1000)
                if event.key == pygame.K_PAGEDOWN:
                    if speed_step>(5/1000):
                        speed_step=speed_step-(5/1000)
                    else:
                        speed_step=1/1000

                if event.key == pygame.K_UP:
                    to_add=1
                if event.key == pygame.K_DOWN:
                    to_add=-1
                if event.key == pygame.K_RIGHT:
                    to_add=0.5
                if event.key == pygame.K_LEFT:
                    to_add=-0.5
                if event.key == pygame.K_DELETE:
                     points=[]
                if event.key == pygame.K_TAB:
                    if arm_sel==1:
                        arm_sel=0
                    else:
                         arm_sel=1
            if event.type == pygame.KEYUP:
                key_down=False
                to_add=0
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down=True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down=False

        if mouse_down==True:
            point=pygame.mouse.get_pos()
            angle=vector_angle(vec2_dx(point0,point))

        if key_down==True:
            if to_add==1:
                if arm_sel==0:
                    ang_step1=ang_step1+speed_step
                if arm_sel==1:
                    ang_step2=ang_step2+speed_step
            if to_add==-1:
                if arm_sel==0:
                    ang_step1=ang_step1-speed_step
                if arm_sel==1:
                    ang_step2=ang_step2-speed_step
            if to_add==0.5:
                if arm_sel==0:
                    arm1_length=arm1_length+speed_step
                if arm_sel==1:
                    arm2_length=arm2_length+speed_step
            if to_add==-0.5:
                if arm_sel==0:
                    arm1_length=arm1_length-speed_step
                if arm_sel==1:
                    arm2_length=arm2_length-speed_step

        screen.fill("black")

        if point2!=(0,0):
            points.append(point2)
        if arm_sel==1:
            pygame.draw.line(screen,  (255,255,255), center,point, 5)
            pygame.draw.line(screen,(150,255,150), point,point2, 5)
            arm_len1_lbl=font.render("Length arm1: "+str(arm1_length)[0:4],True, (255, 255, 255))
            arm_len2_lbl=font.render("Length arm2: "+str(arm2_length)[0:4],True, (150,255,150))
            speed1 = font.render("Speed arm1: "+str(ang_step1)[0:4],True, (255, 255, 255))
            speed2 = font.render("Speed arm2: "+str(ang_step2)[0:4],True, (150,255,150))

        if arm_sel==0:
            pygame.draw.line(screen, (150,255,150), center,point, 5)
            pygame.draw.line(screen, (255,255,255), point,point2, 5)
            arm_len1_lbl=font.render("Length arm1: "+str(arm1_length)[0:4],True, (150,255,150))
            arm_len2_lbl=font.render("Length arm2: "+str(arm2_length)[0:4],True, (255, 255, 255))
            speed1 = font.render("Speed arm1: "+str(ang_step1)[0:4],True, (150,255,150))
            speed2 = font.render("Speed arm2: "+str(ang_step2)[0:4],True, (255, 255, 255))
        if len(points)>1:
            pygame.draw.lines(screen, (200,0,0),False,points, 2)
        start_lbl = font.render(str(angle)[0:5]+"°",True, (255, 255, 255))
        end_lbl = font.render(str(point[0])[0:3]+","+str(-point[1])[0:4],True, (255, 255, 255))

        speed_step_lbl = font.render("Speed step: "+str(speed_step*10)[0:4],True, (255, 255, 255))
        render_controls()
        screen.blit(end_lbl, dest=(point))
        screen.blit(start_lbl, dest=center)
        screen.blit(speed_step_lbl, dest=(20,590))
        screen.blit(arm_len1_lbl, dest=(20,610))
        screen.blit(arm_len2_lbl, dest=(20,630))
        screen.blit(speed1, dest=(20,650))
        screen.blit(speed2, dest=(20,670))

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()
