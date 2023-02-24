
import pygame,time
from pygame import KEYDOWN, RESIZABLE, mixer
import random

# music and pygame module loading part
pygame.init()

def music_game(tune):
    mixer.init()
    mixer.music.load(tune)
    mixer.music.set_volume(0.9)
    mixer.music.play()


############# colors  #############
red=(255,0,0)
yellow=(255,255,0)
black=(0,0,0)
pink=(255,116,140)
gray=(166,166,166)
white=(255,255,255)
purple=(205,0,205)
brown=(150,75,0)
blue=(167, 199, 231)
green=(0,255,0)
########################################################################
######################## FUNCTIONS AREA ################################
########################################################################

########## Game_image or icons functions ########
def game_image(image,x,y,height,width):
    pic = pygame.image.load(image).convert_alpha()
    pic=pygame.transform.scale(pic,(height,width))
    screen.blit(pic,(x,y))
  

#### Screen Background Image ####
def screen_background(image,x,y):
    pic = pygame.image.load(image).convert_alpha()
    screen.blit(pic,(x,y))
     

####### Display of the font and image in start of the screen  #########
def screen_font(word,x,y,size,color):
    font=pygame.font.SysFont('arial',size)
    text=font.render(word,True, color)
    screen.blit(text,(x,y))
    

####################################################################################
####################################################################################
####################################################################################
####################################################################################

#########  screen size formatting part (Game Development Area start)   ############
music_game("game_music.mp3")
pygame.display.set_caption("Space_Mission")
screen=pygame.display.set_mode((1350,700))
####### Window icon image load ##########
image=pygame.image.load('spaceship_icon.png').convert_alpha()
pygame.display.set_icon(image)

game_image("spaceship_icon.png",280,240,500,380)
screen_font("SPACE_MISSION",780,380,40,white)
pygame.display.update()
time.sleep(2)

screen.fill(black)
screen_font("WELCOME",400,350,40,yellow)
pygame.display.update()
time.sleep(0.5)
screen_font("TO",650,350,40,white)
pygame.display.update()
time.sleep(0.5)
screen_font("SPACE",740,350,40,blue)
pygame.display.update()
time.sleep(0.5)
screen_font("GAME",890,350,40,blue)
pygame.display.update()
time.sleep(0.5)
screen_font("!",1010,350,40,green)
pygame.display.update()
time.sleep(1)

screen_background("space.jpg",-40,-100)
time.sleep(2)

#### Code for "press enter key on Background image" ####
screen_font("Get Ready To Start Mission",500,640,40,white)
pygame.display.update()
time.sleep(2)

screen.fill(white)

#################### Game Option(button) Area #################################
Book=pygame.image.load('book.png').convert_alpha()
Start=pygame.image.load('start.png').convert_alpha()
End=pygame.image.load('exit.png').convert_alpha()
Arrow=pygame.image.load('arrow.png').convert_alpha()

class Button:
    def __init__(self,x,y,image):
        self.image=pygame.transform.scale(image,(100,100))
        self.x=x
        self.y=y
        self.rect=self.image.get_rect()
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
    def rect(self):
        return self.rect

arrow1=Button(380,160,Arrow)
arrow2=Button(380,340,Arrow)
arrow3=Button(380,520,Arrow)
book=Button(560,160,Book)
start=Button(560,340,Start)
end=Button(560,520,End)

#### Putting Button and font on screen and calling obj of Button ########
######################## GAME MODULES FUNCTIONS #########################
def game_options():
    music_game("game_options.mp3")
    screen.fill(white)
    screen_background("option_back.jpg",-5,0)
    screen_font("||||| GAME OPTIONS ||||",460,40,40,black)
    screen_font("____________________",450,50,40,black)
    screen_font("| GAME MANNUAL |",680,180,40,black)
    screen_font("| Start To Play Games |",680,360,40,black)
    screen_font("| Exit To Close The Game |",680,540,40,black)

    book.draw()
    start.draw()
    end.draw()
    arrow1.draw()
    arrow2.draw()
    arrow3.draw()
    pygame.display.update()

game_options()

