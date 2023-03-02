'''
3) StringVar() 添加列表选项
'''

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('400x180')
# 创建变量，用var1用来接收鼠标点击的具体选项内容
var1 = tk.StringVar()
l = tk.Label(window, bg='#B0B0B0', font=('微软雅黑', 15), width=20, textvariable=var1)
l.pack()


def click_button():
    # 使用curselection 来选中文本
    try:
        val = listbox.get(listbox.curselection())
        var1.set(val)
    except Exception as e:
        e = '错误'
        messagebox.showwarning(e, '没有选择任何条目')


# 创建一个按钮并放置，点击按钮调用print_selection函数
b1 = tk.Button(window, text='获取当前选项', command=click_button)
b1.pack()
# 创建Listbox并为其添加内容
var2 = tk.StringVar()
var2.set(("C", "Java", "Python", "C#", "Golang", "Runby"))
listbox = tk.Listbox(window, listvariable=var2)
listbox.pack()

window.mainloop()
