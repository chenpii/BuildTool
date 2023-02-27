#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
按钮在主窗口中的布局，通常使用 grid() 函数来完成，该函数以网格状的形式（即行和列）来管理窗口的布局。
grid() 布局管理器提供了一个sticky参数，通过该参数可以设置按钮的方位，
该参数默认将控件设置居中，其他参数值有 N/S/W/E（上/下/左/右），而且可以组合在一起使用，比如 NW/WE/SE/SW/NE 等，
这与anchor参数控制文本的显示位置，有着异曲同工之妙


值得大家注意的是 grid() 布局方法不能与 pack() 混合在一起使用
'''
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
# 设置窗口大小并居中
width = 300
height = 200
screenwigth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwigth - width) / 2, (screenheight - height) / 2)
window.geometry(size_geo)
window.resizable(False, False)

# 将两个标签分别布置在第一行、第二行
tk.Label(window, text='账号：').grid(row=0)
tk.Label(window, text='密码：').grid(row=1)
# 创建输入框控件
entry1 = tk.Entry(window)
entry2 = tk.Entry(window, show='*')
# padx x间隔  pady y间隔
entry1.grid(row=0, column=1, padx=10, pady=5)
entry2.grid(row=1, column=1, padx=10, pady=5)


def login():
    messagebox.showinfo('welcome')



tk.Button(window, text='登录', width=10, command=login).grid(row=3, column=0, sticky='e', padx=20, pady=15)
tk.Button(window, text='退出', width=10, command=window.quit).grid(row=3, column=1, sticky='w', padx=20, pady=15)
window.mainloop()
