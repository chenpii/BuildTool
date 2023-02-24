#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk

window = tk.Tk()
window.title("测试小工具")
# 窗口大小
window.geometry('500x400')

var = tk.StringVar()
# 标签对象
lable1 = tk.Label(window, textvariable=var, bg='green', font=('Arial,12'), width=15, height=2)
lable1.pack()

on_hit = False


# 按钮触发函数
def hit_me():
    global on_hit
    if (on_hit == False):
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set(' ')


# 按钮对象
button1 = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
button1.pack()

window.mainloop()
