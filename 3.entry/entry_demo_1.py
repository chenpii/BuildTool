'''
Entry 控件是 Tkinter GUI 编程中的基础控件之一，
它的作用就是允许用户输入内容，从而实现 GUI 程序与用户的交互，
比如当用户登录软件时，输入用户名和密码，此时就需要使用 Entry 控件
'''

import tkinter as tk
import time

# 动态字符串
window = tk.Tk()
window.geometry('450x150+100+100')
window.resizable(False, False)
window.title("时钟")


# 获取时间的函数
def get_time():
    # 获取当前时间
    dstr.set(time.strftime("%H:%M:%S"))
    pass


# 生成动态字符串
dstr = tk.StringVar()
# 利用textvariable来实现文本变化
tk.Label(window, textvariable=dstr, fg='green', font=("微软雅黑", 85)).pack()
# 调用函数
get_time()
window.mainloop()