######## Mannual Functions ########
def game_mannual():
    end=False
    mixer.music.stop()
    music_game("mannual.mp3")
    screen.fill(black)
    screen_background("mannual_back.jpg",-1450,-700)
    game_image("back_icon.png",20,10,50,50)
    screen_font("-------------------------------------------------------------------------------",100,60,35,white)
    screen_font(" This is a SPACE BASED GAME. In this Game the spaceship,",88,100,35,white)
    screen_font(" will move freely but the obstacle will come randomly so,  ",88,140,35,white)
    screen_font(" You have to protect the spaceship from the obstacle.  ",88,180,35,white)
    screen_font(" The obstacle also can move in fixed path, or it can move  ",88,220,35,white)
    screen_font(" in any direction. As a Captain its your responsiblity to  ",88,260,35,white)
    screen_font(" to protect your spaceship and reach to Destination !!!  ",88,300,35,white)
    screen_font("-------------------------------------------------------------------------------",100,340,35,white)
    screen_font("                    CONTROL OF THE GAME                      ",160,380,35,blue)
    screen_font("-------------------------------------------------------------------------------",100,420,35,blue)
    screen_font("                     W:Toward forward                                         ",160,460,35,blue)
    screen_font("                     A:Toward Left                                            ",160,500,35,blue)
    screen_font("                     S:Toward Backward                                        ",160,540,35,blue)
    screen_font("                     D:Toward Right                                           ",160,580,35,blue)
    screen_font("                     SPACE :  Firing                                          ",160,620,35,blue)
    screen_font("-------------------------------------------------------------------------------",100,660,35,blue)
    pygame.display.update()
    while not end:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if((pos[0]>=19 and pos[0]<=71) and (pos[1]>=12 and pos[1]<=58)):
                        l,m,r=pygame.mouse.get_pressed()
                        if l:
                            end=True
                            mixer.music.stop()
                            game_options()
            if event.type==pygame.QUIT:
                exit()

######################### COMPOENENT OF INSIDE THE GAME ##############################

# def enemy(image,x,y,height,width,angle):
#     pic = pygame.image.load(image)
#     pic=pygame.transform.scale(pic,(height,width))
#     pic=pygame.transform.rotate(pic,angle)
#     screen.blit(pic,(x,y))
#     pygame.display.update()

###############################################################

############## BARRIERS IN THE GAME MOVING ##############################
barrier1=pygame.Rect(20,60,150,20)
barrier2=pygame.Rect(400,60,100,20)
barrier3=pygame.Rect(1100,60,100,20)
barrier4=pygame.Rect(1330,100,20,150)#
barrier5=pygame.Rect(0,100,20,150)#
barrier6=pygame.Rect(0,680,280,20)
barrier7=pygame.Rect(670,350,240,20)

barrier1_x_speed=5
barrier2_x_speed=5
barrier3_x_speed=5
barrier4_y_speed=5
barrier5_y_speed=5
barrier6_x_speed=7
barrier7_x_speed=7

barrier1_x_speed_m=15
barrier2_x_speed_m=15
barrier3_x_speed_m=15
barrier4_y_speed_m=15
barrier5_y_speed_m=15
barrier6_x_speed_m=14
barrier7_x_speed_m=14


