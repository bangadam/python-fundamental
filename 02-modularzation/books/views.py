from books.models import books

def run_views() :
    print("Book Lists")
    print("____________")
    # print(books)
    for data in books:
        print(f'\t {data["title"]}')
        print(f'\t {data["description"]}')
        print(f'\t {data["author"]}')