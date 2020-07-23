from tkinter import *
from playsound import playsound
import datetime
import time
from win10toast import ToastNotifier
from tkinter import font as tkFont
from tkinter.messagebox import *

def alarm(set_alarm):
    toast = ToastNotifier()
    while True:
        time.sleep(1)
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        if now == set_alarm:
            toast.show_toast("Alarm Clock", duration=1)
            playsound("alarm.mp3")
            break

count = 0
sliderwords = ''

def labelslider():
    global count, sliderwords
    text = 'Welcome to My Alarm'
    if(count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count  += 1 
    intro.configure(text = sliderwords)
    intro.after(220, labelslider)

def get_value():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

def stop():
    root.destroy()

root = Tk()
root.geometry("600x330+330+200")
root.title('Alarm')
root.configure(bg = 'Teal')
root.resizable(False, False)

intro = Label(root, text = '', font = ('Courier New', 25, 'italic bold'), bg = 'Teal', fg = 'Crimson', width = 30)
intro.place(x = 10, y = 5)
info = Label(root, text = "(24)Hour  Min  Sec", font = ("Courier New", 15, "italic bold"), bg = 'Teal', fg = 'MediumSpringGreen')
info.place(x = 200, y = 80)
set_time = Label(root, text = "Set Time", relief = RAISED, font = ("cambria", 13, "bold"), bd = 5, width = 10, fg = 'SeaGreen')
set_time.place(x = 80, y = 136) 

hour = StringVar()
min = StringVar()
sec = StringVar()

hourE = Entry(root, textvariable = hour, width = 5, bd = 5, font = ("cambria", 13, "bold")).place(x = 235, y = 135)
minE = Entry(root, textvariable = min, width = 5, bd = 5, font = ("cambria", 13, "bold")).place(x = 300, y = 135)
secE = Entry(root, textvariable = sec, width = 5, bd = 5, font = ("cambria", 13, "bold")).place(x = 365, y = 135)

submit = Button(root, text ="Set Alarm", width = 13, font = ("cambria", 15, "bold"), relief = RAISED, bd = 5, fg = 'SeaGreen', command = get_value).place(x = 223, y = 220)


labelslider()
root.mainloop()
