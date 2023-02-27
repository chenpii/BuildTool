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


def click_button():
    messagebox.showinfo(title='温馨提示', message='欢迎使用')


button = tk.Button(window, text='点击前往', bg='#7CCD7C', width=20, height=5, command=click_button).pack()

window.mainloop()
