#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
protocol协议处理机制

Tinter 除了提供事件绑定机制之外，还提供了协议处理机制，
它指的是应用程序和窗口管理器之间的交互，最常用的协议为 WM_DELETE_WINDOW

当 Tkinter 使用 WM_DELETE_WINDOW 协议与主窗口进行交互时，
Tkinter 主窗口右上角x号的关闭功能失效，也就是无法通过点击x来关闭窗口，而是转变成调用用户自定义的函数。
'''

from tkinter import Tk
# 导入 对话框控件
from tkinter import messagebox

window = Tk()


# 定义回调函数，当用户点击窗口x退出时，执行
def QueryWindow():
    if (messagebox.showwarning("警告", "出现了一个错误")):
        window.destroy()


window.protocol('WM_DELETE_WINDOW', QueryWindow)
window.mainloop()
