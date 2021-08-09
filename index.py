#导入模块
import pygame
from pygame.locals import *
import os
import sys
import json
import datetime

#初始化pygame
pygame.init()

datetimes = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
#加载图片
def load_img(file):
    return pygame.image.load(file)

icon = load_img('Images/panel_ico.ico')
#输出文本
def loginfo(msg):
    print('['+datetimes+' INFO] '+msg)
def logwarn(msg):
    print('['+datetimes+' WARN] '+msg)
def logerro(msg):
    print('['+datetimes+' ERRO] '+msg)

#Debug模式
Debug = False

#监听事件
def Listen_Event():
    for i in pygame.event.get():
        if i.type == QUIT or i.type == KEYDOWN and i.key == K_ESCAPE:
            pygame.quit()
            loginfo('Program exits normally')
            sys.exit()
#保持窗口
def KeepWindow():
    while True:
        Listen_Event()
        pygame.display.update()

#加载主函数
def load_Program():
    global canvas
    loginfo('Loading...')
    #调用加载图片
    try:
        loginfo('Build window..')
        canvas = pygame.display.set_mode((1500,900))
        pygame.display.set_caption('xxpanel')
        pygame.display.set_icon(icon)
        loginfo('Build:'+'xxpanel'+' successful')
    except:
        logerro('An error occurred generating the window!')
    loginfo('Load complete, start the program')
    KeepWindow()
load_Program()