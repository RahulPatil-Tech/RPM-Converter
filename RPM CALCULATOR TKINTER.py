from tkinter import *
from tkinter.ttk import Labelframe
from turtle import left
from tkinter import messagebox
 


def Converter():
    R=int(Rev_box.get())
    M=int(Min_box.get())
    N=int(Rad_box.get())
    RPM= R/M
    print(RPM)
    RPM_index(RPM)
    RPS=RPM*0.10472
    print(RPS)
    RPS_index(RPS)
    MS=0.1047*N*RPM
    print(MS)
    MS_index(MS)
    Hz=RPM/60
    print(Hz)
    Hz_index(Hz)
def RPM_index(RPM):
    messagebox.showinfo('RPM Converter', f'Rate Per Min = {RPM}')
def RPS_index(RPS):
    messagebox.showinfo('RPM Converter', f'Radians Per Sec = {RPS}')
def MS_index(MS):
    messagebox.showinfo('RPM Converter', f'm/s = {MS}')
def Hz_index(Hz):
    messagebox.showinfo('RPM Converter', f'Hz = {Hz}')
    

root = Tk()
root.geometry("500x309")
Rev_user=Label(root,text="Number of Revolution")
Rev_user.grid(row=1,column=1)
Min_user=Label(root,text="Enter Number of Min")
Min_user.grid(row=2,column=1)
Rad_user=Label(root,text="Enter the radious")
Rad_user.grid(row=3,column=1)
Rev_value=StringVar
Min_value=StringVar
Rad_value=StringVar
Rev_box=Entry(root,textvariable=Rev_value)
Rev_box.grid(row=1,column=3)
Min_box=Entry(root,textvariable=Min_value)
Min_box.grid(row=2,column=3)
Rad_box=Entry(root,textvariable=Rad_value)
Rad_box.grid(row=3,column=3)
Button(text="Convert",command=Converter).grid(row=4,column=3)
root.mainloop()