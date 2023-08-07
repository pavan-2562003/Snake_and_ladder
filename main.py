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



score_font1=pygame.font.SysFont("comicsansms",35)


#font size
font1=pygame.font.SysFont("comicsansms",25)
font2=pygame.font.SysFont("comicsansms",20)

clock1= pygame.time.Clock()
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
                    if diceroll == 6 and rx <162 and ry == 251:
                        rx = rx+62
                        ry = 455
                        turn = 'red'
                    elif rx>=162 and rx<358  and diceroll!=6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx=rx+(49*diceroll)
                        if rx==309 and ry==447:
                            rx=358
                            ry=349
                        elif rx==456 and ry==349:
                            rx=358
                            ry=447
                        elif rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        elif rx==260 and ry==251:
                            rx=260
                            ry=398
                        elif rx==603 and ry==251:
                            rx=554
                            ry=153
                        elif rx==407 and ry==153:
                            rx=358
                            ry=251
                        elif rx==554 and ry==55:
                            rx=505
                            ry=202




                    elif rx >=162 and rx<358 and diceroll==6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx=rx+(49*diceroll)
                        if rx == 309 and ry == 447:
                            rx = 358
                            ry = 349
                        elif rx == 456 and ry == 349:
                            rx = 358
                            ry = 447
                        elif rx == 211 and ry == 251:
                            rx = 260
                            ry = 153
                        elif rx == 211 and ry == 153:
                            rx = 162
                            ry = 55
                        elif rx == 260 and ry == 251:
                            rx = 260
                            ry = 398
                        elif rx == 603 and ry == 251:
                            rx = 554
                            ry = 153
                        elif rx == 407 and ry == 153:
                            rx = 358
                            ry = 251
                        elif rx == 554 and ry == 55:
                            rx = 505
                            ry = 202
                        turn='red'

                    elif rx>=358 and rx <407 and diceroll!=6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx = rx + (49 * diceroll)
                        if rx==456 and ry==349:
                            rx=358
                            ry=447
                        elif rx==603 and ry==251:
                            rx=554
                            ry=153
                        elif rx==407 and ry ==153:
                            rx=358
                            ry=251
                        elif rx==554 and ry==55 and diceroll==4:
                            rx=505
                            ry=202
                    elif rx>=358 and rx<407 and diceroll==6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx = rx + (49 * 5)-(49*(diceroll-6))
                        ry=ry-49
                        turn='red'
                    elif rx>=407 and rx<456 and diceroll<=4 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):  #7
                        rx=rx+(49*diceroll)
                        if rx==456 and ry==349:
                            rx=358
                            ry=447
                        elif rx==603 and ry==251:
                            rx=554
                            ry=153
                        elif rx==554 and ry==55 and diceroll==3:
                            rx =505
                            ry =202



                    elif rx >=407 and rx<456 and diceroll>4 and diceroll!=6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx=rx+(49*4)-(49*(diceroll-5))
                        ry=ry-49
                    elif rx>=407 and rx<456 and diceroll==6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx=rx+(49*4)-(49*(diceroll-5))
                        ry=ry-49
                        turn='red'
                    elif rx>=456 and rx<505 and diceroll<=3 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):  #8
                        rx=rx+(49*diceroll)
                        if rx==603 and ry==251:
                            rx=554
                            ry=153
                        elif rx==554 and ry==55 and diceroll==2:
                            rx=505
                            ry=202


                    #change the values from here
                    elif rx>=456 and rx<505 and diceroll>3 and diceroll!=6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx = rx + (49 * 3) - (49 * (diceroll - 4))
                        ry = ry - 49

                        if rx==505 and ry==398:
                            rx=407
                            ry=251
                        elif rx==505 and ry==300:
                            rx=554
                            ry=251



                    elif rx>=456 and rx<505  and diceroll==6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx = rx + (49 * 3) - (49 * (diceroll - 4))
                        ry = ry - 49
                        if rx==505 and ry==398:
                            rx=407
                            ry=251
                        elif rx==505 and ry==300:
                            rx=554
                            ry=251
                        turn='red'
                    elif rx>=505 and rx<554 and diceroll<=2 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):#9
                        rx=rx+(49*diceroll)
                        if rx==603 and ry==251:
                            rx=554
                            ry=153
                        elif rx==554 and ry ==55 and diceroll==1:
                            rx=505
                            ry=202

                    elif rx>=505 and rx<554 and diceroll>2 and diceroll!=6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx =rx+(49*2)-(49*(diceroll-3))
                        ry =ry-49
                        if rx==505 and ry==398:
                            rx=407
                            ry=251
                        elif rx==505 and ry==300:
                            rx=554
                            ry=251
                        elif rx==456 and ry==202:
                            rx=603
                            ry=300
                        elif rx==456 and ry==104:
                            rx=554
                            ry=6
                    elif rx >=505 and rx<554 and diceroll==6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx=rx+(49*2)-(49*(diceroll-3))
                        ry=ry-49
                        if rx==505 and ry==398:
                            rx=407
                            ry=251
                        elif rx==505 and ry==300:
                            rx=554
                            ry=251
                        elif rx==456 and ry==202:
                            rx=603
                            ry=300
                        elif rx==456 and ry==104:
                            rx=554
                            ry=6
                        turn='red'


                    elif rx>=554 and rx<603 and diceroll==1 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55): #10
                        rx=rx+(49*diceroll)

                        if rx==603 and ry==251:
                            rx=554
                            ry=153

                    elif rx>=554 and rx<603 and diceroll>1 and diceroll!=6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx=rx+(49*1)-(49*(diceroll-2))
                        ry=ry-49
                        if rx==505 and ry==398:
                            rx=407
                            ry=251
                        elif rx==505 and ry==300:
                            rx=554
                            ry=251
                        elif rx==456 and ry==202:
                            rx=603
                            ry=300
                        elif rx==456 and ry==104:
                            rx=554
                            ry=6



                    elif rx >=554 and rx<603 and diceroll==6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx=rx+(49*1)-(49*(diceroll-2))
                        ry=ry-49
                        if rx==505 and ry==398:
                            rx=407
                            ry=251
                        elif rx==505 and ry==300:
                            rx=554
                            ry=251
                        elif rx==456 and ry==202:
                            rx=603
                            ry=300
                        elif rx==456 and ry==104:
                            rx=554
                            ry=6
                        turn='red'
                    elif rx>=603 and diceroll!=6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx=rx-(49*(diceroll-1))
                        ry=ry-49

                        if rx==505 and ry==398:
                            rx=407
                            ry=251
                        elif rx==505 and ry==300:
                            rx=554
                            ry=251
                        elif rx==456 and ry==202:
                            rx=603
                            ry=300
                        elif rx==456 and ry==104:
                            rx=554
                            ry=6
                        elif rx == 358 and ry == 104:
                            rx = 260
                            ry = 202
                    elif rx >=603 and diceroll==6 and (ry==455 or ry==349 or ry==251 or ry==153 or ry==55):
                        rx=rx-(49*(diceroll-1))
                        ry = ry-49

                        if rx==505 and ry==398:
                            rx=407
                            ry=251
                        elif rx==505 and ry==300:
                            rx=554
                            ry=251
                        elif rx==456 and ry==202:
                            rx=603
                            ry=300
                        elif rx==456 and ry==104:
                            rx=554
                            ry=6
                        elif rx == 358 and ry == 104:
                            rx = 260
                            ry = 202
                        turn='red'



            #row 2
                    elif rx>358 and rx<=603 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll!=6:
                        rx=rx-(49*diceroll)

                        if rx==505 and ry==398:
                            rx=407
                            ry=251
                        elif rx==505 and ry==300:
                            rx=554
                            ry=251
                        elif rx==456 and ry==202:
                            rx=603
                            ry=300
                        elif rx==456 and ry==104:
                            rx=554
                            ry=6
                        elif rx == 162 and ry == 300:
                            rx = 260
                            ry = 447
                        elif rx == 358 and ry == 104:
                            rx = 260
                            ry = 202

                    elif rx>358 and rx<=603 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 )  and diceroll==6:
                        rx=rx-(49*5)
                        ry=ry-49

                    elif rx>407 and rx<=603 and diceroll!=6 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ):
                        rx=rx-(49*diceroll)
                        if rx==211 and ry==6:
                            rx=162
                            ry=251
                        elif rx==162 and ry==300:
                            rx=260
                            ry=447
                        elif rx==211 and ry==6:
                            rx=162
                            ry=251


                    elif rx>407 and rx<=603 and diceroll==6 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ):
                        rx=rx-(49*diceroll)

                        if rx==211 and ry==6:
                            rx=162
                            ry=251
                        elif rx==162 and ry==300:
                            rx=260
                            ry=447
                        elif rx==211 and ry==6:
                            rx=162
                            ry=251
                        turn = 'red'

                    elif rx==407 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll!=6:
                        rx=rx-(49*diceroll)
                        if rx==358 and ry==104:
                            rx=260
                            ry=202
                        elif rx==211 and ry==6:
                            rx=162
                            ry=251

                    elif rx==407 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll==6:
                        rx=rx-(49*5)
                        ry=ry-49
                        if rx==162 and ry==300:
                            rx=260
                            ry=447
                        turn='red'

                    elif rx==358 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll<5:
                        rx=rx-(49*diceroll)
                        if rx==162 and ry==300:
                            rx=260
                            ry=447

                    elif rx==358 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll==5:
                        rx=rx-(49*4)+(49*(diceroll-5))
                        ry=ry-49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55

                    elif rx==358 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll==6:
                        rx=rx-(49*4)+(49*(diceroll-5))
                        ry=ry-49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        turn='red'

                    elif rx==309 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll<4:
                        rx=rx-(49*diceroll)
                        if rx==162 and ry==300:
                            rx=260
                            ry=447


                    elif rx==309 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll>=4 and diceroll!=6:
                        rx=rx-(49*3)+(49*(diceroll-4))
                        ry=ry-49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        elif rx==260 and ry==251:
                            rx=260
                            ry=398

                    elif rx==309 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll==6:
                        rx=rx-(49*3)+(49*(diceroll-4))
                        ry=ry-49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        elif rx==260 and ry==251:
                            rx=260
                            ry=398
                        turn='red'

                    elif rx==260 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll<3:
                        rx=rx-(49*diceroll)
                        if rx==162 and ry==300:
                            rx=260
                            ry=447

                    elif rx==260 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll>=3 and diceroll!=6:
                        rx=rx-(49*2)+(49*(diceroll-3))
                        ry=ry-49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        elif rx==260 and ry==251:
                            rx=260
                            ry=398

                    elif rx==260 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll==6:
                        rx=rx-(49*2)+(49*(diceroll-3))
                        ry=ry-49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        elif rx==260 and ry==251:
                            rx=260
                            ry=398
                        turn='red'

                    elif rx==211 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll<2:
                        rx=rx-(49*diceroll)
                        if rx==162 and ry==300:
                            rx=260
                            ry=447

                    elif rx ==211 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll!=6 and diceroll>=2:
                        rx=rx-49+(49*(diceroll-2))
                        ry=ry-49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        elif rx==260 and ry==251:
                            rx=260
                            ry=398

                    elif rx==211 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll==6:
                        rx = rx - 49 + (49 * (diceroll - 2))
                        ry = ry - 49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        elif rx==260 and ry==251:
                            rx=260
                            ry=398
                        turn='red'

                    elif rx==162 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll!=6:
                        rx=rx+(49*(diceroll-1))
                        ry=ry-49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        elif rx==260 and ry==251:
                            rx=260
                            ry=398
                        elif rx == 407 and ry == 153:
                            rx = 358
                            ry = 251
                    elif rx == 162 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6 ) and diceroll == 6:
                        rx = rx + (49 * (diceroll - 1))
                        ry = ry - 49
                        if rx==211 and ry==251:
                            rx=260
                            ry=153
                        elif rx==211 and ry==153:
                            rx=162
                            ry=55
                        elif rx==260 and ry==251:
                            rx=260
                            ry=398
                        elif rx == 407 and ry == 153:
                            rx = 358
                            ry = 251
                        turn='red'

                    #final row
                    elif ry==6 and(rx==554 or rx ==603) and diceroll!=6:
                        rx=rx-(49*diceroll)
                    elif ry==6 and(rx==554 or rx ==603) and diceroll==6:
                        rx=rx-(49*diceroll)
                        turn='red'
                    elif ry==6 and  rx==456 and diceroll<5:
                        rx=rx-(49*diceroll)
                    elif ry==6 and  rx==456 and diceroll==5:
                        rx=rx-(49*diceroll)
                        if rx==211 and ry==6 and diceroll==5 :
                            rx=162
                            ry=251
                    elif ry == 6 and rx == 456 and diceroll == 6:
                        rx=rx
                    elif ry == 6 and rx == 505 and diceroll != 6:
                        rx=rx-(49*diceroll)
                    elif ry == 6 and rx == 505 and diceroll == 6:
                        rx=rx-(49*diceroll)
                        if rx==211 and ry==6 and diceroll==6 :
                            rx=162
                            ry=251
                    elif ry==6 and rx==407 and diceroll<6:
                        rx = rx - (49 * diceroll)
                        if rx==211 and ry==6 and diceroll==4 :
                            rx=162
                            ry=251
                    elif ry==6 and  rx==407 and rx>=162 and  diceroll==6 :
                        rx=rx
                    elif ry == 6 and rx == 358 and rx >= 162 and diceroll >= 5:
                        rx = rx
                    elif ry == 6 and rx == 358 and rx >= 162 and diceroll < 5:
                        rx = rx - (49 * diceroll)
                        if rx==211 and ry==6 and diceroll==3 :
                            rx=162
                            ry=251
                    elif ry == 6 and rx == 309 and rx >= 162 and diceroll >=4:
                        rx=rx
                    elif ry == 6 and rx == 309 and rx >= 162 and diceroll <4:
                        rx = rx - (49 * diceroll)
                        if rx==211 and ry==6 and diceroll==2 :
                            rx=162
                            ry=251
                    elif ry == 6 and rx == 260 and rx >= 162 and diceroll >= 3:
                        rx = rx
                    elif ry == 6 and rx == 260 and rx >= 162 and diceroll < 3:
                        rx = rx - (49 * diceroll)
                        if rx == 211 and ry == 6 and diceroll == 1:
                            rx = 162
                            ry = 251
                    elif ry == 6 and rx == 211 and rx >= 162 and diceroll >= 2:
                        rx = rx




                # Player 2 chance
                elif pickNumber() and turn == 'blue':
                    turn='red'
                    if diceroll == 6 and b1x < 162 and b1y == 251:
                        b1x = b1x + 62
                        b1y = 455
                        turn = 'blue'
                    elif b1x >= 162 and b1x < 358 and diceroll != 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * diceroll)
                        if b1x == 309 and b1y == 447:
                            b1x = 358
                            b1y = 349
                        elif b1x == 456 and b1y == 349:
                            b1x = 358
                            b1y = 447
                        elif b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398
                        elif b1x == 603 and b1y == 251:
                            b1x = 554
                            b1y = 153
                        elif b1x == 407 and b1y == 153:
                            b1x = 358
                            b1y = 251
                        elif b1x == 554 and b1y == 55:
                            b1x = 505
                            b1y = 202




                    elif b1x >= 162 and b1x < 358 and diceroll == 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * diceroll)
                        if b1x == 309 and b1y == 447:
                            b1x = 358
                            b1y = 349
                        elif b1x == 456 and b1y == 349:
                            b1x = 358
                            b1y = 447
                        elif b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398
                        elif b1x == 603 and b1y == 251:
                            b1x = 554
                            b1y = 153
                        elif b1x == 407 and b1y == 153:
                            b1x = 358
                            b1y = 251
                        elif b1x == 554 and b1y == 55:
                            b1x = 505
                            b1y = 202
                        turn = 'blue'

                    elif b1x >= 358 and b1x < 407 and diceroll != 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * diceroll)
                        if b1x == 456 and b1y == 349:
                            b1x = 358
                            b1y = 447
                        elif b1x == 603 and b1y == 251:
                            b1x = 554
                            b1y = 153
                        elif b1x == 407 and b1y == 153:
                            b1x = 358
                            b1y = 251
                        elif b1x == 554 and b1y == 55 and diceroll == 4:
                            b1x = 505
                            b1y = 202
                    elif b1x >= 358 and b1x < 407 and diceroll == 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * 5) - (49 * (diceroll - 6))
                        b1y = b1y - 49
                        turn = 'blue'
                    elif b1x >= 407 and b1x < 456 and diceroll <= 4 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):  # 7
                        b1x = b1x + (49 * diceroll)
                        if b1x == 456 and b1y == 349:
                            b1x = 358
                            b1y = 447
                        elif b1x == 603 and b1y == 251:
                            b1x = 554
                            b1y = 153
                        elif b1x == 554 and b1y == 55 and diceroll == 3:
                            b1x = 505
                            b1y = 202



                    elif b1x >= 407 and b1x < 456 and diceroll > 4 and diceroll != 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * 4) - (49 * (diceroll - 5))
                        b1y = b1y - 49
                    elif b1x >= 407 and b1x < 456 and diceroll == 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * 4) - (49 * (diceroll - 5))
                        b1y = b1y - 49
                        turn = 'blue'
                    elif b1x >= 456 and b1x < 505 and diceroll <= 3 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):  # 8
                        b1x = b1x + (49 * diceroll)
                        if b1x == 603 and b1y == 251:
                            b1x = 554
                            b1y = 153
                        elif b1x == 554 and b1y == 55 and diceroll == 2:
                            b1x = 505
                            b1y = 202


                    # change the values from here
                    elif b1x >= 456 and b1x < 505 and diceroll > 3 and diceroll != 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * 3) - (49 * (diceroll - 4))
                        b1y = b1y - 49

                        if b1x == 505 and b1y == 398:
                            b1x = 407
                            b1y = 251
                        elif b1x == 505 and b1y == 300:
                            b1x = 554
                            b1y = 251



                    elif b1x >= 456 and b1x < 505 and diceroll == 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * 3) - (49 * (diceroll - 4))
                        b1y = b1y - 49
                        if b1x == 505 and b1y == 398:
                            b1x = 407
                            b1y = 251
                        elif b1x == 505 and b1y == 300:
                            b1x = 554
                            b1y = 251
                        turn = 'blue'
                    elif b1x >= 505 and b1x < 554 and diceroll <= 2 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):  # 9
                        b1x = b1x + (49 * diceroll)
                        if b1x == 603 and b1y == 251:
                            b1x = 554
                            b1y = 153
                        elif b1x == 554 and b1y == 55 and diceroll == 1:
                            b1x = 505
                            b1y = 202

                    elif b1x >= 505 and b1x < 554 and diceroll > 2 and diceroll != 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * 2) - (49 * (diceroll - 3))
                        b1y = b1y - 49
                        if b1x == 505 and b1y == 398:
                            b1x = 407
                            b1y = 251
                        elif b1x == 505 and b1y == 300:
                            b1x = 554
                            b1y = 251
                        elif b1x == 456 and b1y == 202:
                            b1x = 603
                            b1y = 300
                        elif b1x == 456 and b1y == 104:
                            b1x = 554
                            b1y = 6
                    elif b1x >= 505 and b1x < 554 and diceroll == 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * 2) - (49 * (diceroll - 3))
                        b1y = b1y - 49
                        if b1x == 505 and b1y == 398:
                            b1x = 407
                            b1y = 251
                        elif b1x == 505 and b1y == 300:
                            b1x = 554
                            b1y = 251
                        elif b1x == 456 and b1y == 202:
                            b1x = 603
                            b1y = 300
                        elif b1x == 456 and b1y == 104:
                            b1x = 554
                            b1y = 6
                        turn = 'blue'


                    elif b1x >= 554 and b1x < 603 and diceroll == 1 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):  # 10
                        b1x = b1x + (49 * diceroll)

                        if b1x == 603 and b1y == 251:
                            b1x = 554
                            b1y = 153

                    elif b1x >= 554 and b1x < 603 and diceroll > 1 and diceroll != 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * 1) - (49 * (diceroll - 2))
                        b1y = b1y - 49
                        if b1x == 505 and b1y == 398:
                            b1x = 407
                            b1y = 251
                        elif b1x == 505 and b1y == 300:
                            b1x = 554
                            b1y = 251
                        elif b1x == 456 and b1y == 202:
                            b1x = 603
                            b1y = 300
                        elif b1x == 456 and b1y == 104:
                            b1x = 554
                            b1y = 6



                    elif b1x >= 554 and b1x < 603 and diceroll == 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x + (49 * 1) - (49 * (diceroll - 2))
                        b1y = b1y - 49
                        if b1x == 505 and b1y == 398:
                            b1x = 407
                            b1y = 251
                        elif b1x == 505 and b1y == 300:
                            b1x = 554
                            b1y = 251
                        elif b1x == 456 and b1y == 202:
                            b1x = 603
                            b1y = 300
                        elif b1x == 456 and b1y == 104:
                            b1x = 554
                            b1y = 6
                        turn = 'blue'
                    elif b1x >= 603 and diceroll != 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x - (49 * (diceroll - 1))
                        b1y = b1y - 49

                        if b1x == 505 and b1y == 398:
                            b1x = 407
                            b1y = 251
                        elif b1x == 505 and b1y == 300:
                            b1x = 554
                            b1y = 251
                        elif b1x == 456 and b1y == 202:
                            b1x = 603
                            b1y = 300
                        elif b1x == 456 and b1y == 104:
                            b1x = 554
                            b1y = 6
                        elif b1x == 358 and b1y == 104:
                            b1x = 260
                            b1y = 202
                    elif b1x >= 603 and diceroll == 6 and (
                            b1y == 455 or b1y == 349 or b1y == 251 or b1y == 153 or b1y == 55):
                        b1x = b1x - (49 * (diceroll - 1))
                        b1y = b1y - 49

                        if b1x == 505 and b1y == 398:
                            b1x = 407
                            b1y = 251
                        elif b1x == 505 and b1y == 300:
                            b1x = 554
                            b1y = 251
                        elif b1x == 456 and b1y == 202:
                            b1x = 603
                            b1y = 300
                        elif b1x == 456 and b1y == 104:
                            b1x = 554
                            b1y = 6
                        elif b1x == 358 and b1y == 104:
                            b1x = 260
                            b1y = 202
                        turn = 'blue'



                    # row 2
                    elif b1x > 358 and b1x <= 603 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll != 6:
                        b1x = b1x - (49 * diceroll)

                        if b1x == 505 and b1y == 398:
                            b1x = 407
                            b1y = 251
                        elif b1x == 505 and b1y == 300:
                            b1x = 554
                            b1y = 251
                        elif b1x == 456 and b1y == 202:
                            b1x = 603
                            b1y = 300
                        elif b1x == 456 and b1y == 104:
                            b1x = 554
                            b1y = 6
                        elif b1x == 162 and b1y == 300:
                            b1x = 260
                            b1y = 447
                        elif b1x == 358 and b1y == 104:
                            b1x = 260
                            b1y = 202

                    elif b1x > 358 and b1x <= 603 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll == 6:
                        b1x = b1x - (49 * 5)
                        b1y = b1y - 49

                    elif b1x > 407 and b1x <= 603 and diceroll != 6 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6):
                        b1x = b1x - (49 * diceroll)
                        if b1x == 211 and b1y == 6:
                            b1x = 162
                            b1y = 251
                        elif b1x == 162 and b1y == 300:
                            b1x = 260
                            b1y = 447
                        elif b1x == 211 and b1y == 6:
                            b1x = 162
                            b1y = 251


                    elif b1x > 407 and b1x <= 603 and diceroll == 6 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6):
                        b1x = b1x - (49 * diceroll)

                        if b1x == 211 and b1y == 6:
                            b1x = 162
                            b1y = 251
                        elif b1x == 162 and b1y == 300:
                            b1x = 260
                            b1y = 447
                        elif b1x == 211 and b1y == 6:
                            b1x = 162
                            b1y = 251
                        turn = 'blue'

                    elif b1x == 407 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll != 6:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 358 and b1y == 104:
                            b1x = 260
                            b1y = 202
                        elif b1x == 211 and b1y == 6:
                            b1x = 162
                            b1y = 251

                    elif b1x == 407 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll == 6:
                        b1x = b1x - (49 * 5)
                        b1y = b1y - 49
                        if b1x == 162 and b1y == 300:
                            b1x = 260
                            b1y = 447
                        turn = 'blue'

                    elif b1x == 358 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll < 5:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 162 and b1y == 300:
                            b1x = 260
                            b1y = 447

                    elif b1x == 358 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll == 5:
                        b1x = b1x - (49 * 4) + (49 * (diceroll - 5))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55

                    elif b1x == 358 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll == 6:
                        b1x = b1x - (49 * 4) + (49 * (diceroll - 5))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        turn = 'blue'

                    elif b1x == 309 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll < 4:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 162 and b1y == 300:
                            b1x = 260
                            b1y = 447


                    elif b1x == 309 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll >= 4 and diceroll != 6:
                        b1x = b1x - (49 * 3) + (49 * (diceroll - 4))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398

                    elif b1x == 309 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll == 6:
                        b1x = b1x - (49 * 3) + (49 * (diceroll - 4))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398
                        turn = 'blue'

                    elif b1x == 260 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll < 3:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 162 and b1y == 300:
                            b1x = 260
                            b1y = 447

                    elif b1x == 260 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll >= 3 and diceroll != 6:
                        b1x = b1x - (49 * 2) + (49 * (diceroll - 3))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398

                    elif b1x == 260 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll == 6:
                        b1x = b1x - (49 * 2) + (49 * (diceroll - 3))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398
                        turn = 'blue'

                    elif b1x == 211 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll < 2:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 162 and b1y == 300:
                            b1x = 260
                            b1y = 447

                    elif b1x == 211 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll != 6 and diceroll >= 2:
                        b1x = b1x - 49 + (49 * (diceroll - 2))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398

                    elif b1x == 211 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll == 6:
                        b1x = b1x - 49 + (49 * (diceroll - 2))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398
                        turn = 'blue'

                    elif b1x == 162 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll != 6:
                        b1x = b1x + (49 * (diceroll - 1))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398
                        elif b1x == 407 and b1y == 153:
                            b1x = 358
                            b1y = 251
                    elif b1x == 162 and (
                            b1y == 398 or b1y == 300 or b1y == 202 or b1y == 104 or b1y == 6) and diceroll == 6:
                        b1x = b1x + (49 * (diceroll - 1))
                        b1y = b1y - 49
                        if b1x == 211 and b1y == 251:
                            b1x = 260
                            b1y = 153
                        elif b1x == 211 and b1y == 153:
                            b1x = 162
                            b1y = 55
                        elif b1x == 260 and b1y == 251:
                            b1x = 260
                            b1y = 398
                        elif b1x == 407 and b1y == 153:
                            b1x = 358
                            b1y = 251
                        turn = 'blue'

                    # final row
                    elif b1y == 6 and (b1x == 554 or b1x == 603) and diceroll != 6:
                        b1x = b1x - (49 * diceroll)
                    elif b1y == 6 and (b1x == 554 or b1x == 603) and diceroll == 6:
                        b1x = b1x - (49 * diceroll)
                        turn = 'blue'
                    elif b1y == 6 and b1x == 456 and diceroll < 5:
                        b1x = b1x - (49 * diceroll)
                    elif b1y == 6 and b1x == 456 and diceroll == 5:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 211 and b1y == 6 and diceroll == 5:
                            b1x = 162
                            b1y = 251
                    elif b1y == 6 and b1x == 456 and diceroll == 6:
                        b1x = b1x
                    elif b1y == 6 and b1x == 505 and diceroll != 6:
                        b1x = b1x - (49 * diceroll)
                    elif b1y == 6 and b1x == 505 and diceroll == 6:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 211 and b1y == 6 and diceroll == 6:
                            b1x = 162
                            b1y = 251
                    elif b1y == 6 and b1x == 407 and diceroll < 6:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 211 and b1y == 6 and diceroll == 4:
                            b1x = 162
                            b1y = 251
                    elif b1y == 6 and b1x == 407 and b1x >= 162 and diceroll == 6:
                        b1x = b1x
                    elif b1y == 6 and b1x == 358 and b1x >= 162 and diceroll >= 5:
                        b1x = b1x
                    elif b1y == 6 and b1x == 358 and b1x >= 162 and diceroll < 5:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 211 and b1y == 6 and diceroll == 3:
                            b1x = 162
                            b1y = 251
                    elif b1y == 6 and b1x == 309 and b1x >= 162 and diceroll >= 4:
                        b1x = b1x
                    elif b1y == 6 and b1x == 309 and b1x >= 162 and diceroll < 4:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 211 and b1y == 6 and diceroll == 2:
                            b1x = 162
                            b1y = 251
                    elif b1y == 6 and b1x == 260 and b1x >= 162 and diceroll >= 3:
                        b1x = b1x
                    elif b1y == 6 and b1x == 260 and b1x >= 162 and diceroll < 3:
                        b1x = b1x - (49 * diceroll)
                        if b1x == 211 and b1y == 6 and diceroll == 1:
                            b1x = 162
                            b1y = 251
                    elif b1y == 6 and b1x == 211 and b1x >= 162 and diceroll >= 2:
                        b1x = b1x

    rplayer(rx, ry)
    bplayer(b1x, b1y)

    pygame.display.update()

    #decision on who won at last
    if rx==162 and ry==6:
        screen.fill((50,153,213))
        value=score_font1.render("Blue won",True,(255,255,102))
        screen.blit(value,[250,200])
        running=False
    if b1x==162 and b1y==9:
        screen.fill((50,153,213))
        value=score_font1.render("Red won",True,(255,255,102))
        screen.blit(value,[250,200])
        running=False


    time.sleep(2.5)
pygame.display.update()
clock1.tick(40)
pygame.quit()
quit()
#