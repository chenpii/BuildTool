'''
当列表的项目过多时，用到 Combobox 控件，也就是下拉菜单控件（或称复合框），
该控件是列表控件的改进版，具有更加灵活的界面，因此其应用场景相比于前者要更加广泛。

不过需要注意的是 Combobox 并不包含在 tkinter 模块中，
而是包含在tkinter.ttk子模块中，
因此若想使用 Combobox 控件，需要使用下面的导包方式：
'''
import tkinter as tk
# 导入ttk模块，下拉菜单控件combobox位于ttk子模块中
from tkinter import ttk

win = tk.Tk()
win.geometry('400x250')
win.resizable(0, 0)

# 创建下拉菜单
combobox = ttk.Combobox(win)
# 使用grid()控制控件的位置
combobox.grid(row=1, sticky='NW')
# 设置下拉菜单的值
combobox['value'] = ('C', 'C#', 'Go', 'Python', 'Java')
# 通过current（）设置下拉菜单选项的默认值
combobox.current(3)


# 编写回调函数，绑定执行事件，向文本插入选中文本
def func(event):
    text.insert('insert', combobox.get() + "\n")


combobox.bind("<<ComboboxSelected>>", func)

# 新建文本框
text = tk.Text(win)
text.grid(pady=5)

win.mainloop()