def bouncing_barrier(level):
    
    global barrier1_x_speed,barrier1_x_speed_m
    global barrier2_x_speed,barrier2_x_speed_m
    global barrier3_x_speed,barrier3_x_speed_m
    global barrier4_y_speed,barrier4_y_speed_m
    global barrier5_y_speed,barrier5_y_speed_m
    global barrier6_x_speed,barrier6_x_speed_m
    global barrier7_x_speed,barrier7_x_speed_m

    if level==1 or level==2:
        barrier1.x+=barrier1_x_speed
        if barrier1.left<=0:
            barrier1_x_speed=-barrier1_x_speed
        elif barrier1.right>=barrier2.left:
            barrier1_x_speed=-barrier1_x_speed

        barrier2.x+=barrier2_x_speed
        if barrier2.right>=barrier3.left:
            barrier2_x_speed=-barrier2_x_speed
        elif barrier2.left<=barrier1.right:
            barrier2_x_speed=-barrier2_x_speed
        barrier3.x+=barrier3_x_speed
        if barrier3.left<=barrier2.right:
            barrier3_x_speed=-barrier3_x_speed
        elif barrier3.right>=1350:
            barrier3_x_speed=-barrier3_x_speed

        barrier4.y+=barrier4_y_speed
        if barrier4.top<=0:
            barrier4_y_speed=-barrier4_y_speed
        elif barrier4.bottom>=700:
            barrier4_y_speed=-barrier4_y_speed

        barrier5.y-=barrier5_y_speed
        if barrier5.bottom>=700:
            barrier5_y_speed=-barrier5_y_speed
        elif barrier5.top<=0:
            barrier5_y_speed=-barrier5_y_speed

        barrier6.x+=barrier6_x_speed
        if barrier6.right>=1350:
            barrier6_x_speed=-barrier6_x_speed
        elif barrier6.left<=0:
            barrier6_x_speed=-barrier6_x_speed

        barrier7.x+=barrier7_x_speed
        if barrier7.right>=1350:
            barrier7_x_speed=-barrier7_x_speed
        elif barrier7.left<=0:
                barrier7_x_speed=-barrier7_x_speed
    
    elif level==3:
        barrier1.x+=barrier1_x_speed_m
        if barrier1.left<=0:
            barrier1_x_speed_m=-barrier1_x_speed_m
        elif barrier1.right>=barrier2.left:
            barrier1_x_speed_m=-barrier1_x_speed_m

        barrier2.x+=barrier2_x_speed_m
        if barrier2.right>=barrier3.left:
            barrier2_x_speed_m=-barrier2_x_speed_m
        elif barrier2.left<=barrier1.right:
            barrier2_x_speed_m=-barrier2_x_speed_m
        
        barrier3.x+=barrier3_x_speed_m
        if barrier3.left<=barrier2.right:
            barrier3_x_speed_m=-barrier3_x_speed_m
        elif barrier3.right>=1350:
            barrier3_x_speed_m=-barrier3_x_speed_m

        barrier4.y+=barrier4_y_speed_m
        if barrier4.top<=0:
            barrier4_y_speed_m=-barrier4_y_speed_m
        elif barrier4.bottom>=700:
            barrier4_y_speed_m=-barrier4_y_speed_m

        barrier5.y-=barrier5_y_speed_m
        if barrier5.bottom>=700:
            barrier5_y_speed_m=-barrier5_y_speed_m
        elif barrier5.top<=0:
            barrier5_y_speed_m=-barrier5_y_speed_m

        barrier6.x+=barrier6_x_speed_m
        if barrier6.right>=1350:
            barrier6_x_speed_m=-barrier6_x_speed_m
        elif barrier6.left<=0:
            barrier6_x_speed_m=-barrier6_x_speed_m

        barrier7.x+=barrier7_x_speed_m
        if barrier7.right>=1350:
            barrier7_x_speed_m=-barrier7_x_speed_m
        elif barrier7.left<=0:
                barrier7_x_speed_m=-barrier7_x_speed_m

    pygame.draw.rect(screen,white,barrier1)
    pygame.draw.rect(screen,white,barrier2)
    pygame.draw.rect(screen,white,barrier3)
    pygame.draw.rect(screen,white,barrier4)
    pygame.draw.rect(screen,white,barrier5)
    pygame.draw.rect(screen,white,barrier6)
    pygame.draw.rect(screen,white,barrier7)

    
##### Bullet part and spaceship part variable #####
loc_x=500
loc_y=500
velocity_x=0
velocity_y=0

# bullet=pygame.image.load("bullet.png")
# bullet=pygame.transform.scale(bullet,(40,40))
# bullet=pygame.transform.rotate(bullet,360)
# bullet_rect=bullet.get_rect()
# bullet_rect.x=650
# bullet_rect.y=600
bullet_velocity_y=0
bullet_velocity_x=0
bullet_state="ready"  #As bullet is ready to fire it out!

###############################################################


def fire_bullet(image,x,y):
    screen.blit(image,(x,y))

