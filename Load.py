#from index import *
import pygame
imgs = []
fps = 0
#加载图片
def load_img(file):
    return pygame.image.load(file)
def Loadimg():
    global imgs,fps
    imgs = []
    fps = 0
    for i in range(1,76):
        img = load_img('Images/Load/'+str(i)+'.jpg')
        imgs.append(img)

def action(canvas,pos):
    global fps
    for i in imgs:
        if fps >= 75:
            canvas.blit(i,pos)
        else:
            fps = 0
