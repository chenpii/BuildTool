#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk

window = tk.Tk()
window.title("测试")
# 窗口大小
window.geometry('500x400')


lable1 = tk.Label(window, text='hello', bg='green', font=('Arial,12'), width=15, height=2).pack()


window.mainloop()
