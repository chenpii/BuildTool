#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Label（标签）控件，是 Tkinter 中最常使用的一种控件，
主要用来显示窗口中的文本或者图像，
并且不同的 Lable（标签）允许设置各自不同的背景图片。
'''
from tkinter import *

# 创建主窗口
win = Tk()
win.config(bg='#8DB6CD')
win.title("C语言中文网")
win.geometry('400x300')
txt = "C语言中文网，网址是：c.biancheng.net"
msg = Message(win, text=txt, width=60, font=('微软雅黑', 10, 'bold'))
msg.pack(side=LEFT)
# 开始程序循环
win.mainloop()
