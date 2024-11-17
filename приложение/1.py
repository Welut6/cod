from tkinter import *

def click():
    lbl.configure(text="why....")

        
window = Tk() #начало окна
window.geometry('400x250') #размер окна
window.title("Тест") #название окна

lbl = Label(window, text="текст:", font=("Arial Bold",16)) #текст 
lbl.grid(column=0, row=0) #комманда для отображения текста

btn = Button(window, text="i am a button", command=click ,bg="black",fg="red") #кнопка
btn.grid(column=0,row=1) #комманда для отображения кнопки

window.mainloop()