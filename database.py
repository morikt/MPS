import sqlite3
import datetime
from model import Tasks
from typing import List



conn = sqlite3.connect('TASKS.db')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS TASKS(
    task text,
    date_added text,
    date_completed text,
    status integer,
    position integer)""")

create_table()

def insert_task(task: Tasks):
    c.execute('select count(*) FROM TASKS')
    count = c.fetchone()[0]
    task.position = count if count else 0
    with conn:
        c.execute('INSERT INTO TASKS VALUES (:task, :date_added, :date_completed, :status, :position)',
                  {'task': task.task, 'date_added': task.date_added, 'date_completed': task.date_completed,
                   'status': task.status, 'position': task.position})


def get_results() -> List[Tasks]:
    c.execute('SELECT * FROM TASKS')
    results = c.fetchall()
    tasks = []
    for result in results:
        tasks.append(Tasks(*result))
    return tasks


def delete_task(position):
    c.execute('SELECT COUNT(*) FROM TASKS')
    count = c.fetchone()[0]

    with conn:
        c.execute(f'DELETE FROM TASKS WHERE position=:position', {'position': position})
        for pos in range(position+1, count):
            change_position(pos,pos-1,False)


def change_position(old_p: int,new_p: int, commit = True):
    c.execute('UPDATE TASKS SET position=:position_new WHERE position=:position_old', {
        'position_new': new_p,'position_old': old_p
    })
    if commit:
        conn.commit()


def update_task(position: int, task: str):
    with conn:
        if task is not None:
            c.execute('UPDATE TASKS SET task=:task WHERE position=:position', {'position': position,
                                                                               'task':task
                                                                               })

def complete_to_do(position: int):
    with conn:
        c.execute('UPDATE TASKS SET status = 2, date_completed=:date_completed WHERE position=:position',
                  {'date_completed': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),'position': position})

