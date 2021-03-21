import pygame
import numpy as np
from PIL import Image
import cv2
import socket, pickle

def init_screen(win):
    win.fill((255,255,255))
   
    button(win, 'CLEAR', 90, 650, (0,0,255))
    button(win, 'SEND', 290, 650, (0,0,255))

    pygame.draw.line(win,(255,0,0),(0,590),(700,590),5)  

def button(win, text1, x, y, color):
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render(text1, True, (0,255,0), color) 
    textRect = text.get_rect()  
    textRect.center = (x,y)
    win.blit(text, textRect)

def button_click(win,x,y,text):
    button(win, text, x, y, (255,0,0))   

def drawP(win,brush):
    x,y = pygame.mouse.get_pos()
    #print(x,y)
    if(y>=0 and y<=540):
        win.blit(brush,(x-50,y-50))
    elif(x>=30 and x<=150 and y>=630 and y<=670):
        button_click(win,90,650,'CLEAR')
        button(win, 'screen cleared', 450, 650, (0,0,255))
        init_screen(win)
    elif(x>=230 and x<=350 and y>=630 and y<=670):
        button_click(win,290,650,'SEND') 
        img = take_ss(win)
        
        im = Image.open('pic_input.png')
        im = im.convert('1')
        na = np.array(im)
        arr = na.tolist()
        client_shit(arr)

def client_shit(arr):
    HOST = '192.168.1.30'
    PORT = 6969
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # arr = [[True, True, True, True, True, True, True, True, True, True], [True, True, True, False, False, True, True, True, True, True], [True, True, True, False, False, False, False, False, True, True], [True, True, True, True, True, True, False, True, True, True], [True, True, True, True, True, True, False, True, True, True], [True, True, True, True, True, True, False, True, True, True], [True, True, True, True, True, True, False, True, True, True], [True, True, True, True, True, False, False, True, True, True], [True, True, True, True, True, False, True, True, True, True], [True, True, True, True, True, False, True, True, True, True]]

    data_string = pickle.dumps(arr)
    s.send(data_string)
    s.close()

def take_ss(win):
    save_file = "pic_input.png" #save image in same folder
    rect = pygame.Rect(0, 0, 700, 540)
    sub = win.subsurface(rect)
    pygame.image.save(sub, save_file)
    pic = pygame.image.load(save_file)
    pic = pygame.transform.scale(pic, (10, 10))
    pygame.image.save(pic, save_file)
    return save_file


def main():
    pygame.init()
    pygame.init()
    win = pygame.display.set_mode((700,700))
    pygame.display.set_caption('Draw')
    d = False
    brush = pygame.image.load("brush.png")
    brush = pygame.transform.scale(brush,(90,90))

    init_screen(win)
    pygame.display.update()

    run = True
    while(run):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.MOUSEBUTTONUP:
                d = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                d = True
            if(d):
                drawP(win,brush)
                pygame.display.update()
    
    pygame.quit()
main()