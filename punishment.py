from tkinter import *
import time

def start_punishment(sec):

    root = Tk()

    root.grab_set()

    root['bg'] = 'black'
    root.title('ТЫ ЗАБАНЕН!!!')
    root.wm_attributes('-alpha', 1)
    root.resizable(False, False)
    root.attributes("-topmost", True)
    root.overrideredirect(True)
    root.state('zoomed')
    def disable_event():
        pass

    root.protocol("WM_DELETE_WINDOW", disable_event)
    count_digit = Label(root, text='0', font='Arial 50 bold', bg='black', fg='white',justify='center')
    count_digit.place(rely=0.5, relx=0.4)

    dur = int(sec)*5
    while dur:
        h = dur//3600
        m = dur%3600//60
        s = dur%3600%60
        msformat = '{:02d}:{:02d}:{:02d}'.format(h,m,s)
        count_digit['text'] = msformat
        count_digit.update()
        time.sleep(1)
        dur-=1

    root.destroy()