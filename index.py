#导入模块
from Plugin.test import Load
import pygame
from pygame.locals import *
import os
import sys
import json
import datetime
import threading

#加载插件
from Plugin import *

#初始化pygame
pygame.init()

datetimes = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
#加载图片
def load_img(file):
    return pygame.image.load(file)

EnableUpdate = True
#更新时间
def Update_Time():
    global datetimes
    while True:
        datetimes = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

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
    global EnableUpdate
    for i in pygame.event.get():
        if i.type == QUIT or i.type == KEYDOWN and i.key == K_ESCAPE:
            EnableUpdate = False
            #up_time.join()
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

#加载插件
def load_plugin():
    Load()

#加载主函数
def load_Program():
    global canvas,up_time
    loginfo('Loading...')
    up_time = threading.Thread(target=Update_Time)
    up_time.start()
    
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
    loginfo('Loading plugin')
    load_plugin()
    KeepWindow()
load_Program()