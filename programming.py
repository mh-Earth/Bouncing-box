import pygame
import random
import math
import time


pygame.mixer.init()
screen_hight=800
screen_wight=800
display=pygame.display.set_mode((screen_hight,screen_wight))
pygame.display.set_caption('Social media in a box')
clock=pygame.time.Clock()
running=True
size=100
max_ran=30

# pygame.mixer.music.load('')

python_x=random.randint(0,600-size)
python_y=random.randint(0,600-size)

python_x_v=random.randint(10,max_ran)
python_y_v=10
# _________________
java_x=random.randint(0,600-size)
java_y=random.randint(0,600-size)

java_x_v=random.randint(10,max_ran)
java_y_v=10
# _________________
javascript_x=random.randint(0,600-size)
javascript_y=random.randint(0,600-size)

javascript_x_v=random.randint(10,max_ran)
javascript_y_v=10
# _________________
cpp_x=random.randint(0,600-size)
cpp_y=random.randint(0,600-size)

cpp_x_v=random.randint(10,max_ran)
cpp_y_v=10
# _________________
c_x=random.randint(0,600-size)
c_y=random.randint(0,600-size)

c_x_v=random.randint(10,max_ran)
c_y_v=10
# _________________
swift_x=random.randint(0,600-size)
swift_y=random.randint(0,600-size)

swift_x_v=random.randint(10,max_ran)
swift_y_v=10
# _________________
ruby_x=random.randint(0,600-size)
ruby_y=random.randint(0,600-size)

ruby_x_v=random.randint(10,max_ran)
ruby_y_v=10
# _________________
pygame.mixer.set_num_channels(20)
position_list=[[python_x,python_y],[java_x,java_y],[javascript_x,javascript_y],[cpp_x,cpp_y],[c_x,c_y]]

box=pygame.image.load('box.PNG')
box=pygame.transform.scale(box,(screen_hight+40,screen_wight+40))

img=pygame.image.load('python.PNG')
img=pygame.transform.scale(img, (size,size))

img2=pygame.image.load('java.PNG')
img2=pygame.transform.scale(img2, (size,size))

img3=pygame.image.load('javascript.PNG')
img3=pygame.transform.scale(img3, (size,size))

img4=pygame.image.load('c++.PNG')
img4=pygame.transform.scale(img4, (size,size))

img5=pygame.image.load('c.PNG')
img5=pygame.transform.scale(img5, (size,size))

img6=pygame.image.load('swift.PNG')
img6=pygame.transform.scale(img6, (size,size))

img7=pygame.image.load('ruby.PNG')
img7=pygame.transform.scale(img7, (size,size))

pygame.display.set_icon(img)

