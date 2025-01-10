import sys
import typer
from datetime import datetime
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


def search(query: str, result_count: int=10):
    client = DocumentCloud()
    doc_list = client.documents.search(query).results[:result_count]
    if not doc_list:  # List is empty (no results for query)
        print("[bold red]Your query returned no results!")
    else:
        table = Table(title="Search Results")
        table.add_column("Contributor", justify="center", style="cyan")
        table.add_column("Title", justify="center", style="magenta")
        table.add_column("Creation Date", justify="center", style="cyan")
        for doc in doc_list:
            table.add_row(f"{doc.contributor}", f"{doc.title}", f"{doc.created_at.strftime('%b %d %Y')}")
        print(table)
            # print(f"{i + 1}: \"{doc.title}\" - {doc.contributor} - {doc.created_at.strftime('%b %d %Y')}")

if __name__ == "__main__":
    typer.run(search("Los Angeles"))