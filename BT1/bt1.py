from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title('Form nhóm 2')
window.geometry('800x600')
# window.config(bg='green')

# bg = PhotoImage(file='background.png')
text = Label(window, text='Nhóm 2', fg='red', font=('Arial',50,'bold'))
text.pack(pady=20)

# lbl = tkinter.Label(window, image=bg)
# lbl.pack(pady=20)



tree = ttk.Treeview(window)

tree['columns'] = ('MSSV','Name','Role')
tree.column('#0', width=50, minwidth=25)
tree.column('MSSV', anchor=W, width=80)
tree.column('Name',anchor=CENTER, width=120)
tree.column('Role', anchor=W, width=120)

tree.heading('#0', text='STT', anchor=W)
tree.heading('MSSV', text='MSSV', anchor=W)
tree.heading('Name', text='Họ và tên', anchor=CENTER)
tree.heading('Role', text='Vai trò', anchor=W)

lst = [('2051120071','Nguyễn Ngọc Thiện','Tìm hiểu tkinter'),
       ('2051120073','Lê Trường Thọ','Tìm hiểu latex'),
       ('2051120111','Bùi Quốc Hào','Tìm hiểu tkinter'),
       ('2051120127','Trần Nhật Huy','Tìm hiểu latex'),
       ('2051120044','Từ Thị Cẩm Nhung','Truy vấn sql'),
       ('2051120133','Phạm Nguyễn Duy Khánh','Truy vấn sql'),
       ('2051120090','Nguyễn Huy Bảo','Truy vấn sql')]

for i in range(len(lst)):
       tree.insert(parent='', index='end', iid=i, text=f'{i+1}', values=lst[i])

# tree.insert(parent='', index='end', iid=0, text='1', values=lst[0])
# tree.insert(parent='', index='end', iid=1, text='2', values=lst[1])
# tree.insert(parent='', index='end', iid=2, text='3', values=lst[2])
# tree.insert(parent='', index='end', iid=3, text='4', values=lst[3])
# tree.insert(parent='', index='end', iid=4, text='5', values=lst[4])
# tree.insert(parent='', index='end', iid=5, text='6', values=lst[5])
# tree.insert(parent='', index='end', iid=6, text='7', values=lst[6])

tree.place(x=230,y=140)

# def hello_button():
#        messagebox.showinfo(title='Message',message='Hello mọi người')
#        return

# btn_hello = Button(window, text='Hello', command=hello_button)
# btn_hello.place(x=300,y=400)

btn_quit = Button(window, text='Quit', width=10, command=window.destroy)
btn_quit.place(x=450, y=400)

window.mainloop()
