from tkinter import*
from tkinter.ttk import*

answers=0
window=Tk()
window.title("welome")
window.geometry('650x750')

def submit ():
    global la, labellast,labelphoto
    win = Tk()
    win.title("submission")
    win.geometry('400x200')
    window.destroy()
    labellast=Label(win,text="     Being eco-friendly\n     makes our planet a\n     better place to live \n Thank you for your time  ",font=('Times', 30))
    labellast.grid(column=0,row=0)


def barchange(*args):
    prog.set(prog.get()+9)

prog=IntVar()
prog.set(1)
bar=Progressbar(window,length=600,style='black.Horizontal.TProgressbar',variable=prog)
bar.grid(column=0,row=0,columnspan=2,pady=5)

l1=Label(window,text="Whats your gender ?",font=('Times', 13))
l1.grid(column=0,row=1,padx=10)
r1=StringVar()
r1.trace("w",barchange)
a1=Radiobutton(window,text='Female',value='Female',variable=r1,)
b1=Radiobutton(window,text='Male',value='Male',variable=r1,)
c1=Radiobutton(window,text='Other ',value='Other ',variable=r1,)
a1.grid(column=0,row=2)
b1.grid(column=0,row=3)
c1.grid(column=0,row=4)

l2=Label(window,text="What's your age ?",font=('Times', 13))
l2.grid(column=0,row=5,padx=10)
r2=StringVar()
r2.trace("w", barchange)
a2=Radiobutton(window,text='0-18',value='0-18',variable=r2)
b2=Radiobutton(window,text='18-50',value='18-50',variable=r2)
c2=Radiobutton(window,text='50+',value='50+',variable=r2,)
a2.grid(column=0,row=6)
b2.grid(column=0,row=7)
c2.grid(column=0,row=8)

l3=Label(window,text="Are you well informed\n    about recycling? ",font=('Times', 13))
l3.grid(column=0,row=9,padx=10)
r3=StringVar()
r3.trace("w",barchange)
a3=Radiobutton(window,text=' A little ',value='A little ',variable=r3,)
b3=Radiobutton(window,text='A lot ',value='A lot ',variable=r3,)
c3=Radiobutton(window,text='Not at all ',value='Not at all ',variable=r3,)
a3.grid(column=0,row=10)
b3.grid(column=0,row=11)
c3.grid(column=0,row=12)

l4=Label(window,text="Do you  separate the disposable waste\n    in your home before disposing it? ",font=('Times', 13))
l4.grid(column=0,row=13,padx=10)
r4=StringVar()
r4.trace("w",barchange)
a4=Radiobutton(window,text='Never ',value='Never',variable=r4)
b4=Radiobutton(window,text='Often',value='Often',variable=r4)
c4=Radiobutton(window,text=' Always',value='Always',variable=r4)
a4.grid(column=0,row=14)
b4.grid(column=0,row=15)
c4.grid(column=0,row=16)




l5=Label(window,text="                       \nDo you do the necessary preparation before\n      throwing the packages in the bin?",font=('Times', 13))
l5.grid(column=1,row=1,padx=10,pady=5)
combo=Combobox(window)
combo['values']=("","Yes","No","Sometimes","I don't know ","What preparation?")
combo.current(0)
combo.bind("<<ComboboxSelected>>",barchange)
combo.grid(column=1,row=2,padx=10)

l6=Label(window,text="Do you avoid plastic packaging \n   when you buy something ?",font=('Times', 13))
l6.grid(column=1,row=3,padx=10,pady=5)
combo2=Combobox(window)
combo2['values']=("","Rarely","Often","Always","I don't pay attention")
combo2.current(0)
combo2.bind("<<ComboboxSelected>>",barchange)
combo2.grid(column=1,row=4,padx=10)

l7=Label(window,text="Are you reusing product packaging?",font=('Times', 13))
l7.grid(column=1,row=5,padx=10,pady=5)
combo3=Combobox(window)
combo3['values']=("","Never","Rarely","Often","Always")
combo3.current(0)
combo3.bind("<<ComboboxSelected>>",barchange)
combo3.grid(column=1,row=6,padx=10)

l8=Label(window,text="Do you use rechargeable\n batteries in your home?",font=('Times', 13))
l8.grid(column=1,row=7,padx=10,pady=5)
combo4=Combobox(window)
combo4['values']=("","Yes","No")
combo4.current(0)
combo4.bind("<<ComboboxSelected>>",barchange)
combo4.grid(column=1,row=8,padx=10)

l9=Label(window,text="Do you know how many times\nwe can recycle a glass bottle ?",font=('Times', 13))
l9.grid(column=1,row=9,padx=10,pady=5)
combo5=Combobox(window)
combo5['values']=("","Once","Twice","As many times as i want " ,"I don't know")
combo5.current(0)
combo5.bind("<<ComboboxSelected>>",barchange)
combo5.grid(column=1,row=10,padx=10,)

l10=Label(window,text="Are you satisfied with the\nrecycling programs in your\n          municipality? ",font=('Times', 13))
l10.grid(column=1,row=11,padx=10,pady=5)
combo6=Combobox(window)
combo6['values']=("","Vary","A little"," Not at all "," I dont know ")
combo6.current(0)
combo6.bind("<<ComboboxSelected>>",barchange)
combo6.grid(column=1,row=12,padx=10)

l11=Label(window,text="I do not recycle because\n it is difficult for me to \nseparate the garbage and \ntransfer it to special bins ",font=('Times', 13))
l11.grid(column=1,row=13,padx=10,pady=5)
combo7=Combobox(window)
combo7['values']=("","Agree","Disagree" ,"I dont know ")
combo7.current(0)
combo7.bind("<<ComboboxSelected>>",barchange)
combo7.grid(column=1,row=14,padx=10)

btn = Button(window,text="Submit",command=submit)
btn.grid(column=1,row=16,padx=5)


window.mainloop()