from tkinter import *
from tkinter import ttk
from model import Tasks
from database import insert_task, get_results, delete_task, update_task, complete_to_do

root = Tk()
root['bg'] = 'black'
root.title('MPS - MEXT PREPARATION')
root.wm_attributes('-alpha', 1)
root.geometry('500x450')

canvas = Canvas(root, height=450, width=500, bg= 'black', highlightthickness=0)
canvas.pack()

frame = Frame(root, bg='black')
frame.place(rely=0.1,relwidth=1,relheight=0.5)

title = Label(frame, text='MPS', bg="#480607",font=40, fg='white',  width=350)
title.pack()

tasks = get_results()

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
    for idx,task in enumerate(tasks, start=1):
        is_done_str = "✅" if task.status==2 else "❌"
        tree.insert("",END, values= (str(idx), task.task, is_done_str, task.date_added, task.date_completed))

show()

btn_frame=Frame()

btn = Button(btn_frame)
# def add(task: str):
#     typer.echo(f"adding {task}")
#     one_task = Tasks(task)
#     insert_task(one_task)
#     show()
#
# def delete(position: int):
#     typer.echo(f"deleting {position}")
#     delete_task(position-1)
#     show()
#
# def update(position: int, task: str):
#     typer.echo(f"updating {position}")
#     update_task(position-1, task)
#     show()
#
# def complete(position: int):
#     typer.echo(f"complete {position}")
#     complete_to_do(position-1)
#     show()
#
# def show():
#     tasks = get_results()
#     console.print("[bold red]DEADLINES[/bold red]")
#
#     table = Table(show_header=True, header_style="bold red")
#     table.add_column("#", style="dim", width=6, justify="center")
#     table.add_column("TASKS", min_width = 20, justify="center")
#     table.add_column("PROGRESS", min_width = 12, justify="center")
#     table.add_column("STATING DATE", min_width=25, justify="center")
#     table.add_column("ENDING DATE", min_width=25, justify="center")
#
#     for idx,task in enumerate(tasks, start=1):
#         is_done_str = "✅" if task.status==2 else "❌"
#         table.add_row(str(idx), task.task, is_done_str, task.date_added, task.date_completed)
#     console.print(table)

root.mainloop()