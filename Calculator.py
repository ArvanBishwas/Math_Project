from tkinter import *

def bClick(numbers):
     global operator
     operator=operator + str(numbers)
     text_Input.set(operator)

def bclearDisplay():
     global operator
     operator=""
     text_Input.set("")

def bequalsInput():
     global operator
     sumup=str(eval(operator))
     text_Input.set(sumup)
     operator=""

cal = Tk()
cal.title("Calculator")
operator=""
text_Input = StringVar()


textDisplay = Entry(cal,font=('atial',20,'bold'),textvariable=text_Input,bd=30,
                    insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)



b7=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="7",command=lambda:bClick(7)).grid(row=1,column=0)

b8=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="8",command=lambda:bClick(8)).grid(row=1,column=1)

b9=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="9",command=lambda:bClick(9)).grid(row=1,column=2)

Add=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
           bg="powder blue",text="+",command=lambda:bClick("+")).grid(row=1,column=3)

#=================================================================

b4=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="4",command=lambda:bClick(4)).grid(row=2,column=0)

b5=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="5",command=lambda:bClick(5)).grid(row=2,column=1)

b6=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="6",command=lambda:bClick(6)).grid(row=2,column=2)

sub=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
           bg="powder blue",text="-",command=lambda:bClick("-")).grid(row=2,column=3)

#===================================================================

b1=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="1",command=lambda:bClick(1)).grid(row=3,column=0)

b2=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="2",command=lambda:bClick(2)).grid(row=3,column=1)

b3=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="3",command=lambda:bClick(3)).grid(row=3,column=2)

mul=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
           bg="powder blue",text="*",command=lambda:bClick("*")).grid(row=3,column=3)

#===================================================================

b0=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text="0",command=lambda:bClick(0)).grid(row=4,column=0)

bfloat=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
          text=".",command= lambda:bClick('.')).grid(row=4,column=1)

bclear=Button(cal,padx=16,bd=8,fg="black",font=('atial',20,'bold'),
          bg="powder blue",text="C",command= bclearDisplay).grid(row=4,column=2)

div=Button(cal,padx=16,bd=8, fg="black",font=('atial',20,'bold'),
           bg="powder blue",text="/",command=lambda:bClick("/")).grid(row=4,column=3)

#====================================================================

bequals=Button(cal,padx=148,bd=8,fg="black",font=('atial',20,'bold'),
          bg="powder blue",text="=",command= bequalsInput).grid(columnspan=4)

cal.mainloop()
