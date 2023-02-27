#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk

# 创建窗口对象
window = tk.Tk()
# 设置窗口标题
window.title("测试小工具")
# 设置窗口大小
window.geometry('200x200')

var1 = tk.StringVar()
lable = tk.Label(window, textvariable=var1, bg='yellow', width=4)
lable.pack()


# 按钮触发函数
def print_selection():
    pass


# 按钮对象
button1 = tk.Button(window, name='选项',text='print selection', width=15, height=2, command=print_selection).pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44, 55, 66, 77, 88, 99, 100))
# ListBox
listbox = tk.Listbox(window, listvariable=var2, height=4)
yscrollbar = tk.Scrollbar(listbox,command=listbox.yview)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=yscrollbar.set)
listbox.pack()

window.mainloop()
