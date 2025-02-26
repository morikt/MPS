import datetime


class Tasks():
    def __init__(self,task,
                 date_added=None, date_completed=None,
                 status=None, position="None"):
        self.task = task
        self.date_added = date_added if date_added is not None else datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.date_completed = date_completed if date_completed is not None else None
        self.status = status if status is not None else 1 #1-open 2-closed
        self.position =  position if position is not None else None

    def __repr__(self) -> str:
        return f"{self.task}, {self.date_added}, {self.date_completed}, {self.status}. {self.position}"

