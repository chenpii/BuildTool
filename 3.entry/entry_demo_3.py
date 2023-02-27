'''
Entry 控件也提供了对输入内容的验证功能，比如要求输入英文字母，你却输入了数字，这就属于非法输入，Entry 控件通过以下参数实现对内容的校验：
validate	指定验证方式，字符串参数，参数值有 focus、focusin、focusout、key、all、none。
validatecommand	指定用户自定义的验证函数，该函数只能返回 True 或者 Fasle
invalidcommand	当 validatecommand 指定的验证函数返回 False 时，可以使用该参数值再指定一个验证函数。

focus	当 Entry 组件获得或失去焦点的时候验证
focusin	当 Entry 组件获得焦点的时候验证
focusout	当 Entry 组件失去焦点的时候验证
key	当输入框被编辑的时候验证
all	当出现上边任何一种情况的时候验证
none	 默认不启用验证功能，需要注意的是这里是字符串的 'none'
'''

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
# 主窗口
win.geometry('250x200+250+200')
win.resizable(0, 0)

# 新建文本标签
tk.Label(win, text='账号：').grid(row=0)
tk.Label(win, text='密码：').grid(row=1)


def check():
    if (Dy_String.get() == "test"):
        messagebox.showinfo("账号输入正确")
        return True
    else:
        messagebox.showinfo("账号输入错误")
        entry1.delete(0, 'end')
        return False


# 创建活动字符串
Dy_String = tk.StringVar()
# 使用验证参数validate,参数值为focusout，即当失去焦点的时候，验证输入框的内容是否正确
entry1 = tk.Entry(win, textvariable=Dy_String, validate='focusout', validatecommand=check)
entry2 = tk.Entry(win, show='*')
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
win.mainloop()
