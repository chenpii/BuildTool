import tkinter as tk
from tkinter import ttk
from numpy import Inf

# 定义选择框内容
select = {
    "一、二级":
        {
            "工业建筑":
                {
                    "厂房":
                        {
                            "甲、乙": [15, 15, 20, 25, 30, 35],
                            "丙": [15, 15, 20, 25, 30, 40],
                            "丁、戊": [15, 15, 15, 15, 15, 20]
                        },
                    "仓库":
                        {
                            "甲、乙": [15, 15, 25, 25, None, None],
                            "丙": [15, 15, 25, 25, 35, 45],
                            "丁、戊": [15, 15, 15, 15, 15, 20]
                        }
                },
            "民用建筑":
                {
                    "住宅": [15, 15, 15, 15, 15, 15],
                    "公共建筑":
                        {
                            "单层及多层": [15, 15, 15, 25, 30, 40],
                            "高层": [None, None, None, 25, 30, 40]
                        }
                }
        },
    "三级":
        {
            "工业建筑":
                {
                    "乙、丙": [15, 20, 30, 40, 45, None],
                    "丁、戊": [None, None, None, 20, 25, 35]
                },
            "单层及多层民用建筑": [15, 20, 25, 30, None]
        },
    "四级":
        {
            "丁、戊类工业建筑": [15, 20, 25, None, None, None],
            "单层及多层民用建筑": [15, 20, 25, None, None, None]
        }
}

# 创建窗体
win = tk.Tk()
# 选项一
lable1 = tk.Label(win, text='选项一')
lable1.grid(row=0, column=0)
fire_level_range = tk.StringVar()
fire_level_range.set(tuple(select.keys()))
listbox1 = tk.Listbox(win, listvariable=fire_level_range)
listbox1.grid(row=1, column=0)

# 选项二
lable2 = tk.Label(win, text='选项二')
lable2.grid(row=0, column=1)
build_name_range = tk.StringVar()
listbox2 = tk.Listbox(win, listvariable=build_name_range)
listbox2.grid(row=1, column=1, padx=5)

# 选项三
lable3 = tk.Label(win, text='选项三')
lable3.grid(row=0, column=1)
build_type_range = tk.StringVar()
listbox3 = tk.Listbox(win, listvariable=build_type_range)
listbox3.grid(row=1, column=2, padx=5)


# 选项一选中时调用
def fun1(event):
    listbox2.delete(0, tk.END)
    global fire_level
    fire_level = listbox1.get(listbox1.curselection())
    global build_name_range
    build_name_range.set(tuple(select[fire_level].keys()))


# 选项二选中时调用
def fun2(event):
    listbox3.delete(0, tk.END)
    global build_name
    build_name = listbox2.get(listbox2.curselection())
    build_type_range.set(tuple(select[fire_level][build_name].keys()))


# 绑定事件
listbox1.bind("<<ListboxSelect>>", fun1)
listbox2.bind("<<ListboxSelect>>", fun2)

# 输入框
entry = tk.Entry(win)
entry.grid(row=2)

# 阈值区间
all_range = [[0, 1500], [1500, 3000], [3000, 5000], [5000, 20000], [20000, 50000], [50000, float(Inf)]]


def cal():
    build_vol = int(entry.get())
    for item in all_range:
        if (build_vol > item[0] and build_vol <= item[1]):
            index = all_range.index(item)
            break


button = tk.Button(win, text='计算', command=cal)
button.grid(row=3)
win.mainloop()
