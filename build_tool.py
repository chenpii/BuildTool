#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk

window = tk.Tk()
window.title("小工具")
# 窗口大小
window.geometry('500x400')

fire_rating = tk.StringVar()  # 防火等级（列表）
building_name = tk.StringVar()  # 建筑物名称（列表）
building_cate = tk.StringVar()  # 建筑物类别1（列表）
building_cate2 = tk.StringVar()  # 建筑物类别（列表）
building_volum = tk.StringVar()  # 建筑体积（entry）


# 按钮触发函数
def calculate():
    pass


# 按钮对象
button1 = tk.Button(window, text='计算', width=15, height=2, command=calculate)
button1.pack()

window.mainloop()
