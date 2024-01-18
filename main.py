from tkinter import *
from tkinter import filedialog as fd
from pdf2docx import parse
import pathlib

def cback():
    name = fd.askopenfilename()
    ePath.config(state='normal')
    ePath.delete('1', END)
    ePath.insert('1', name)
    ePath.config(state='readonly')

def convert():
    pdf_file = ePath.get()
    word_file = pathlib.Path(pdf_file)
    word_file = word_file.stem + '.docx'
    parse(pdf_file, word_file)
    Label(root, text='Covert complete!', fg='black', bg='white', font='Arial 16 bold').pack(pady=10)


root = Tk()
root.title('Convertor PDF to WORD')
root.geometry('500x400+400+400')
root.resizable(width=False, height=False)
root['bg'] = 'white'

Button(root, text='Select PDF file', font='Arial 16 bold', fg='black', bg='white', command=cback).pack(pady=10)

lbPath = Label(root, text='Path to file:', fg='black', bg='white', font='Arial 16 bold')
lbPath.pack()

ePath = Entry(root, width=50, state='readonly')
ePath.pack(pady=10)

ButtonConvert = Button(root, text='Convert', fg='black', bg='white', font='Arial 16 bold', command=convert).pack(pady=10)

root.mainloop()