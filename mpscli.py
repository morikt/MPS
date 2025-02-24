import typer
from  rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()

@app.command(short_help='adds an item')
def add(task: str):
    typer.echo(f"adding {task}")
    show()

@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    show()

@app.command()
def update(position: int, task: str = None):
    typer.echo(f"updating {position}")
    show()

@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    show()

@app.command()
def show():
    tasks = ["MEXT","UNIVERSITY"]
    console.print("[bold red]DEADLINES[/bold red]")

    table = Table(show_header=True, header_style="bold red")
    table.add_column("#", style="dim", width=6)
    table.add_column("TASKS", min_width = 20)
    table.add_column("PROGRESS", min_width = 12, justify="right")

    for idx,task in enumerate(tasks, start=1):
        is_done_str = "✅" if True==0 else "❌"
        table.add_row(str(idx), task, is_done_str)
    console.print(table)

if __name__ == "__main__":
    app()