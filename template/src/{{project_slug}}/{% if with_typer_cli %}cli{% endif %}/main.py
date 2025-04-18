from typing import Annotated

from rich import print as rprint
from typer import Typer

from {{ project_slug }} import __version__
from {{ project_slug }}.cli.commands import version

app = typer.Typer(
    help="{{ package_name }} CLI.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    # epilog="Made with [red]:heart:[/red] by [bold]Bassem Karoui[/bold]",
    # pretty_exceptions_show_locals=False,
)


@app.callback(invoke_without_command=True)
def callback(
    version: Annotated[bool, typer.Option("--version", help="Show the CLI's version.")] = False,
) -> None:
    if version:
        rprint(f"{{ cli_name }} Version: [green]{__version__}[/green]")
        raise typer.Exit()


app.add_typer(version.app, help="Show the CLI's version.")
