import tkinter
from tkinter import *
from tkinter import ttk

cor0 = "#444466"
cor01 = "#feffff"
cor02 = "#6f9fbd"

fundo_manha = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"
fundo = fundo_manha

janela = Tk()
janela.title("clima")
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

janela.mainloop()