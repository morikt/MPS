from tkinter import *
from tkinter import ttk
import time
#import vlc

#player = vlc.MediaPlayer('file:///tmp/foo.avi')

seconds = 60

def start_timer():
    dur = seconds
    while dur:
        m, s = divmod(dur,60)
        msformat = '{:02d}:{:02d}'.format(m,s)
        count_digit['text'] = msformat
        count_digit.update()
        time.sleep(1)
        dur-=1


root = Tk()
root['bg'] = 'black'
root.title('ДЕДЛАЙН')
root.wm_attributes('-alpha', 1)
root.geometry('500x100')
root.resizable(False,False)

frame = Frame(root, bg='black')
frame.place(relwidth=1,relheight=0.5)

title = Label(frame, text='Дедлайн', bg="#480607",font=80, fg='white', width=350)
title.pack()

count_digit = Label(frame,text='0', font='Arial 20 bold', bg='black', fg='white')
count_digit.pack()

frame1 = Frame(root, bg='black')
frame1.place(rely = 0.5,relwidth=1,relheight=0.5)

btn_start = Button(frame1, text="Start",font='Arial 12 bold',fg='white', bg='#480607', command=start_timer)
btn_start.pack()


root.mainloop()