def game_start():
    
    sspace="rest"
    clock=pygame.time.Clock()
    end=False

    global loc_x
    global loc_y
    global velocity_x
    global velocity_y

    global bullet_state
    bullet=pygame.image.load("bullets.png")
    bullet=pygame.transform.scale(bullet,(40,40))
    bullet=pygame.transform.rotate(bullet,360)
    bullet_rect=bullet.get_rect()
    bullet_rect.x=0
    bullet_rect.y=0
    global bullet_velocity_y
    global bullet_velocity_x
    ##############################   
    ##############################
    bullet1_velocity_x=15
    bullet2_velocity_x=15
    bullet3_velocity_x=15
    bullet4_velocity_x=15

    rocket1_velocity_x=10
    rocket2_velocity_x=10
    rocket3_velocity_x=10
    rocket4_velocity_x=10

    
    rocket1=pygame.image.load("rocket1.png")
    rocket1=pygame.transform.scale(rocket1,(60,60))
    rocket1=pygame.transform.rotate(rocket1,270)
    rocket1_rect=rocket1.get_rect()
    rocket1_rect.x=60
    rocket1_rect.y=500

    bullet1=pygame.image.load("bullets.png")
    bullet1=pygame.transform.scale(bullet,(2,2))
    bullet1=pygame.transform.rotate(bullet,270)
    bullet1_rect=bullet1.get_rect()
    bullet1_rect.x=rocket1_rect.x+40
    bullet1_rect.y=rocket1_rect.y+10

    
    rocket2=pygame.image.load("rocket2.png")
    rocket2=pygame.transform.scale(rocket2,(60,60))
    rocket2=pygame.transform.rotate(rocket2,270)
    rocket2_rect=rocket2.get_rect()
    rocket2_rect.x=60
    rocket2_rect.y=175

    bullet2=pygame.image.load("bullets.png")
    bullet2=pygame.transform.scale(bullet,(2,2))
    bullet2=pygame.transform.rotate(bullet,270)
    bullet2_rect=bullet2.get_rect()
    bullet2_rect.x=rocket2_rect.x+40
    bullet2_rect.y=rocket2_rect.y+10
    
    rocket3=pygame.image.load("rocket3.png")
    rocket3=pygame.transform.scale(rocket3,(60,60))
    rocket3=pygame.transform.rotate(rocket3,90)
    rocket3_rect=rocket3.get_rect()
    rocket3_rect.x=1220
    rocket3_rect.y=500

    bullet3=pygame.image.load("bullets.png")
    bullet3=pygame.transform.scale(bullet,(2,2))
    bullet3=pygame.transform.rotate(bullet,90)
    bullet3_rect=bullet3.get_rect()
    bullet3_rect.x=rocket3_rect.x+40
    bullet3_rect.y=rocket3_rect.y+10

    rocket4=pygame.image.load("rocket4.png")
    rocket4=pygame.transform.scale(rocket4,(60,60))
    rocket4=pygame.transform.rotate(rocket4,90)
    rocket4_rect=rocket4.get_rect()
    rocket4_rect.x=1220
    rocket4_rect.y=175

    bullet4=pygame.image.load("bullets.png")
    bullet4=pygame.transform.scale(bullet,(2,2))
    bullet4=pygame.transform.rotate(bullet,90)
    bullet4_rect=bullet4.get_rect()
    bullet4_rect.x=rocket4_rect.x+40
    bullet4_rect.y=rocket4_rect.y+10

    
    
    screen.fill(black)
    spaceship=pygame.image.load("spaceship.png")
    spaceship=pygame.transform.scale(spaceship,(60,60))
    ship_rect=spaceship.get_rect()
    ship_rect.x=650
    ship_rect.y=600

    angle=0
    game_count=20

    count1=10
    count2=10
    count3=10
    count4=10
    
    level=1
    total_count=0
    enemy1="| Enemy1_Health="+str(int(count1))+" | "
    enemy2="  Enemy2_Health="+str(int(count2))+" | "
    enemy3="  Enemy3_Health="+str(int(count3))+" | "
    enemy4="  Enemy4_Health="+str(int(count4))+" | "
    game_level="GAME_LEVEL="+str(level)
    health="|Ship-Health|="+str(int(game_count))
    pygame.display.flip()
    
    while not end:
        screen.fill(black)     
        
        health="|Ship-Health|="+str(int(game_count))
        screen_font(health,1180,10,20,green)
        
        if count1>=0:
            enemy1="| Enemy1_Health="+str(int(count1))+" | "
        elif count1<0:
            enemy1="| Enemy_1_Down |"
        screen_font(enemy1,10,10,20,pink)
        
        if count2>=0:
            enemy2="  Enemy2_Health="+str(int(count2))+" | "
        elif count2<0:
            enemy2="| Enemy_2_Down |"
        screen_font(enemy2,200,10,20,gray)
        
        if count3>=0:
            enemy3="  Enemy3_Health="+str(int(count3))+" | "
        elif count3<0:
            enemy3="| Enemy_3_Down |"
        screen_font(enemy3,400,10,20,purple)
        
        if count4>=0:
            enemy4="  Enemy4_Health="+str(int(count4))+" | "
        elif count4<0:
            enemy4="| Enemy_4_Down |"
        screen_font(enemy4,600,10,20,white)

        game_level="GAME_LEVEL="+str(level)
        screen_font(game_level,850,10,20,yellow)
       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    sspace="move"
                    spaceship=pygame.image.load("spaceship.png")
                    spaceship=pygame.transform.scale(spaceship,(60,60))
                    spaceship=pygame.transform.rotate(spaceship,360)
                    velocity_y=-10
                    velocity_x=0
                    angle=360
                elif event.key==pygame.K_d:
                    sspace="move"
                    spaceship=pygame.image.load("spaceship.png")
                    spaceship=pygame.transform.scale(spaceship,(60,60))
                    spaceship=pygame.transform.rotate(spaceship,270)
                    velocity_y=0
                    velocity_x=10
                    angle=270
                elif event.key==pygame.K_s:
                    sspace="move"
                    spaceship=pygame.image.load("spaceship.png")
                    spaceship=pygame.transform.scale(spaceship,(60,60))
                    spaceship=pygame.transform.rotate(spaceship,180)
                    velocity_y=10
                    velocity_x=0
                    angle=180
                elif event.key==pygame.K_a:
                    sspace="move"
                    spaceship=pygame.image.load("spaceship.png")
                    spaceship=pygame.transform.scale(spaceship,(60,60))
                    spaceship=pygame.transform.rotate(spaceship,90)
                    velocity_y=0
                    velocity_x=-10
                    angle=90
                elif event.key==pygame.K_SPACE:
                    music_game("ship_firing.mp3")
                    bullet_state="fire"
                    bullet_rect.x=ship_rect.x+10
                    bullet_rect.y=ship_rect.y+10
                    if angle==360:
                        bullet=pygame.image.load("bullets.png")
                        bullet=pygame.transform.scale(bullet,(40,40))
                        bullet=pygame.transform.rotate(bullet,360)
                        bullet_velocity_y=-20
                        bullet_velocity_x=0
                    if angle==270:
                        bullet=pygame.image.load("bullets.png")
                        bullet=pygame.transform.scale(bullet,(40,40))
                        bullet=pygame.transform.rotate(bullet,270)
                        bullet_velocity_y=0
                        bullet_velocity_x=20
                    if angle==180:
                        bullet=pygame.image.load("bullets.png")
                        bullet=pygame.transform.scale(bullet,(40,40))
                        bullet=pygame.transform.rotate(bullet,180)
                        bullet_velocity_y=20
                        bullet_velocity_x=0
                    if angle==90:
                        bullet=pygame.image.load("bullets.png")
                        bullet=pygame.transform.scale(bullet,(40,40))
                        bullet=pygame.transform.rotate(bullet,90)
                        bullet_velocity_y=0
                        bullet_velocity_x=-20
                    elif angle==0:
                        bullet=pygame.image.load("bullets.png")
                        bullet=pygame.transform.scale(bullet,(40,40))
                        bullet=pygame.transform.rotate(bullet,360)
                        bullet_velocity_y=-20
                        bullet_velocity_x=0
 
        if ship_rect.x<=-70:
            ship_rect.x=1355
            ship_rect.x=ship_rect.x-15
        elif ship_rect.x>=1355:
            ship_rect.x=-70
            ship_rect.x=ship_rect.x+15
        elif ship_rect.y<=-60:
            ship_rect.y=700
            ship_rect.y=ship_rect.y-15
        elif ship_rect.y>=700:
            ship_rect.y=-60
            ship_rect.y=ship_rect.y+15
        else:
            ship_rect.x=ship_rect.x+velocity_x
            ship_rect.y=ship_rect.y+velocity_y 
        
        screen.blit(spaceship,(ship_rect.x,ship_rect.y))

        if level==1:

            bullet1_rect.x+=bullet1_velocity_x
            if bullet1_rect.x>=1350:
                bullet1_rect.x=70
            screen.blit(bullet1,(bullet1_rect.x,bullet1_rect.y))
            
            bullet2_rect.x+=bullet2_velocity_x
            if bullet2_rect.x>=1350:
                bullet2_rect.x=70
            screen.blit(bullet2,(bullet2_rect.x,bullet2_rect.y))
            
            bullet3_rect.x-=bullet3_velocity_x
            if bullet3_rect.x<=0:
                bullet3_rect.x=1220
            screen.blit(bullet3,(bullet3_rect.x,bullet3_rect.y))
            
            bullet4_rect.x-=bullet4_velocity_x
            if bullet4_rect.x<=0:
                bullet4_rect.x=1230
            screen.blit(bullet4,(bullet4_rect.x,bullet4_rect.y))
            
            screen.blit(rocket1,(rocket1_rect.x,rocket1_rect.y))
            screen.blit(rocket2,(rocket2_rect.x,rocket2_rect.y))
            screen.blit(rocket3,(rocket3_rect.x,rocket3_rect.y))
            screen.blit(rocket4,(rocket4_rect.x,rocket4_rect.y))

            if bullet1_rect.colliderect(ship_rect):
                pygame.draw.rect(screen,red,ship_rect,2)
                game_count=game_count-0.05
            if bullet2_rect.colliderect(ship_rect):
                pygame.draw.rect(screen,red,ship_rect,2)
                game_count=game_count-0.05
            elif bullet3_rect.colliderect(ship_rect):
                pygame.draw.rect(screen,red,ship_rect,2)
                game_count=game_count-0.05
            elif bullet4_rect.colliderect(ship_rect):
                pygame.draw.rect(screen,red,ship_rect,2)
                game_count=game_count-0.05
            
            bouncing_barrier(level)
        
        elif level==2:
            
            bullet1_velocity_x=0
            bullet2_velocity_x=0
            bullet3_velocity_x=0
            bullet4_velocity_x=0
            
            screen.blit(bullet1,(-5000,1200))
            screen.blit(bullet2,(-5000,-1000))
            screen.blit(bullet3,(1800,1000))
            screen.blit(bullet4,(1800,-1000))

            rocket1_rect.x=rocket1_rect.x+rocket1_velocity_x
            if rocket1_rect.right>=1300:
                rocket1=pygame.transform.flip(rocket1,True,False)
                rocket1_velocity_x=-15
            elif rocket1_rect.left<=10:
                rocket1=pygame.transform.flip(rocket1,True,False)
                rocket1_velocity_x=15
            screen.blit(rocket1,(rocket1_rect.x,rocket1_rect.y))

            rocket2_rect.x=rocket2_rect.x+rocket2_velocity_x
            if rocket2_rect.right>=1300:
                rocket2=pygame.transform.flip(rocket2,True,False)
                rocket2_velocity_x=-15
            elif rocket2_rect.left<=10:
                rocket2=pygame.transform.flip(rocket2,True,False)
                rocket2_velocity_x=15
            screen.blit(rocket2,(rocket2_rect.x,rocket2_rect.y))

            rocket3_rect.x=rocket3_rect.x-rocket3_velocity_x
            if rocket3_rect.right>=1300:
                rocket3=pygame.transform.flip(rocket3,True,False)
                rocket3_velocity_x=15
            elif rocket3_rect.left<=10:
                rocket3=pygame.transform.flip(rocket3,True,False)
                rocket3_velocity_x=-15
            screen.blit(rocket3,(rocket3_rect.x,rocket3_rect.y))

            rocket4_rect.x=rocket4_rect.x-rocket4_velocity_x
            if rocket4_rect.right>=1300:
                rocket4=pygame.transform.flip(rocket4,True,False)
                rocket4_velocity_x=15
            elif rocket4_rect.left<=10:
                rocket4=pygame.transform.flip(rocket4,True,False)
                rocket4_velocity_x=-15
            screen.blit(rocket4,(rocket4_rect.x,rocket4_rect.y))

            bouncing_barrier(level)
        
        elif level==3:
            
            rocket1_rect.x=rocket1_rect.x+rocket1_velocity_x
            if rocket1_rect.right>=1300:
                rocket1=pygame.transform.flip(rocket1,True,False)
                rocket1_velocity_x=-15
            elif rocket1_rect.left<=10:
                rocket1=pygame.transform.flip(rocket1,True,False)
                rocket1_velocity_x=15
            screen.blit(rocket1,(rocket1_rect.x,rocket1_rect.y))

            rocket2_rect.x=rocket2_rect.x+rocket2_velocity_x
            if rocket2_rect.right>=1300:
                rocket2=pygame.transform.flip(rocket2,True,False)
                rocket2_velocity_x=-15
            elif rocket2_rect.left<=10:
                rocket2=pygame.transform.flip(rocket2,True,False)
                rocket2_velocity_x=15
            screen.blit(rocket2,(rocket2_rect.x,rocket2_rect.y))

            rocket3_rect.x=rocket3_rect.x-rocket3_velocity_x
            if rocket3_rect.right>=1300:
                rocket3=pygame.transform.flip(rocket3,True,False)
                rocket3_velocity_x=15
            elif rocket3_rect.left<=10:
                rocket3=pygame.transform.flip(rocket3,True,False)
                rocket3_velocity_x=-15
            screen.blit(rocket3,(rocket3_rect.x,rocket3_rect.y))

            rocket4_rect.x=rocket4_rect.x-rocket4_velocity_x
            if rocket4_rect.right>=1300:
                rocket4=pygame.transform.flip(rocket4,True,False)
                rocket4_velocity_x=15
            elif rocket4_rect.left<=10:
                rocket4=pygame.transform.flip(rocket4,True,False)
                rocket4_velocity_x=-15
            screen.blit(rocket4,(rocket4_rect.x,rocket4_rect.y))

            if bullet1_rect.colliderect(ship_rect):
                pygame.draw.rect(screen,red,ship_rect,2)
                game_count=game_count-0.05
            if bullet2_rect.colliderect(ship_rect):
                pygame.draw.rect(screen,red,ship_rect,2)
                game_count=game_count-0.05
            elif bullet3_rect.colliderect(ship_rect):
                pygame.draw.rect(screen,red,ship_rect,2)
                game_count=game_count-0.05
            elif bullet4_rect.colliderect(ship_rect):
                pygame.draw.rect(screen,red,ship_rect,2)
                game_count=game_count-0.05
            
            bouncing_barrier(level)
            

        if ship_rect.colliderect(barrier1):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        elif ship_rect.colliderect(barrier2):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        elif ship_rect.colliderect(barrier3):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        elif ship_rect.colliderect(barrier4):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        elif ship_rect.colliderect(barrier5):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        elif ship_rect.colliderect(barrier6):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        elif ship_rect.colliderect(barrier7):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05

        elif ship_rect.colliderect(rocket1_rect):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        elif ship_rect.colliderect(rocket2_rect):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        elif ship_rect.colliderect(rocket3_rect):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        elif ship_rect.colliderect(rocket4_rect):
            pygame.draw.rect(screen,red,ship_rect,2)
            game_count=game_count-0.05
        
        if bullet_state=="ready":
            pass
        elif (bullet_state=="fire") or (sspace=="move"):
            if bullet_rect.x<=-70:
                bullet_state="ready"
            elif bullet_rect.x>=1355:
                bullet_state="ready"
            elif bullet_rect.y<=-60:
                bullet_state="ready"
            elif bullet_rect.y>=700:
                bullet_state="ready"
            else:
                bullet_rect.x=bullet_rect.x+bullet_velocity_x
                bullet_rect.y=bullet_rect.y+bullet_velocity_y 
            bullet_rect.x=bullet_rect.x+bullet_velocity_x
            bullet_rect.y=bullet_rect.y+bullet_velocity_y 
            fire_bullet(bullet,bullet_rect.x,bullet_rect.y)
        else:
            pass

        if bullet_rect.colliderect(rocket1_rect):
            pygame.draw.rect(screen,blue,rocket1_rect,2)
            count1=count1-0.5
            if count1==0:
                count1=0
                total_count=total_count+1
            elif count1<0:
                bullet1_velocity_x=0
                bullet1_rect.x=-500
              
        elif bullet_rect.colliderect(rocket2_rect):
            pygame.draw.rect(screen,blue,rocket2_rect,2)
            count2=count2-0.5
            if count2==0:
                count2=0
                total_count=total_count+1
            elif count2<0:
                bullet2_velocity_x=0
                bullet2_rect.x=-500
                
        elif bullet_rect.colliderect(rocket3_rect):
            pygame.draw.rect(screen,blue,rocket3_rect,2)
            count3=count3-0.5
            if count3==0:
                count3=0
                total_count=total_count+1
            elif count3<0:
                bullet3_velocity_x=0
                bullet3_rect.x=1800
                
        elif bullet_rect.colliderect(rocket4_rect):
            pygame.draw.rect(screen,blue,rocket4_rect,2)
            count4=count4-0.5
            if count4==0:
                count4=0
                total_count=total_count+1
            elif count4<0:
                bullet4_velocity_x=0
                bullet4_rect.x=1800
               
        
        ######## DECIDING GAME LEVEL INCREMENT #############
        if total_count>=4:
            level=level+1

            if level==2:
                spaceship=pygame.transform.rotate(spaceship,360)
                ship_rect.x=650
                ship_rect.y=600
                velocity_x=0
                velocity_y=0
                screen.blit(spaceship,(ship_rect.x,ship_rect.y))
                game_count=10
                total_count=0

                count1=10
                count2=10
                count3=10
                count4=10

                screen.fill(black)
                screen_font("GAME LEVEL 2",650,350,50,(0,255,0))
                screen_font("BE READY",650,450,45,blue)
                pygame.display.flip()
                time.sleep(2)

            elif level==3:
                spaceship=pygame.transform.rotate(spaceship,360)
                ship_rect.x=650
                ship_rect.y=600
                velocity_x=0
                velocity_y=0
                screen.blit(spaceship,(ship_rect.x,ship_rect.y))

                rocket1_rect.x=60
                rocket1_rect.y=500
                bullet1_rect.x=rocket1_rect.x+40
                bullet1_rect.y=rocket1_rect.y+10

                rocket2_rect.x=60
                rocket2_rect.y=175
                bullet2_rect.x=rocket2_rect.x+40
                bullet2_rect.y=rocket2_rect.y+10

                rocket3_rect.x=1220
                rocket3_rect.y=500
                bullet3_rect.x=rocket3_rect.x+40
                bullet3_rect.y=rocket3_rect.y+10

                rocket4_rect.x=1220
                rocket4_rect.y=175
                bullet4_rect.x=rocket4_rect.x+40
                bullet4_rect.y=rocket4_rect.y+10
                
                spaceship=pygame.transform.rotate(spaceship,360)
                ship_rect.x=650
                ship_rect.y=600
                velocity_x=0
                velocity_y=0
                screen.blit(spaceship,(ship_rect.x,ship_rect.y))
                game_count=10
                total_count=0

                count1=10
                count2=10
                count3=10
                count4=10

                screen.fill(black)
                screen_font("GAME LEVEL 3",650,350,50,(0,255,0))
                screen_font("BE READY For Finishing the Game",450,450,45,blue)
                screen_font("With Crazy Speed Attacks!",450,550,45,blue)
                pygame.display.flip()
                time.sleep(2)


            elif level==4:
                level=0
                spaceship=pygame.transform.rotate(spaceship,360)
                ship_rect.x=650
                ship_rect.y=600
                velocity_x=0
                velocity_y=0
                screen.blit(spaceship,(ship_rect.x,ship_rect.y))
                
                count1=10
                count2=10
                count3=10
                count4=10
                
                end=pygame.image.load("end_image.jpg")
                screen.blit(end,(0,0))
                pygame.display.flip()
                time.sleep(0.5)
                screen_font("C",480,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("O",510,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("N",550,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("G",585,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("R",615,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("A",645,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("T",675,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("U",705,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("L",735,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("A",765,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("T",795,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("I",825,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("O",855,100,45,(0,255,0))
                time.sleep(0.5)
                pygame.display.update()
                screen_font("N",885,100,45,(0,255,0))
                time.sleep(1)
                pygame.display.update()
                time.sleep(2)
                screen_font("You Successfully clear all the level",450,300,40,(0,255,0))
                pygame.display.update()
                time.sleep(3)
                game_options()
                
        else:
            pass

#################### Bullet Working #######################
        
        if game_count<=0:
            screen.fill(black)
            music_game("failure.mp3")
            screen_font("GAME OVER !!!",675,350,60,blue)
            ship_rect.x=650
            ship_rect.y=600
            velocity_y=0
            velocity_x=0
            pygame.display.flip()
            time.sleep(2)
            game_count=10
            game_options()
            break
        pygame.display.update()
        clock.tick(60)
    
########################  Main Execution of the Game #############################

while True:
    pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if((pos[0]>=564 and pos[0]<=654) and (pos[1]>=164 and pos[1]<=257)):
                l,m,r=pygame.mouse.get_pressed()
                music_game("click_sound.mp3")
                time.sleep(1)
                if l:
                    game_mannual()

            elif((pos[0]>=557 and pos[0]<=660) and (pos[1]>=346 and pos[1]<=437)):
                l,m,r=pygame.mouse.get_pressed()
                music_game("start_sound.mp3")
                time.sleep(2)
                mixer.music.stop()
                if l:
                    screen.fill(black)
                    screen_font("GAME LEVEL 1",650,350,45,(0,255,0))
                    screen_font("BE READY FOR MISSION",650,480,45,blue)
                    pygame.display.update()
                    game_start() 

            elif((pos[0]>=559 and pos[0]<=658) and (pos[1]>=526 and pos[1]<=618)):
                l,m,r=pygame.mouse.get_pressed()
                music_game("click_sound.mp3")
                time.sleep(1)
                mixer.music.stop()
                if l:
                    screen.fill(white)
                    mixer.music.stop()
                    music_game("end_music.mp3")
                    screen_background("space_end.jpg",-40,0)
                    screen_font("Thank you for playing, See You Soon !!!",200,220,50,white)
                    pygame.display.flip()
                    time.sleep(6)
                    exit()
        
       
    
            
