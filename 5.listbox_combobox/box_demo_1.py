'''
列表框（Listbox）和复选框（Combobox）是 Tkinter 中两个控件，由于其非常相似，本节将它们放在一起进行介绍。
'''
import tkinter as tk

win = tk.Tk()
win.geometry('400x200')
# 创建列表选项
listbox1 = tk.Listbox(win)
listbox1.pack()
# 根据索引值的位置一次插入
# for i, item in enumerate(["C", "C++", "C#", "Python", "Java"]):
#     listbox1.insert(i, item)
# 使用end插入，表示最后一个位置
for item in ["C", "C++", "C#", "Python", "Java"]:
    listbox1.insert("end", item)
win.mainloop()