while running:
    # display.fill((0,0,0))
    display.blit(box,(-25,-23))
    # colliding()
    if python_x>screen_hight-size:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('bounce.mp3'))
        python_x_v=random.randint(10,max_ran)
        python_x_v=python_x_v*-1

    if python_y>screen_hight-size:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('bounce.mp3'))
        python_y_v=random.randint(10,max_ran)
        python_y_v=python_y_v*-1

    if python_x<0:
        pygame.mixer.Channel(8).play(pygame.mixer.Sound('bounce.mp3'))
        python_x_v=python_x_v*-1

    if python_y<0:
        pygame.mixer.Channel(8).play(pygame.mixer.Sound('bounce.mp3'))
        python_y_v=python_y_v*-1

    if java_x>screen_hight-size:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('bounce.mp3'))
        java_x_v=random.randint(10,max_ran)
        java_x_v=java_x_v*-1

    if java_y>screen_hight-size:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('bounce.mp3'))
        java_y_v=random.randint(10,max_ran)
        java_y_v=java_y_v*-1

    if java_x<0:
        pygame.mixer.Channel(9).play(pygame.mixer.Sound('bounce.mp3'))
        java_x_v=java_x_v*-1

    if java_y<0:
        pygame.mixer.Channel(9).play(pygame.mixer.Sound('bounce.mp3'))
        java_y_v=java_y_v*-1

    if javascript_x>screen_hight-size:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('bounce.mp3'))
        javascript_x_v=random.randint(10,max_ran)
        javascript_x_v=javascript_x_v*-1

    if javascript_y>screen_hight-size:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('bounce.mp3'))
        javascript_y_v=random.randint(10,max_ran)
        javascript_y_v=javascript_y_v*-1

    if javascript_x<0:
        pygame.mixer.Channel(10).play(pygame.mixer.Sound('bounce.mp3'))
        javascript_x_v=javascript_x_v*-1

    if javascript_y<0:
        pygame.mixer.Channel(10).play(pygame.mixer.Sound('bounce.mp3'))
        javascript_y_v=javascript_y_v*-1

    if cpp_x>screen_hight-size:
        pygame.mixer.Channel(3).play(pygame.mixer.Sound('bounce.mp3'))
        cpp_x_v=random.randint(10,max_ran)
        cpp_x_v=cpp_x_v*-1

    if cpp_y>screen_hight-size:
        pygame.mixer.Channel(3).play(pygame.mixer.Sound('bounce.mp3'))
        cpp_y_v=random.randint(10,max_ran)
        cpp_y_v=cpp_y_v*-1

    if cpp_x<0:
        pygame.mixer.Channel(11).play(pygame.mixer.Sound('bounce.mp3'))
        cpp_x_v=cpp_x_v*-1

    if cpp_y<0:
        pygame.mixer.Channel(11).play(pygame.mixer.Sound('bounce.mp3'))
        cpp_y_v=cpp_y_v*-1

    if c_x>screen_hight-size:
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('bounce.mp3'))
        c_x_v=random.randint(10,max_ran)
        c_x_v=c_x_v*-1

    if c_y>screen_hight-size:
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('bounce.mp3'))
        c_y_v=random.randint(10,max_ran)
        c_y_v=c_y_v*-1

    if c_x<0:
        pygame.mixer.Channel(12).play(pygame.mixer.Sound('bounce.mp3'))
        c_x_v=c_x_v*-1

    if c_y<0:
        pygame.mixer.Channel(12).play(pygame.mixer.Sound('bounce.mp3'))
        c_y_v=c_y_v*-1

    if swift_x>screen_hight-size:
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('bounce.mp3'))
        swift_x_v=random.randint(10,max_ran)
        swift_x_v=swift_x_v*-1

    if swift_y>screen_hight-size:
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('bounce.mp3'))
        swift_y_v=random.randint(10,max_ran)
        swift_y_v=swift_y_v*-1

    if swift_x<0:
        pygame.mixer.Channel(13).play(pygame.mixer.Sound('bounce.mp3'))
        swift_x_v=swift_x_v*-1

    if swift_y<0:
        pygame.mixer.Channel(13).play(pygame.mixer.Sound('bounce.mp3'))
        swift_y_v=swift_y_v*-1

    if ruby_x>screen_hight-size:
        pygame.mixer.Channel(7).play(pygame.mixer.Sound('bounce.mp3'))
        ruby_x_v=random.randint(10,max_ran)
        ruby_x_v=ruby_x_v*-1

    if ruby_y>screen_hight-size:
        pygame.mixer.Channel(7).play(pygame.mixer.Sound('bounce.mp3'))
        ruby_y_v=random.randint(10,max_ran)
        ruby_y_v=ruby_y_v*-1

    if ruby_x<0:
        pygame.mixer.Channel(14).play(pygame.mixer.Sound('bounce.mp3'))
        ruby_x_v=ruby_x_v*-1

    if ruby_y<0:
        pygame.mixer.Channel(14).play(pygame.mixer.Sound('bounce.mp3'))
        ruby_y_v=ruby_y_v*-1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_position=pygame.mouse.get_pos()
            if event.button== 1:
                # for positions in position_list:

                python_x=mouse_position[0]-size/2
                python_y=mouse_position[1]-size/2
                python_y_v=0
                python_x_v=0

                ruby_x=mouse_position[0]-size/2
                ruby_y=mouse_position[1]-size/2
                ruby_y_v=0
                ruby_x_v=0

                javascript_x=mouse_position[0]-size/2
                javascript_y=mouse_position[1]-size/2
                javascript_y_v=0
                javascript_x_v=0

                c_x=mouse_position[0]-size/2
                c_y=mouse_position[1]-size/2
                c_y_v=0
                c_x_v=0

                cpp_x=mouse_position[0]-size/2
                cpp_y=mouse_position[1]-size/2
                cpp_y_v=0
                cpp_x_v=0

                swift_x=mouse_position[0]-size/2
                swift_y=mouse_position[1]-size/2
                swift_y_v=0
                swift_x_v=0

                java_x=mouse_position[0]-size/2
                java_y=mouse_position[1]-size/2
                java_y_v=0
                java_x_v=0
        elif event.type==pygame.MOUSEBUTTONUP:
            
            python_y_v=random.randint(10,max_ran)
            python_x_v=random.randint(10,max_ran)

            c_y_v=random.randint(10,max_ran)
            c_x_v=random.randint(10,max_ran)

            cpp_y_v=random.randint(10,max_ran)
            cpp_x_v=random.randint(10,max_ran)

            javascript_y_v=random.randint(10,max_ran)
            javascript_x_v=random.randint(10,max_ran)

            java_y_v=random.randint(10,max_ran)
            java_x_v=random.randint(10,max_ran)

            swift_y_v=random.randint(10,max_ran)
            swift_x_v=random.randint(10,max_ran)

            ruby_y_v=random.randint(10,max_ran)
            ruby_x_v=random.randint(10,max_ran)
            # if mouse_position[0]-im and mouse_position[1]:
            #     pass
    display.blit(img,(python_x,python_y))
    display.blit(img2,(java_x,java_y))
    display.blit(img3,(javascript_x,javascript_y))
    display.blit(img4,(cpp_x,cpp_y))
    display.blit(img5,(c_x,c_y))
    display.blit(img6,(swift_x,swift_y))
    display.blit(img7,(ruby_x,ruby_y))
    

    python_x+=python_x_v
    python_y+=python_y_v

    java_x+=java_x_v
    java_y+=java_y_v

    javascript_x+=javascript_x_v
    javascript_y+=javascript_y_v

    cpp_x+=cpp_x_v
    cpp_y+=cpp_y_v

    c_x+=c_x_v
    c_y+=c_y_v

    swift_x+=swift_x_v
    swift_y+=swift_y_v

    ruby_x+=ruby_x_v
    ruby_y+=ruby_y_v
    clock.tick(40)
    pygame.display.update()

