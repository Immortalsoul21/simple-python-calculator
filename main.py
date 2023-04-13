from tkinter import *









window = Tk()
window.geometry("400x300")
window.title("simple calculator")

labl1 = Label(window,text="Enter 1st Number:")
labl1.place(x=54,y=50)

labl2 = Label(window,text="Enter 2nd Number:")
labl2.place(x=50,y=100)

t1 = Entry()
t1.place(x=170,y=50)

t2 = Entry()
t2.place(x=170, y=100)

labl3= Label(window,text="Result: ")
labl3.place(x=70,y=140)

t3= Entry()
t3.place(x=170,y=140)

def add():
  num1=int(t1.get())
  num2=int(t2.get())
  sum = num1 + num2
  t3.insert(END,str(sum))

b1 = Button(window,text="Add",command=add)
b1.place(x=50,y=200)

def sub():
  num1=int(t1.get())
  num2=int(t2.get())
  dif = num1 - num2
  t3.insert(END,str(dif))

b2 = Button(window,text="Sub",command=sub)
b2.place(x=120,y=200)

def multiply():
  num1=int(t1.get())
  num2=int(t2.get())
  product = num1 * num2
  t3.insert(END,str(product))
b3 = Button(window,text="Multiply",command=multiply)
b3.place(x=220,y=200)


def div():
  num1=int(t1.get())
  num2=int(t2.get())
  div = num1 / num2
  t3.insert(END,str(div))


b4 = Button(window,text="Divide",command=div)
b4.place(x=320,y=200)

def clear():
  t1.delete(0,END)
  t2.delete(0,END)
  t3.delete(0,End)

b5 = Button(window,text="Clear",command=clear)
b5.place(x=180,y=250)

   


