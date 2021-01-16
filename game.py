import pygame
import random
import math
import time
display=pygame.display.set_mode((800,800))
pygame.display.set_caption('game')
clock=pygame.time.Clock()
running=True

instra_x=200
instra_y=500

instra_x_v=10
instra_y_v=10
# _________________
facebook_x=500
facebook_y=400

facebook_x_v=10
facebook_y_v=10
# _________________
youtube_x=500
youtube_y=400

youtube_x_v=10
youtube_y_v=10
# _________________
skype_x=500
skype_y=400

skype_x_v=10
skype_y_v=10
# _________________
twitter_x=500
twitter_y=400

twitter_x_v=10
twitter_y_v=10
# _________________

position_list=[[instra_x,instra_y],[facebook_x,facebook_y],[youtube_x,youtube_y],[skype_x,skype_y],[twitter_x,twitter_y]]
size=100
max_ran=30

img=pygame.image.load('instagram.PNG')
img=pygame.transform.scale(img, (size,size))

img2=pygame.image.load('facebook.PNG')
img2=pygame.transform.scale(img2, (size,size))

img3=pygame.image.load('youtube.PNG')
img3=pygame.transform.scale(img3, (size,size))

img4=pygame.image.load('skype.PNG')
img4=pygame.transform.scale(img4, (size,size))

img5=pygame.image.load('twitter.PNG')
img5=pygame.transform.scale(img5, (size,size))


def calculateDistance(x1,y1,x2,y2):
    global dist
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(dist)
    return dist
def colliding():
    global instra_x,instra_x_v,instra_y,instra_y_v, facebook_y_v,facebook_x_v,facebook_x,facebook_y
    pygame.draw.rect(display, ((0,255,255)), ((facebook_x,facebook_y),(5,5)),5) #left up^
    pygame.draw.rect(display, ((255,255,0)), ((facebook_x+200,facebook_y),(5,5)),5) #right up*
    pygame.draw.rect(display, ((0,255,0)), ((facebook_x+200,facebook_y+200),(5,5)),5) #right down>
    pygame.draw.rect(display, ((255,0,0)), ((facebook_x,facebook_y+200),(5,5)),5) #left down

    pygame.draw.rect(display, ((0,255,255)), ((instra_x,instra_y),(5,5)),5) #left up^
    pygame.draw.rect(display, ((255,255,0)), ((instra_x+200,instra_y),(5,5)),5) #right up*
    pygame.draw.rect(display, ((0,255,0)), ((instra_x+200,instra_y+200),(5,5)),5) #right down>
    pygame.draw.rect(display, ((255,0,0)), ((instra_x,instra_y+200),(5,5)),5) #left down

    # pygame.draw.rect(display, ((0,255,255)), ((facebook_x+100,facebook_y),(5,5)),5) #cyan up^
    # pygame.draw.rect(display, ((255,255,0)), ((facebook_x,facebook_y+100),(5,5)),5) #yellow left*
    # pygame.draw.rect(display, ((0,255,0)), ((facebook_x+200,facebook_y+100),(5,5)),5) #green right>
    # pygame.draw.rect(display, ((255,0,0)), ((facebook_x+100,facebook_y+200),(5,5)),5) #red down
    
    # pygame.draw.rect(display, ((0,255,255)), ((instra_x+100,instra_y),(5,5)),5)  #cyan up
    # pygame.draw.rect(display, ((255,255,0)), ((instra_x,instra_y+100),(5,5)),5) #yellow left>
    # pygame.draw.rect(display, ((0,255,0)), ((instra_x+200,instra_y+100),(5,5)),5) #green right*
    # pygame.draw.rect(display, ((255,0,0)), ((instra_x+100,instra_y+200),(5,5)),5) #red down^


    if calculateDistance(instra_x+100,instra_y,facebook_x+100,facebook_y+200)<=20: #du done
        instra_y_v=instra_y_v*-1
        facebook_y_v=facebook_y_v*-1

    if calculateDistance(facebook_x,facebook_y+100,instra_x+200,instra_y+100)<=20: #lr
        instra_x_v=instra_x_v*-1
        facebook_x_v=facebook_x_v*-1
        # time.sleep(2)

    if calculateDistance(facebook_x+200,facebook_y+100,instra_x,instra_y+100)<=20: #rl2
        print("work")
        time.sleep(2)
        instra_x_v=instra_x_v*-1
        facebook_x_v=facebook_x_v*-1
        
    if calculateDistance(facebook_x+100,facebook_y,instra_x+100,instra_y+200)<=20: #ud
        instra_y_v=instra_y_v*-1
        facebook_y_v=facebook_y_v*-1

