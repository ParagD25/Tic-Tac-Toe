from tkinter import *

def click_1():
    b1['state']='disabled'
    b1['bg']='#D4D4D4'
def click_2():
    b2['state']='disabled'
    b2['bg']='#D4D4D4'
def click_3():
    b3['state']='disabled'
    b3['bg']='#D4D4D4'

def click_4():
    b4['state']='disabled'
    b4['bg']='#D4D4D4'
def click_5():
    b5['state']='disabled'
    b5['bg']='#D4D4D4'
def click_6():
    b6['state']='disabled'
    b6['bg']='#D4D4D4'

def click_7():
    b7['state']='disabled'
    b7['bg']='#D4D4D4'
def click_8():
    b8['state']='disabled'
    b8['bg']='#D4D4D4'
def click_9():
    b9['state']='disabled'
    b9['bg']='#D4D4D4'
      
ttt=Tk()
ttt.config(background='white')
b1=Button(ttt,height=4,width=10,bd=2,bg='white',relief='groove',command=click_1)
b2=Button(ttt,height=4,width=10,bd=2,bg='white',relief='groove',command=click_2)
b3=Button(ttt,height=4,width=10,bd=2,bg='white',relief='groove',command=click_3)
b4=Button(ttt,height=4,width=10,bd=2,bg='white',relief='groove',command=click_4)
b5=Button(ttt,height=4,width=10,bd=2,bg='white',relief='groove',command=click_5)
b6=Button(ttt,height=4,width=10,bd=2,bg='white',relief='groove',command=click_6)
b7=Button(ttt,height=4,width=10,bd=2,bg='white',relief='groove',command=click_7)
b8=Button(ttt,height=4,width=10,bd=2,bg='white',relief='groove',command=click_8)
b9=Button(ttt,height=4,width=10,bd=2,bg='white',relief='groove',command=click_9)
reset=Button(ttt,text='Reset',bd=2,bg='white',relief='groove',fg='blue')
close=Button(ttt,text='Close',bd=2,bg='white',relief='groove',fg='red',command=ttt.destroy)

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
close.grid(row=3,column=2)
reset.grid(row=3,column=0)

ttt.mainloop()