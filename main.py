from typing import Optional, Annotated

import typer
from documentcloud import DocumentCloud
from documentcloud.exceptions import (
    APIError,
    DuplicateObjectError,
    CredentialsFailedError,
    DoesNotExistError,
    MultipleObjectsReturnedError
)
from rich import print
from rich.table import Table

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

if __name__ == "__main__":
    app()