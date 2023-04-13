from tkinter import *
def add():
  num1=int(t1.get())
  num2=int(t2.get())
  sum = num1 + num2
  t3.insert(END,str(sum))

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

b1 = Button(window,text="Add",command=add)
b1.place(x=60,y=180)


   


