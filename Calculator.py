from tkinter import *

root=Tk()
root.title('Calculator')
root.geometry('354x460')

mylabel=Label(root,text="CALCULATOR",font=("Courier New",30,'bold')).pack(side=TOP)

textin=StringVar()
operator=""

def clickbut(numbers):
	global operator
	operator = operator + str(numbers)
	textin.set(operator)

def clrbut():
	textin.set('')

def equbut():
	global operator
	try:
		add=str(eval(operator))
	except:
		add = str(eval(textin.get()))
	textin.set(add)
	operator=''

# Buttons
metext = Entry(root,font=("Courier New",12,'bold'),textvar=textin,width=25,bd=5,bg='powder blue').pack()

b1 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(1),text="1",font=("Courier New",10,'bold'))
b1.place(x=10,y=100)

b2 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(2),text="2",font=("Courier New",10,'bold'))
b2.place(x=10,y=170)

b3 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(3),text="3",font=("Courier New",10,'bold'))
b3.place(x=10,y=240)

b4 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(4),text="4",font=("Courier New",10,'bold'))
b4.place(x=75,y=100)

b5 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(5),text="5",font=("Courier New",10,'bold'))
b5.place(x=75,y=170)

b6 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(6),text="6",font=("Courier New",10,'bold'))
b6.place(x=75,y=240)

b7 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(7),text="7",font=("Courier New",10,'bold'))
b7.place(x=140,y=100)

b8 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(8),text="8",font=("Courier New",10,'bold'))
b8.place(x=140,y=170)

b9 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(9),text="9",font=("Courier New",10,'bold'))
b9.place(x=140,y=240)

b0 = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut(0),text="0",font=("Courier New",10,'bold'))
b0.place(x=10,y=310)

plus = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut('+'),text="+",font=("Courier New",10,'bold'))
plus.place(x=205,y=100)

minus = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut('-'),text="-",font=("Courier New",10,'bold'))
minus.place(x=205,y=170)

mult = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut('*'),text="*",font=("Courier New",10,'bold'))
mult.place(x=205,y=240)

divi = Button(root,padx=18,pady=18,bd=4,bg='light blue',command=lambda:clickbut('/'),text="/",font=("Courier New",10,'bold'))
divi.place(x=205,y=310)

dot = Button(root,padx=50,pady=18,bd=4,bg='light blue',command=lambda:clickbut('.'),text=".",font=("Courier New",10,'bold'))
dot.place(x=75,y=310)

clear = Button(root,padx=14,pady=123,bd=4,bg='light blue',command=clrbut,text="CE",font=("Courier New",10,'bold'))
clear.place(x=270,y=100)

equal = Button(root,padx=151,pady=14,bd=4,bg='light blue',command=equbut,text="=",font=("Courier New",10,'bold'))
equal.place(x=10,y=380)

root.mainloop()