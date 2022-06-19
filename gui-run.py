from tkinter import *
import tkinter.font as font
from tempchecker import find_highest_temp
from api import maxtemp, processTime


window = Tk()
# add widgets here

window.title('Max Temp Finder')
window.geometry("550x400")
window.eval('tk::PlaceWindow . center')


def display_max_temp():
    
    a = Label(window, text=maxtemp)
    a.place(relx=0.4, rely=0.65)
    print(f"process[{processTime}s]")


myFont = font.Font(family='Arial', weight="bold")
findTempButton = Button(
    window, text="Press to find highest the highest temperature currently in England", command=display_max_temp)
findTempButton['font'] = myFont


findTempButton.pack(ipady=15, ipadx=5, expand=True)


window.mainloop()