def mouseHold():
    pass

while running:
    display.fill((0,0,0))
    # colliding()
    if instra_x>800-size:
        instra_x_v=random.randint(10,max_ran)
        instra_x_v=instra_x_v*-1

    if instra_y>800-size:
        instra_y_v=random.randint(10,max_ran)
        instra_y_v=instra_y_v*-1

    if instra_x<0:
        instra_x_v=instra_x_v*-1

    if instra_y<0:
        instra_y_v=instra_y_v*-1

    if facebook_x>800-size:
        facebook_x_v=random.randint(10,max_ran)
        facebook_x_v=facebook_x_v*-1

    if facebook_y>800-size:
        facebook_y_v=random.randint(10,max_ran)
        facebook_y_v=facebook_y_v*-1

    if facebook_x<0:
        facebook_x_v=facebook_x_v*-1

    if facebook_y<0:
        facebook_y_v=facebook_y_v*-1

    if youtube_x>800-size:
        youtube_x_v=random.randint(10,max_ran)
        youtube_x_v=youtube_x_v*-1

    if youtube_y>800-size:
        youtube_y_v=random.randint(10,max_ran)
        youtube_y_v=youtube_y_v*-1

    if youtube_x<0:
        youtube_x_v=youtube_x_v*-1

    if youtube_y<0:
        youtube_y_v=youtube_y_v*-1

    if skype_x>800-size:
        skype_x_v=random.randint(10,max_ran)
        skype_x_v=skype_x_v*-1

    if skype_y>800-size:
        skype_y_v=random.randint(10,max_ran)
        skype_y_v=skype_y_v*-1

    if skype_x<0:
        skype_x_v=skype_x_v*-1

    if skype_y<0:
        skype_y_v=skype_y_v*-1

    if twitter_x>800-size:
        twitter_x_v=random.randint(10,max_ran)
        twitter_x_v=twitter_x_v*-1

    if twitter_y>800-size:
        twitter_y_v=random.randint(10,max_ran)
        twitter_y_v=twitter_y_v*-1

    if twitter_x<0:
        twitter_x_v=twitter_x_v*-1

    if twitter_y<0:
       twitter_y_v=twitter_y_v*-1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_position=pygame.mouse.get_pos()
            if event.button== 1:
                # if
                instra_x=mouse_position[0]-size/2
                instra_y=mouse_position[1]-size/2
                instra_y_v=0
                instra_x_v=0
        elif event.type==pygame.MOUSEBUTTONUP:
            instra_y_v=random.randint(10,max_ran)
            instra_x_v=random.randint(10,max_ran)
            # if mouse_position[0]-im and mouse_position[1]:
            #     pass
    display.blit(img,(instra_x,instra_y))
    display.blit(img2,(facebook_x,facebook_y))
    display.blit(img3,(youtube_x,youtube_y))
    display.blit(img4,(skype_x,skype_y))
    display.blit(img5,(twitter_x,twitter_y))
    

    instra_x+=instra_x_v
    instra_y+=instra_y_v

    facebook_x+=facebook_x_v
    facebook_y+=facebook_y_v

    youtube_x+=youtube_x_v
    youtube_y+=youtube_y_v

    skype_x+=skype_x_v
    skype_y+=skype_y_v

    twitter_x+=twitter_x_v
    twitter_y+=twitter_y_v
    clock.tick(40)
    pygame.display.update()

