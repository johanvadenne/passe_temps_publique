# coding: utf-8
from tkinter import *

def actionEvent(event):     
    lbl.configure(text = "Vous avez tapé = "+ entry.get())     

root = Tk()
root.geometry("300x150")
entry = Entry(root)

# Association de l'évènement actionEvent au champ de saisie
entry.bind("<Return>", actionEvent) 
lbl = Label(root, text = ".....") 
entry.pack() 
lbl.pack() 
root.mainloop()