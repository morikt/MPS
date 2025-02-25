from tkinter import *
from tkinter import ttk
from model import Tasks
from database import insert_task, get_results, delete_task, update_task, complete_to_do
from timer import start_timer


class Window(Tk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title('Новое окно')
        self.geometry('250x250')
        self['bg'] = 'black'
        self.window_add = Label(self, text='', bg="#480607", font=40, fg='white', width=100)
        self.enter_add = Entry(self, width=50, font=40)
        self.confirm_add = Button(self, text="Подтвердить", width=70, font=40, bg='#480607',fg='white',
                                  command=self.button_clicked)
        self.entr_add = 0

        self.enter_d = Entry(self, width=50, font=40)


    def get_data(self,pady):
        #enter
        self.enter_add.pack(pady=pady)
        #button
        self.confirm_add.pack(pady=pady)

        try:
            self.entr_add.pack(pady=10)
            self.enter_d.pack()
        except:
            pass

    def button_clicked(self):
        add(self.enter_add.get())
        show()
        try:
            if int(self.enter_d.get()) > 0:
                start_timer(self.enter_d.get(),self)
        except:
            self.destroy()

    def button_clicked1(self):
        delete(int(self.enter_add.get()))
        show()
        self.destroy()

    def button_clicked2(self):
        a,b = map(str, self.enter_add.get().split())
        update(a,b)
        show()
        self.destroy()

    def button_clicked3(self):
        complete(int(self.enter_add.get()))
        show()
        self.destroy()


root = Tk()
root['bg'] = 'black'
root.title('MPS - MEXT PREPARATION')
root.wm_attributes('-alpha', 1)
root.geometry('500x450')

canvas = Canvas(root, height=450, width=500, bg= 'black', highlightthickness=0)
canvas.pack()

frame = Frame(root, bg='black')
frame.place(rely=0.2,relwidth=1,relheight=0.5)

title = Label(frame, text='MPS', bg="#480607",font=80, fg='white', width=350)
title.pack()

columns = ("#", "TASKS", "PROGRESS", "STARTING DATE", "ENDING DATE")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)

tree.heading("#",text="#")
tree.heading("TASKS", text='TASKS')
tree.heading("PROGRESS", text='PROGRESS')
tree.heading("STARTING DATE", text='STARTING DATE')
tree.heading("ENDING DATE", text='ENDING DATE')

tree.column("#1", stretch=YES, width=50)
tree.column("#2", stretch=YES, width=100)
tree.column("#3", stretch=YES, width=75)
tree.column("#4", stretch=YES, width=100)
tree.column("#5", stretch=YES, width=100)


def show():
    tree.delete(*tree.get_children())
    tasks = get_results()
    for idx, task in enumerate(tasks, start=1):
        is_done_str = "✅" if task.status == 2 else "❌"
        tree.insert("", END, values=(str(idx), task.task, is_done_str, task.date_added, task.date_completed))

show()


def click_add_button(text='Введите название'):
    window1 = Window()
    window1.window_add['text'] = 'Введите название'
    window1.window_add.pack()
    window1.confirm_add['command'] = window1.button_clicked
    window1.entr_add = Label(window1, text='Введите дедлайн', bg="#480607", font=40, fg='white', width=100)
    window1.get_data(10)



def add(task: str):
    one_task = Tasks(task)
    insert_task(one_task)



def click_dell_button():
    window1 = Window()
    window1.window_add['text'] = 'Введите номер'
    window1.window_add.pack()
    window1.confirm_add['command'] = window1.button_clicked1
    window1.get_data(10)

def delete(position: int):
    delete_task(position-1)


def click_upd_button():
    window1 = Window()
    window1.window_add['text'] = 'Введите номер и имя'
    window1.window_add.pack()
    window1.confirm_add['command'] = window1.button_clicked2
    window1.get_data(10)

def update(position: str, task: str):
    update_task(int(position)-1, task)


def click_cmp_button():
    window1 = Window()
    window1.window_add['text'] = 'Введите номер'
    window1.window_add.pack()
    window1.confirm_add['command'] = window1.button_clicked3
    window1.get_data(10)

def complete(position: int):
    complete_to_do(position-1)


def create_buttons():
    btn_frame = Frame(root, bg='#480607')
    btn_frame.place(rely=0.6, relheight=0.2, relwidth=1)

    btn_add = Button(btn_frame, text="Add task",bg="black", fg="white", font=40, command=click_add_button)
    btn_add.place(rely=0.2, relx=0.08, relheight=0.7,relwidth=0.2)

    btn_dell = Button(btn_frame, text="Delete",bg="black", fg="white", font=40, command=click_dell_button)
    btn_dell.place(rely=0.2, relx=0.3, relheight=0.7,relwidth=0.2)

    btn_upd = Button(btn_frame, text="Update",bg="black", fg="white", font=40, command=click_upd_button)
    btn_upd.place(rely=0.2,relx=0.52, relheight=0.7,relwidth=0.2)

    btn_cpl = Button(btn_frame, text="Complete",bg="black", fg="white", font=40, command=click_cmp_button)
    btn_cpl.place(rely=0.2,relx=0.74, relheight=0.7,relwidth=0.2)

create_buttons()

root.mainloop()