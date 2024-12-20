from documentcloud import DocumentCloud
username_result = input("Please provide your DocumentCloud username, type 'N' to remain a guest: ")
if username_result == 'N':
    client = DocumentCloud()
else:
    password_result = input("Please provide your DocumentCloud password: ").strip()
    client = DocumentCloud(username_result, password_result)

loop = True
while loop:
    query = input("Type your search query: ").strip()
    doc_list = client.documents.search(query)
    for i, doc in enumerate(doc_list):
        print(f"{i+1}: \"{doc.title}\" - {doc.contributor} - {doc.created_at}")

        if i == 25: break # Only show first 25 results.
    choice = input("Search again? (Y/N) ")
    if choice == 'N':
        loop = False