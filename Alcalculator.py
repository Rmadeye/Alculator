# -*- coding: utf-8 -*-
"""
Moonshine dilution calculator
"""
from tkinter import *

import backend as ba
import pandas as pd

density = pd.read_excel("./EtOH.xlsx")

window=Tk()
window.wm_title("Moonshine calculator")

def front():
    vol=float(e2.get())
    per=float(e1.get())
    des=float(e3.get())
    a = density.loc[density['Percentage']==float(per)]
    den=float(a['Density'])
    b=density.loc[density['Percentage']==float(des)]
    dendes=float(b['Density'])
  
    add_water=ba.Calculations.calc_dil(vol,des,dendes,den,per)
    pure_alc=ba.Calculations.count_pure(vol,per,den)
    """
    Answer labels
    """
    l10=Label(window,text="You need to add").grid(row=5,column=0)
    l11=Label(window,text="mL of water").grid(row=5,column=2)
    l12=Label(window,text=round(add_water,2)).grid(row=5,column=1)
    l13=Label(window,text="Density of initial solution[g/mL]:").grid(row=6,column=0)
    l14=Label(window,text=den).grid(row=6,column=1)
    l15=Label(window,text="Density of final solution[g/mL]:").grid(row=7,column=0)
    l16=Label(window,text=dendes).grid(row=7,column=1)
    l17=Label(window,text="Pure alcohol (in grams):").grid(row=8,column=0)
    l18=Label(window,text=round(pure_alc,2)).grid(row=8,column=1)
    l19=Label(window,text="Total volume[mL]").grid(row=9,column=0)
    l20=Label(window,text=round(vol+add_water,2)).grid(row=9,column=1)    
    
    
"""
Labels
"""
#Percentage
l1=Label(window,text="What's the percentage of the solution?").grid(row=0,column=0)
l2=Label(window,text="%").grid(row=0,column=2)
#Volume
l3=Label(window,text="What's initial volume?").grid(row=1,column=0)
l4=Label(window,text="mL").grid(row=1,column=2)
#Dilution %
l6=Label(window,text="What's the desired percentage?").grid(row=2,column=0)
l5=Label(window,text="%").grid(row=2,column=2)
# Trademark
lmad=Label(window, text="Created by MadEye", bg="blue",font=("Helvetica 8"), fg="red").grid(row=4,column=0)
"""
Entries
"""
#Percentage
e1=Entry(window)
e1.grid(row=0,column=1)
#Volume
e2=Entry(window)
e2.grid(row=1,column=1)
#Dilution %
e3=Entry(window)
e3.grid(row=2,column=1)
#Density
"""
Buttons
"""

b1=Button(window,text="Run!", command=front)
b1.grid(row=4,column=2)

window.mainloop()
