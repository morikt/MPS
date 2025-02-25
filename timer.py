from tkinter import *
from tkinter import ttk
import time



def start_timer(seconds,o):

    root = Toplevel()

    root.grab_set()

    root['bg'] = 'black'
    root.title('ДЕДЛАЙН')
    root.wm_attributes('-alpha', 1)
    root.geometry('500x100+0+820')
    root.resizable(False, False)
    root.attributes("-topmost", True)
    root.overrideredirect(True)
    def disable_event():
        pass

    root.protocol("WM_DELETE_WINDOW", disable_event)

    frame = Frame(root, bg='black')
    frame.place(relwidth=1, relheight=0.5)

    title = Label(frame, text='Дедлайн', bg="#480607", font=80, fg='white', width=350)
    title.pack()

    count_digit = Label(frame, text='0', font='Arial 20 bold', bg='black', fg='white')
    count_digit.pack()

    o.destroy()
    dur = int(seconds)
    while dur:
        h = dur//3600
        m = dur%3600//60
        s = dur%3600%60
        msformat = '{:02d}:{:02d}:{:02d}'.format(h,m,s)
        count_digit['text'] = msformat
        count_digit.update()
        time.sleep(1)
        dur-=1
    root.grab_release()
    root.destroy()

