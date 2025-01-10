import typer
import json
from documentcloud import DocumentCloud
from documentcloud.exceptions import (
    APIError,
    DuplicateObjectError,
    CredentialsFailedError,
    DoesNotExistError,
    MultipleObjectsReturnedError
)
from pathlib import Path
from rich import print
from rich.table import Table
from typing import Annotated


app = typer.Typer()

@app.command()
# Doesn't show 'INTEGER' in help instead shows '[RESULT_COUNT]' as type instead :/
def search(query: str, result_count: Annotated[int, typer.Argument(min=1, max=25)]=10):
    client = DocumentCloud()
    doc_list = client.documents.search(query).results[:result_count]
    if not doc_list:  # List is empty (no results for query)
        print("[bold red]Your query returned no results!")
    else:
        table = Table(title="[red]Search Results")
        table.add_column("Contributor", justify="center", style="cyan")
        table.add_column("Title", justify="center", style="magenta")
        table.add_column("Creation Date", justify="center", style="green")
        for doc in doc_list:
            table.add_row(f"{doc.contributor}",
                          f"[link={doc.canonical_url}]{doc.title}[/link]",
                          f"{doc.created_at.strftime('%b %d %Y')}")
        print(table)

@app.command()
# Can't handle spaces in file names at the moment.
def upload(file_path: Annotated[Path, typer.Argument(exists=True, file_okay=True, readable=True, resolve_path=True)],
           username: Annotated[str, typer.Option(prompt=True)],
           password: Annotated[str, typer.Option(prompt=True, hide_input=True)]):
    try:
        client = DocumentCloud(username, password)
        client.documents.upload(file_path)
        print(f"Uploaded {file_path} to your DocumentCloud account.")
    except CredentialsFailedError:
        print(f"\n[bold red]CredentialsFailedError: Invalid username and/or password!")
    except APIError as e:
        print(f"\n[bold red]APIError: {json.loads(e.error)['detail']}")

if __name__ == "__main__":
    app()