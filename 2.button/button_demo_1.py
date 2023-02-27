#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Button 控件是 Tkinter 中常用的窗口部件之一，同时也是实现程序与用户交互的主要控件。
通过用户点击按钮的行为来执行回调函数，是 Button 控件的主要功用。
首先自定义一个函数或者方法，然后将函数与按钮关联起来，
最后，当用户按下这个按钮时，Tkinter 就会自动调用相关函数
'''
import tkinter as tk

# 创建窗口
window = tk.Tk()


# 设置回调函数
def callback():
    print("click me!")


# 使用按钮控件调用函数
b = tk.Button(window, text="点击执行回调函数", command=callback).pack()
# 显示窗口
tk.mainloop()
