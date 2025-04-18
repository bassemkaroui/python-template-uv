from rich import print as rprint
from typer import Typer

from {{ project_slug }} import __version__

app = typer.Typer()

@app.command(rich_help_panel="Help and Others", help="Show the CLI's version.")
def version() -> None:
    rprint(f"{{ cli_name }} Version: [green]{__version__}[/green]")
