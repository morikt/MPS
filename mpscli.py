import typer
from  rich.console import Console
from rich.table import Table
from model import  Tasks
from database import insert_task, get_results, delete_task, update_task, complete_to_do

console = Console()

app = typer.Typer()

@app.command(short_help='adds an item')
def add(task: str):
    typer.echo(f"adding {task}")
    one_task = Tasks(task)
    insert_task(one_task)
    show()

@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    delete_task(position-1)
    show()

@app.command()
def update(position: int, task: str):
    typer.echo(f"updating {position}")
    update_task(position-1, task)
    show()

@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    complete_to_do(position-1)
    show()

@app.command()
def show():
    tasks = get_results()
    console.print("[bold red]DEADLINES[/bold red]")

    table = Table(show_header=True, header_style="bold red")
    table.add_column("#", style="dim", width=6, justify="center")
    table.add_column("TASKS", min_width = 20, justify="center")
    table.add_column("PROGRESS", min_width = 12, justify="center")
    table.add_column("STATING DATE", min_width=25, justify="center")
    table.add_column("ENDING DATE", min_width=25, justify="center")

    for idx,task in enumerate(tasks, start=1):
        is_done_str = "✅" if task.status==2 else "❌"
        table.add_row(str(idx), task.task, is_done_str, task.date_added, task.date_completed)
    console.print(table)

if __name__ == "__main__":
    app()