from tkinter import *

from XuLyFile import DocFile, LuuFile


def themAction():
    line = stringMa.get() + ";" + stringTen.get() + ";" + stringNam.get()
    LuuFile(line)
    stringTen.set("")
    stringNam.set("")
    stringMa.set("")
    showList()


def showList():
    arrSach = DocFile()
    listbox.delete(0, END)
    for item in arrSach:
        listbox.insert(END, item)


root = Tk()
stringMa = StringVar()
stringTen = StringVar()
stringNam = StringVar()
Label(root, text="Quản Lý Sách", fg='blue', font=("cambria", 16)).grid(row=0, columnspan=2)
root.title("Quản lý sách")
root.minsize(height=300, width=310)
root.resizable(height=True, width=True)

listbox = Listbox(root, width=50)
listbox.grid(row=1, columnspan=2)
showList()
Label(root, text="Mã sách:").grid(row=2, column=0)
Entry(root, width=35, textvariable=stringMa).grid(row=2, column=1)
Label(root, text="Tên sách:").grid(row=3, column=0)
Entry(root, width=35, textvariable=stringTen).grid(row=3, column=1)
Label(root, text="Năm xuất bản:").grid(row=4, column=0)
Entry(root, width=35, textvariable=stringNam).grid(row=4, column=1)
frameButton = Frame(root)
Button(frameButton, text="Thêm", command=themAction).pack(side=LEFT)
Button(frameButton, text="Tìm").pack(side=LEFT)
Button(frameButton, text="Sắp xếp").pack(side=LEFT)
Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=5, column=1)
root.mainloop()
