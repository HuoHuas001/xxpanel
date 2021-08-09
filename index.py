#导入模块
import pygame
from pygame.locals import *
import os
import sys
import json
import datetime

#加载插件
import Load

#初始化pygame
pygame.init()

datetimes = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
#加载图片
def load_img(file):
    return pygame.image.load(file)

icon = load_img('Images/panel_ico.ico')
Desktop_BG = load_img('Images/Desktop_BG.jpg')
Desktop_Bar = load_img('Images/bar.png')
#输出文本
def loginfo(msg):
    print('['+datetimes+' INFO] '+msg)
def logwarn(msg):
    print('['+datetimes+' WARN] '+msg)
def logerro(msg):
    print('['+datetimes+' ERRO] '+msg)

#Debug模式
Debug = False

#状态
state = 'DESKTOP'

#监听事件
def Listen_Event():
    for i in pygame.event.get():
        if i.type == QUIT or i.type == KEYDOWN and i.key == K_ESCAPE:
            pygame.quit()
            loginfo('Program exits normally')
            sys.exit()

#渲染桌面背景
def Paint_Desktop():
    #绘制桌面背景
    canvas.blit(Desktop_BG,(0,0))
    #绘制任务栏
    canvas.blit(Desktop_Bar,(0,0))

#保持窗口
def KeepWindow():
    while True:
        Listen_Event()
        pygame.display.update()
        if state == 'DESKTOP':
            Paint_Desktop()

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