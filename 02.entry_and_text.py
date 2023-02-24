#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk

window = tk.Tk()
window.title("测试小工具")
# 窗口大小
window.geometry('200x200')

entry = tk.Entry(window, show=None)
entry.pack()


# 按钮触发函数
def insert():
    var = entry.get()
    text.insert('insert', var)



def end():
    var = entry.get()
    text.insert('end', var)



# 按钮对象
button1 = tk.Button(window, text='insert point', width=15, height=2, command=insert)
button1.pack()
button2 = tk.Button(window, text='insert end', width=15, height=2, command=end)
button2.pack()

text = tk.Text(window, height=2)
text.pack()

window.mainloop()
