from tkinter import *
import pandas as pd
import back
path = "C:\\Windows\\System32\\"

def view_all():
    list1.delete(0, END)
    res = back.get_file()
    if 'No files exists' in res:
        list1.insert(END, res)
    for line in res:
        s = ""
        for l in line.split(','):
            s = s + "    " +l
        list1.insert(END, s)

def search():
    list1.delete(0, END)
    res = back.get_file(name_text.get())
    if isinstance(res, list):
        list1.insert(END, 'Product Name: '+res[0])
        list1.insert(END, 'Product price: '+res[1])
        list1.insert(END, 'Product Stock: '+res[2])
        list1.insert(END, 'Product Category: '+res[3])
    else:
        list1.insert(END, res)


def insert():
    res = back.insert(name_text.get(), stock_text.get(), category_text.get(), price_text.get())
    res=res.split(',')
    list1.delete(0, END)
    list1.insert(END, "Product details inserted")
    list1.insert(END, "------------------------")
    list1.insert(END, 'Product Name: '+res[0])
    list1.insert(END, 'Product price: '+res[1])
    list1.insert(END, 'Product Stock: '+res[2])
    list1.insert(END, 'Product Category: '+res[3])
    
    
    
window=Tk()

l1=Label(window, text="Product Name")
l1.grid(row=0, column=0)

l2=Label(window, text="Price")
l2.grid(row=0, column=2)

l3=Label(window, text="Stock")
l3.grid(row=1, column=0)

l4=Label(window, text="Product Category")
l4.grid(row=1, column=2)

name_text=StringVar()
e1=Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

price_text=StringVar()
e2=Entry(window, textvariable=price_text)
e2.grid(row=0, column=3)

stock_text=StringVar()
e3=Entry(window, textvariable=stock_text)
e3.grid(row=1, column=1)

category_text=StringVar()
e4=Entry(window, textvariable=category_text)
e4.grid(row=1, column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=3, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window, text="View all", width=12, command=view_all)
b1.grid(row=4, column=3)

b2=Button(window, text="Search", width=12, command=search)
b2.grid(row=5, column=3)

b3=Button(window, text="Add Product", width=12, command=insert)
b3.grid(row=6, column=3)

b4=Button(window, text="Low on stocks", width=12)
b4.grid(row=7, column=3)

b5=Button(window, text="Update selected", width=12)
b5.grid(row=8, column=3)

b6=Button(window, text="Delete Selected", width=12)
b6.grid(row=9, column=3)

b7=Button(window, text="Close", width=12)
b7.grid(row=10, column=3)


window.mainloop()