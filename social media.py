import pygame
import random
import math
import time
screen_hight=800
screen_wight=800
display=pygame.display.set_mode((screen_hight,screen_wight))
pygame.display.set_caption('Social media in a box')
clock=pygame.time.Clock()
running=True
size=100
max_ran=30

instra_x=random.randint(0,600-size)
instra_y=random.randint(0,600-size)

instra_x_v=random.randint(10,max_ran)
instra_y_v=10
# _________________
facebook_x=random.randint(0,600-size)
facebook_y=random.randint(0,600-size)

facebook_x_v=random.randint(10,max_ran)
facebook_y_v=10
# _________________
youtube_x=random.randint(0,600-size)
youtube_y=random.randint(0,600-size)

youtube_x_v=random.randint(10,max_ran)
youtube_y_v=10
# _________________
skype_x=random.randint(0,600-size)
skype_y=random.randint(0,600-size)

skype_x_v=random.randint(10,max_ran)
skype_y_v=10
# _________________
twitter_x=random.randint(0,600-size)
twitter_y=random.randint(0,600-size)

twitter_x_v=random.randint(10,max_ran)
twitter_y_v=10
# _________________

position_list=[[instra_x,instra_y],[facebook_x,facebook_y],[youtube_x,youtube_y],[skype_x,skype_y],[twitter_x,twitter_y]]

box=pygame.image.load('box.PNG')
box=pygame.transform.scale(box,(screen_hight+40,screen_wight+40))

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

pygame.display.set_icon(img)

while running:
    # display.fill((0,0,0))
    display.blit(box,(-25,-23))
    # colliding()
    if instra_x>screen_hight-size:
        instra_x_v=random.randint(10,max_ran)
        instra_x_v=instra_x_v*-1

    if instra_y>screen_hight-size:
        instra_y_v=random.randint(10,max_ran)
        instra_y_v=instra_y_v*-1

    if instra_x<0:
        instra_x_v=instra_x_v*-1

    if instra_y<0:
        instra_y_v=instra_y_v*-1

    if facebook_x>screen_hight-size:
        facebook_x_v=random.randint(10,max_ran)
        facebook_x_v=facebook_x_v*-1

    if facebook_y>screen_hight-size:
        facebook_y_v=random.randint(10,max_ran)
        facebook_y_v=facebook_y_v*-1

    if facebook_x<0:
        facebook_x_v=facebook_x_v*-1

    if facebook_y<0:
        facebook_y_v=facebook_y_v*-1

    if youtube_x>screen_hight-size:
        youtube_x_v=random.randint(10,max_ran)
        youtube_x_v=youtube_x_v*-1

    if youtube_y>screen_hight-size:
        youtube_y_v=random.randint(10,max_ran)
        youtube_y_v=youtube_y_v*-1

    if youtube_x<0:
        youtube_x_v=youtube_x_v*-1

    if youtube_y<0:
        youtube_y_v=youtube_y_v*-1

    if skype_x>screen_hight-size:
        skype_x_v=random.randint(10,max_ran)
        skype_x_v=skype_x_v*-1

    if skype_y>screen_hight-size:
        skype_y_v=random.randint(10,max_ran)
        skype_y_v=skype_y_v*-1

    if skype_x<0:
        skype_x_v=skype_x_v*-1

    if skype_y<0:
        skype_y_v=skype_y_v*-1

    if twitter_x>screen_hight-size:
        twitter_x_v=random.randint(10,max_ran)
        twitter_x_v=twitter_x_v*-1

    if twitter_y>screen_hight-size:
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
                # for positions in position_list:

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

