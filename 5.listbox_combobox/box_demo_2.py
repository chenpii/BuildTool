'''
增加滚动条和删除功能
'''
from tkinter import *

win = Tk()
win.geometry('400x180')
# 创建滚动条
s = Scrollbar(win)
# 设置垂直滚动条显示的位置，使得滚动条，靠右侧；通过 fill 沿着 Y 轴填充
s.pack(side=RIGHT, fill=Y)

# 设置为多选模式，并为控件添加滚动条
listbox1 = Listbox(win, selectmode=MULTIPLE,  height=10, yscrollcommand=s.set)
for i, item in enumerate(range(1, 50)):
    listbox1.insert(i, item)
listbox1.pack()
# 设置滚动条，使用 yview使其在垂直方向上滚动
# Listbox 组件的内容，通过绑定 Scollbar 组件的 command 参数实现
s.config(command=listbox1.yview)
# 使用匿名函数,创建删除函数，点击删除按钮，会删除选项
bt = Button(win, text='删除', command=lambda x=listbox1: x.delete(ACTIVE))
# 将按钮放置在底部
bt.pack(side=BOTTOM)
win.mainloop()
