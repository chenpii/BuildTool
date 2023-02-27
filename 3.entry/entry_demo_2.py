'''
除了一些基本的属性之外，Entry 控件还提供了一些常用的方法
delete()	根据索引值删除输入框内的值
get()	获取输入框内的值
set()	设置输入框内的值
insert()	在指定的位置插入字符串
index()	返回指定的索引值
select_clear()	取消选中状态
select_adujst()	确保输入框中选中的范围包含 index 参数所指定的字符，选中指定索引和光标所在位置之前的字符
select_from (index)	设置一个新的选中范围，通过索引值 index 来设置
select_present()	返回输入框是否有处于选中状态的文本，如果有则返回 true，否则返回 false。
select_to()	选中指定索引与光标之间的所有值
select_range()	选中指定索引与光标之间的所有值，参数值为 start,end，要求 start 必须小于 end。
'''
import tkinter as tk

window = tk.Tk()
window.geometry('250x100')
window.resizable(False, False)
# 文本标签
tk.Label(window, text='账号：').grid(row=0)
tk.Label(window, text='密码：').grid(row=1)
# 创建对应的输入框
tk.Entry(window, width=20).grid(row=0, column=1)
tk.Entry(window, width=20).grid(row=1, column=1)
window.mainloop()
