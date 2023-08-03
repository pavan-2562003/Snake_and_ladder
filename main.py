import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((750, 550))
pygame.display.set_caption("Snake and Ladder")

bcking = pygame.image.load("bg_snake.jpg")
stg=pygame.image.load("wood finish.jpg")
arrow=pygame.image.load("arrow-forward.png")
bx = 200
by = 10

#players
r1=pygame.image.load("user avatar yellow.png")
b1=pygame.image.load("user avatar green.png")


rx=100
ry=251

b1x=100
b1y=362

button=pygame.Rect(10,50,40,40)


#font size
font1=pygame.font.SysFont("comicsansms",25)
font2=pygame.font.SysFont("comicsansms",20)


def bck():
    screen.blit(stg, (0, 0))
    screen.blit(bcking, (bx, by))
    screen.blit(arrow, (10, 25))
def rplayer(x,y):
    screen.blit(r1,(x,y))
def bplayer(x,y):
    screen.blit(b1,(x,y))
def pickNumber():
    diceroll=random.randint(1,6)
    if diceroll==1:
        dice=pygame.image.load("dice1.png")
    elif diceroll == 2:
            dice = pygame.image.load("dice2.png")
    elif diceroll == 3:
            dice = pygame.image.load("dice3.png")
    elif diceroll == 4:
            dice = pygame.image.load("dice4.png")
    elif diceroll == 5:
            dice = pygame.image.load("dice5.png")
    elif diceroll == 6:
            dice = pygame.image.load("dice6.png")
    return (dice,diceroll)


def players():
    msg1=font1.render("Player 1",True,(255, 255, 255))
    screen.blit(msg1,[5,251])
    msg2 = font1.render("Player 2",True,(200, 255, 200))
    screen.blit(msg2, [5, 362])

def rollr():
    msg3=font2.render("Your Turn",True,(255,255,255))
    screen.blit(msg3,[20,290])
def rollg():
    msg4=font2.render("Your Turn",True,(255,255,255))
    screen.blit(msg4,[20,400])


# game loop
running = True
turn = 'red'
while running:
    screen.fill((0, 255, 195))
    bck()
    players()
    if turn == 'red':
        rollr()
    else:
        rollg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                dice, diceroll = pickNumber()
                screen.blit(dice, (58, 48))
                print(diceroll)

                # Player 1 chance
                if pickNumber() and turn == 'red':
                    turn = 'blue'
                    if diceroll == 6 and rx == 100 and ry == 251:
                        rx = 203
                        ry = 455
                        turn = 'red'
                    elif rx in range(162,358) and diceroll!=6 and ry==447:
                        rx=rx+(49*diceroll)
                    elif rx in range(162,358) and diceroll==6 and ry ==447:
                        rx=rx+(49*diceroll)
                        turn='red'
                    elif rx==358 and diceroll!=6 and ry==447:
                        rx = rx + (49 * diceroll)
                    elif rx==358 and diceroll==6 and ry==447:
                        rx = rx + (49 * 5)
                        ry=ry-49
                        turn='red'
                    elif rx==407 and diceroll<=4 and ry==447:  #7
                        rx=rx+(49*diceroll)
                    elif rx ==4077 and diceroll>4 and diceroll!=6 and ry==447:
                        rx=rx+(49*4)
                        ry=ry-49
                    elif rx==407 and diceroll==6 and ry==447:
                        rx=rx+(49*4)-(49*(diceroll-5))
                        ry=ry-49
                        turn='red'
                    elif rx==456 and diceroll<=3 and ry==447:  #8
                        rx=rx+(49*diceroll)
                    elif rx==456 and diceroll>3 and diceroll!=6 and ry ==447:
                        rx = rx + (49 * 3) - (49 * (diceroll - 4))
                        ry = ry - 49
                    elif rx==456  and diceroll==6 and ry ==447:
                        rx = rx + (49 * 3) - (49 * (diceroll - 4))
                        ry = ry - 49
                        turn='red'
                    elif rx==505 and diceroll<=2 and ry==447:#9
                        rx=rx+(49*diceroll)
                    elif rx==505 and diceroll>2 and diceroll!=6 and ry==447 :
                        rx =rx+(49*2)-(49*(diceroll-3))
                        ry =ry-49
                    elif rx ==505 and diceroll==6 and ry==447:
                        rx=rx+(49*2)-(49*(diceroll-3))
                        ry=ry-49
                        turn='red'
                    elif rx==554 and diceroll==1 and ry==447: #10
                        rx=rx+(49*diceroll)
                    elif rx==554 and diceroll==1 and diceroll!=6 and ry==447:
                        rx=rx+(49*1)-(49*(diceroll-2))
                        ry=ry-49

                    


























                # Player 2 chance
                elif pickNumber() and turn == 'blue':
                    if diceroll == 6 and b1x == 100 and b1y == 362:
                        b1x = 203
                        b1y = 455
                    turn = 'red'

    rplayer(rx, ry)
    bplayer(b1x, b1y)

    pygame.display.update()
    time.sleep(2.5)

pygame.quit()
quit()
#