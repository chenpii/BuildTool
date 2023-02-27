#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
当我们运行 Tkinter 程序时，主窗口都会出现在距离屏幕左上角指定的位置上，这是由 Tkinter 软件包默认设置的。
但是在许多情况下，我们需要根据实际情况来移动窗口在电脑屏幕上的位置，这时应该如何处理呢？
其实很简单，通过窗口对象的 geometry() 方法即可改变主窗口的位置
'''
from tkinter import Tk
window = Tk()
# window.geometry('450x400+300+200')
# 上述代码表示，设置主窗口宽度为450，高度为400，同时窗口距离屏幕左边300，距离屏幕顶部200
# 将带+的参数成为位置参数，如果设置成负数，主窗口会被移动至“屏幕之外”，此时就看不到主窗口了

# 设置窗口大小变量
width=300
height=200
# 窗口居中，获取屏幕尺寸以计算布局参数，使得窗口居中
screenwigth=window.winfo_screenwidth()
screenheight=window.winfo_screenheight()
size_geo='%dx%d+%d+%d'%(width,height,(screenwigth-width)/2,(screenheight-height)/2)

window.geometry(size_geo)


window.mainloop()