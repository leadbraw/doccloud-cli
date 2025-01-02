import sys
from datetime import datetime
from documentcloud import DocumentCloud

def execute_search():
    asking_limit = True
    while asking_limit:
        try:
            limit = int(input("Enter the maximum amount of search results displayed (up to 25): "))
            if 1 <= limit <= 25:
                asking_limit = False
        except ValueError:
            pass
    query = input("Type your search query: ").strip()
    doc_list = client.documents.search(query).results[:limit]
    for i, doc in enumerate(doc_list):
        print(f"{i + 1}: \"{doc.title}\" - {doc.contributor} - {doc.created_at.strftime('%b %d %Y')}")
    execute_inspect(doc_list, limit)

def execute_inspect(doc_list, result_limit):
    try:
        selection_choice = int(input("Enter the number of the document you want to "
                                     f"inspect (1-{result_limit}) Anything else to exit: "))
    except ValueError:
        sys.exit()
    if 1 <= selection_choice <= 10:
        doc = doc_list[selection_choice - 1]
        print(f"{'Metadata fields':_^35}")
        metadata_fields = ["id", "access", "canonical_url", "created_at", "title", "page_count"]
        for field in metadata_fields:
            attribute = getattr(doc, field)
            if isinstance(attribute, datetime): # need to handle converting datetime object to string.
                attribute = attribute.strftime('%b %d %Y')
            print(f"{field:.<30}{attribute}")

def execute_upload():
    pass

# --initial setup--
username_result = input("Please provide your DocumentCloud username, type 'G' to remain a guest: ")
if username_result == 'G':
    client = DocumentCloud()
else:
    password_result = input("Please provide your DocumentCloud password: ").strip()
    client = DocumentCloud(username_result, password_result)

loop = True
while loop:
    asking_action = True
    while asking_action:
        try:
            action_choice = int(input("What would you like to do? Exit (0), Search (1), Upload (2): "))
            if action_choice == 1:
                execute_search()
            elif action_choice == 2:
                execute_upload()
            elif action_choice == 0:
                sys.exit()
            else:
                pass
        except ValueError:
            pass