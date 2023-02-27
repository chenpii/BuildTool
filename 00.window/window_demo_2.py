from tkinter import *

window = Tk()

# 窗口常用方法
# 设置窗口title
window.title("my title")
# 设置窗口大小：宽x高，注意不能用*，必须使用x
window.geometry('300x200')
# 获取电脑屏幕分辨率
print("电脑的分辨率是%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))
# 要获取窗口的大小，必须先刷新下屏幕，否则返回为1
window.update()
print("窗口的分辨率是%dx%d" % (window.winfo_width(), window.winfo_height()))
# 设置窗口不能被拉伸
# window.resizable(False, False)
# 设置窗口背景颜色
window.config(background='#6fb765')
# 设置窗口始终置顶
# window.attributes('-topmost',True)
# 设置窗口的透明度
window.attributes('-alpha', 1)
# 设置窗口被允许最大/最小调整的范围，与resizable冲突
window.maxsize(600, 600)
window.minsize(50, 50)

# 调用mainloop()显示主窗口
window.mainloop()
