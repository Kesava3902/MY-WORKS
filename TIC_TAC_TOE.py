import pygame,sys
import numpy as np
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('It is a draw', True,(0,0,0))
text1 = font.render('O wins the game', True,(0,0,0))
text2= font.render('X wins the game', True,(0,0,0))
textRect = text.get_rect()
screen_color=(100,0,255)
screen_color1=(100,0,255)
circle_color=(255,255,255)
cross_color=(5,5,5)
ROW=3
COL=3
screen=pygame.display.set_mode((600,600))
screen.fill(screen_color)
pygame.display.set_caption(" TIC_TAC_TOE ")
player=1
for i in range(200,401,200):
    pygame.draw.line(screen,(69,69,69),(i,0),(i,600),10)
    pygame.draw.line(screen,(69,69,69),(0,i),(600,i),10)
    
Board=np.zeros((ROW,COL))
game_over=False

def Mark_board(player,r,c):
    if player == 1:
        Board[r][c]=1
    if player == 2:
        Board[r][c]=2
def Owins():
    screen.fill(screen_color1)
    screen.blit(text1, textRect)
def Xwins():
    screen.fill(screen_color1)
    screen.blit(text2, textRect)
     

def Avaliable_in_Board(r,c):
            if Board[r][c] != 0:
                return False
            else:
                return True
def check_winner():
    for i in range(ROW):
        if Board[i][0]==1 and Board[i][1]==1 and Board[i][2]==1:
            pygame.draw.line(screen,circle_color,(0,i*200+100),(600,i*200+100),10)
            pygame.display.update()
            return True
        if Board[i][0]==2 and Board[i][1]==2 and Board[i][2]==2:
            pygame.draw.line(screen,cross_color,(0,i*200+100),(600,i*200+100),10)
            pygame.display.update()
            return True
    for j in range(COL):
        if Board[0][j]==1 and Board[1][j]==1 and Board[2][j]==1:
            pygame.draw.line(screen,circle_color,(j*200+100,0),(j*200+100,600),10)
            pygame.display.update()
            return True
        if Board[0][j]==2 and Board[1][j]==2 and Board[2][j]==2:
            pygame.draw.line(screen,cross_color,(j*200+100,0),(j*200+100,600),10)
            pygame.display.update()
            return True
    if Board[0][0]==1 and Board[1][1]==1 and Board[2][2]==1:
            pygame.draw.line(screen,circle_color,(0,0),(600,600),10)
            pygame.display.update()
            return True 
    if Board[0][0]==2 and Board[1][1]==2 and Board[2][2]==2:
            pygame.draw.line(screen,cross_color,(0,0),(600,600),10)
            pygame.display.update()
            return True
    if Board[0][2]==1 and Board[1][1]==1 and Board[2][0]==1:
            pygame.draw.line(screen,circle_color,(600,0),(0,600),10)
            pygame.display.update()
            return True 
    if Board[0][2]==2 and Board[1][1]==2 and Board[2][0]==2:
            pygame.draw.line(screen,cross_color,(600,0),(0,600),10)
            pygame.display.update()
            return True
    pygame.display.update()
    return False
    
def draw_circle(r,c):
    pygame.draw.circle(screen,circle_color,(c*200+200/2,r*200+200/2),80,10)
def draw_cross():
    pygame.draw.line(screen,cross_color,(c*200+20,r*200+20),(c*200+180,r*200+180),15)
    pygame.draw.line(screen,cross_color,(c*200+20,r*200+180),(c*200+180,r*200+20),15)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP and not game_over:
            pos=pygame.mouse.get_pos()
            c=pos[0]//200
            r=pos[1]//200
            if Avaliable_in_Board(r,c):
                if player == 1:
                    Mark_board(1,r,c)
                    draw_circle(r,c)
                    pygame.display.update()
                    if check_winner():
                        game_over=True
                    player = 2
                elif player == 2:
                    Mark_board(2,r,c)
                    draw_cross()
                    pygame.display.update()
                    draw_cross()
                    if check_winner():
                        game_over=True
                    player = 1   
        if 0 not in Board and not game_over:
             pygame.display.update()
             screen.fill(screen_color1)
             screen.blit(text, textRect)                       
        if game_over:
            if player==1:
                 pygame.display.update()
                 Xwins()
            if player==2:
                 pygame.display.update()
                 Owins()         
    pygame.display.update()
    pygame.time.delay(30)

