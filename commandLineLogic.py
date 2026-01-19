import typer

app = typer.Typer(no_args_is_help=True, add_completion=False, rich_markup_mode="markdown", pretty_exceptions_enable=False)

def initCLI():
    app()

@app.command()
def idk():
    print("Logic will be here at some point")
