from ctypes import *
from tkinter import *
from tkinter import ttk
import ctypes
import os

class DequePY:
    def __init__(self):
        self.items = []

    def insertTail(self, item):
        self.items.insert(0, item)

    def insertHead(self, item):
        self.items.append(item)

    def deleteTail(self):
        if not self.is_empty():
            return self.items.pop(0)

    def deleteHead(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def deleteDeque(self):
        self.items.clear()

    def countDeque(self):
        return len(self.items)

    def dequeElement(self, i):
        if 0 <= i < len(self.items):
            return self.items[i]
        return None

cpp_lib = True # True - библиотека на плюсах, False - на питоне

if cpp_lib:

    os.add_dll_directory(r'C:\Users\GreamZ\PycharmProjects\Laba')
    lib = ctypes.CDLL('./deque.dll', winmode=0)

    class Node(Structure):
        pass

    Node._fields_ = [("data", c_int), ("next", POINTER(Node)), ("prev", POINTER(Node))]

    class Deque(Structure):
        _fields_ = [("head", POINTER(Node)), ("tail", POINTER(Node)), ("cnt", c_int)]

    lib.createDeque.restype = POINTER(Deque)
    lib.insertHead.argtypes = [POINTER(Deque), c_int]
    lib.insertTail.argtypes = [POINTER(Deque), c_int]
    lib.deleteHead.argtypes = [POINTER(Deque)]
    lib.deleteTail.argtypes = [POINTER(Deque)]
    lib.deleteDeque.argtypes = [POINTER(Deque)]
    lib.countDeque.argtypes = [POINTER(Deque)]
    lib.countDeque.restype = c_int
    lib.dequeElement.argtypes = [POINTER(Deque), c_int]
    lib.dequeElement.restype = c_int

    class Deque_lib:
        def createDeque(self): return lib.createDeque()
        def insertHead(self, deq, val): lib.insertHead(deq, val)
        def insertTail(self, deq, val): lib.insertTail(deq, val)
        def deleteHead(self, deq): lib.deleteHead(deq)
        def deleteTail(self, deq): lib.deleteTail(deq)
        def deleteDeque(self, deq): lib.deleteDeque(deq)
        def countDeque(self, deq): return lib.countDeque(deq)
        def dequeElement(self, deq, idx): return lib.dequeElement(deq, idx)

else:
    class Deque_lib:
        def createDeque(self): return DequePY()
        def insertHead(self, deq, val): deq.insertHead(val)
        def insertTail(self, deq, val): deq.insertTail(val)
        def deleteHead(self, deq): deq.deleteHead()
        def deleteTail(self, deq): deq.deleteTail()
        def deleteDeque(self, deq): deq.deleteDeque()
        def countDeque(self, deq): return deq.countDeque()
        def dequeElement(self, deq, idx): return deq.dequeElement(idx)

libb = Deque_lib()

root = Tk()
root.title("Демонстрейшен")
root.geometry("500x500")
root.resizable(False,False)

list = []
check = 0
def insHead():
    global entry, btn, label, flag, check, errCheck

    if check == 0:
        check = 1
        errCheck = 1
        label = ttk.Label(text="Введите число")
        label.place(x = 220, y = 265)
        entry = ttk.Entry()
        entry.place(relx=.4, rely=.6)
        btn = ttk.Button(text="Принять", command = confirm)
        btn.place(x = 340, y = 298)
        flag = 1

def insTail():
    global entry, btn, flag, label, check, errCheck

    if check == 0:
        check = 1
        errCheck = 1
        label = ttk.Label(text="Введите число")
        label.place(x = 220, y = 265)
        entry = ttk.Entry()
        entry.place(relx=.4, rely=.6)
        btn = ttk.Button(text="Принять", command = confirm)
        btn.place(x = 340, y = 298)
        flag = 0

def confirm():
    global entry, btn, label, num, flag, check, errCheck, error
    temp = entry.get()
    try:
        num = int(temp)
        if flag == 1:
            libb.insertHead(Deq,num)
        else:
            libb.insertTail(Deq,num)
        libb.countDeque(Deq)
        entry.destroy()
        btn.destroy()
        label.destroy()
        displayDeq()
        check = 0
        if errCheck == 0:
            error.destroy()
    except ValueError:
        if errCheck == 1:
            errCheck = 0
            error = ttk.Label(text = "Вы ввели не число",foreground="red")
            error.place(x = 210, y = 325)

def displayDeq():
    global Deq, list

    for j in list:
        j.destroy()
    list.clear()

    cnt = libb.countDeque(Deq)
    for i in range(cnt):
        num = libb.dequeElement(Deq, i)
        element = ttk.Label(text=(num))
        element.place(x = 100 + (i * 30), y = 150)
        list.append(element)

def remHead():
    global Deq
    libb.deleteHead(Deq)
    displayDeq()

def remTail():
    global Deq
    libb.deleteTail(Deq)
    displayDeq()

def deleteDeq():
    global btnInsertHead,btnInsertTail,btnRemoveHead,btnRemoveTail,btnDeleteDeq, btn, list
    libb.deleteDeque(Deq)
    btnInsertHead.destroy()
    btnInsertTail.destroy()
    btnRemoveHead.destroy()
    btnRemoveTail.destroy()
    btnDeleteDeq.destroy()
    for j in list:
        j.destroy()
    list.clear()
    btn = ttk.Button(text="Создать дек", command=createDeq)
    btn.place(relx=.5, rely=.5, anchor="center", width=80, height=60)

def createDeq():
    global Deq, btn, btnInsertHead, btnInsertTail, btnRemoveHead, btnRemoveTail, btnDeleteDeq
    Deq = libb.createDeque()
    btn.destroy()
    btnInsertHead = ttk.Button(text = "Добавить голову", command = insHead)
    btnInsertHead.place(relx=.2, rely=.7, width = 120, height = 40)
    btnInsertTail = ttk.Button(text="Добавить хвост", command = insTail)
    btnInsertTail.place(relx=.6, rely=.7, width=120, height=40)
    btnRemoveHead = ttk.Button(text="Удалить голову", command = remHead)
    btnRemoveHead.place(relx=.2, rely=.8, width=120, height=40)
    btnRemoveTail = ttk.Button(text="Удалить хвост", command = remTail)
    btnRemoveTail.place(relx=.6, rely=.8, width=120, height=40)
    btnDeleteDeq= ttk.Button(text="Удалить дек", command=deleteDeq)
    btnDeleteDeq.place(relx=.4, rely=.9, width=120, height=40)

btn = ttk.Button(text="Создать дек", command=createDeq)
btn.place(relx=.5, rely=.5, anchor="center", width = 80, height = 60)

root.mainloop()

