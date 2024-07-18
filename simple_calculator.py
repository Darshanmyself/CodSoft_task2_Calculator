from tkinter import *

root =Tk()
root.title('Simple Calculator')

root.configure(bg='black')

e= Entry(root, width=35, borderwidth=5,bg='grey',fg='black',font='arial 10 bold')
e.grid(row=0,column=0,columnspan=4, padx=10, pady=10)

def but_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def but_clr():
    e.delete(0,END)
    
    
    

def but_add():
    first_num= e.get()
    global f_num
    global math
    math='addition'
    f_num=int(first_num)
    e.delete(0,END)

def but_equal():
    sec_num=e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,f_num+int(sec_num))
    if math=='subtraction':
        e.insert(0,f_num-int(sec_num))
    if math=='multiplication':
        e.insert(0,f_num*int(sec_num))
    if math=='division':
        e.insert(0,f_num/int(sec_num))

def but_sub():
    first_num= e.get()
    global f_num
    global math
    math='subtraction'
    f_num=int(first_num)
    e.delete(0,END)
    
def but_mul():
    first_num= e.get()
    global f_num
    global math
    math='multiplication'
    f_num=int(first_num)
    e.delete(0,END)

def but_div():
    first_num= e.get()
    global f_num
    global math
    math='division'
    f_num=int(first_num)
    e.delete(0,END)
    

but_1=Button(root, text='1' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(1))
but_2=Button(root, text='2' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(2))
but_3=Button(root, text='3' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(3))
but_4=Button(root, text='4' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(4))
but_5=Button(root, text='5' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(5))
but_6=Button(root, text='6' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(6))
but_7=Button(root, text='7' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(7))
but_8=Button(root, text='8' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(8))
but_9=Button(root, text='9' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(9))
but_0=Button(root, text='0' , padx=40, pady=20, bg='black',fg='white',font='times 10 bold',borderwidth=5,relief=RAISED,command=lambda: but_click(0))


but_eq=Button(root, text='=' , padx=80, pady=20, command=but_equal, bg='green',fg='white',relief=RAISED,font=20,borderwidth=5)
but_clr=Button(root, text='CLEAR' , padx=22, pady=20, bg='red',fg='white',font='times 9 bold',borderwidth=5,relief=RAISED,command=but_clr)

but_pls=Button(root, text='+' , padx=40, pady=20, borderwidth=5,bg='black',fg='white',font='times 10 bold',relief=RAISED,command=but_add)
but_sub=Button(root, text='--' , padx=40, pady=20, borderwidth=5,bg='black',fg='white',font='times 10 bold',relief=RAISED,command=but_sub)
but_mul=Button(root, text='x' , padx=40, pady=20, borderwidth=5,bg='black',fg='white',font='times 10 bold',relief=RAISED,command=but_mul)
but_div=Button(root, text='/' , padx=40, pady=20, borderwidth=5,bg='black',fg='white',font='times 10 bold',relief=RAISED,command=but_div)

#positioning buttons on the screen

but_1.grid(row=3, column=0)
but_2.grid(row=3, column=1)
but_3.grid(row=3, column=2)

but_4.grid(row=2, column=0)
but_5.grid(row=2, column=1)
but_6.grid(row=2, column=2)

but_7.grid(row=1, column=0)
but_8.grid(row=1, column=1)
but_9.grid(row=1, column=2)

but_div.grid(row=4, column=0)
but_0.grid(row=4, column=1)
but_clr.grid(row=4, column=2)

but_eq.grid(row=6, column=0,columnspan=3)


but_pls.grid(row=5, column=0)
but_sub.grid(row=5, column=1)
but_mul.grid(row=5, column=2)


root.mainloop()
