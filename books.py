from fastapi import Body, FastAPI


app = FastAPI()

BOOKS = [
    {
        "title": "The Beautyful Ones are Not Yet Born",
        "author": "Ayi Kwei Armah",
        "category": "Fiction",
    },
    {"title": "Things Fall Apart", "author": "Chinua Achebe", "category": "Fiction"},
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "category": "Fantasy",
    },
    {"title": "The Godfather", "author": "Mario Puzo", "category": "Crime Fiction"},
    {
        "title": "Once Bitten, Twice Shy",
        "author": "Jennifer Rardin",
        "category": "Fantasy",
    },
    {
        "title": "Changes: A Love Story",
        "author": "Ama Ata Aidoo",
        "category": "Fiction",
    },
    {
        "title": "Tail of the Blue Bird",
        "author": "Nii Ayikwei Parkes",
        "category": "Fiction",
    },
    {"title": "Ghana Must Go", "author": "Taiye Selasi", "category": "Fiction"},
    {
        "title": "Two Thousand Seasons",
        "author": "Ayi Kwei Armah",
        "category": "Fiction",
    },
    {
        "title": "The Gods Are Not to Blame",
        "author": "Ola Rotimi",
        "category": "Fiction",
    },
    {"title": "Anowa", "author": "Ama Ata Aidoo", "category": "Fiction"},
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "Fiction",
    },
    {"title": "The Da Vinci Code", "author": "Dan Brown", "category": "Thriller"},
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "category": "Fiction",
    },
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy"},
    {"title": "1984", "author": "George Orwell", "category": "Dystopian Fiction"},
    {
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "category": "Children's Literature",
    },
    {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Fantasy"},
    {"title": "Purpose Driven Life", "author": "Rick Warren", "category": "Religious"},
    {"title": "The Bible", "author": "God", "category": "Religious"},
    {"title": "The Torah", "author": "God", "category": "Religious"},
    {"title": "The Ten Commandments", "author": "God", "category": "Religious"},
    {"title": "The Quran", "author": "Allah", "category": "Religious"},
    {"title": "The Bhagavad Gita", "author": "Krishna", "category": "Religious"},
    {"title": "The Tripitaka", "author": "Buddha", "category": "Religious"},
    {"title": "The Guru Granth Sahib", "author": "Guru Nanak", "category": "Religious"},
    {
        "title": "The Count of Monte Cristo",
        "author": "Alexandre Dumas",
        "category": "Adventure",
    },
    {"title": "The Blacklist", "author": "Sara Paretsky", "category": "Mystery"},
    {
        "title": "Malcolm X: A Life of Reinvention",
        "author": "Manning Marable",
        "category": "Biography",
    },
    {
        "title": "The Autobiography of Malcolm X",
        "author": "Malcolm X",
        "category": "Biography",
    },
    {
        "title": "The Autobiography of Benjamin Franklin",
        "author": "Benjamin Franklin",
        "category": "Biography",
    },
    {
        "title": "Tupac Shakur: The Life and Times of an American Icon",
        "author": "Tayannah Lee McQuillar",
        "category": "Biography",
    },
    {
        "title": "Bob Marley: The Untold Story",
        "author": "Chris Salewicz",
        "category": "Biography",
    },
    {
        "title": "Kwame Nkrumah: The Father of African Nationalism",
        "author": "David Birmingham",
        "category": "Biography",
    },
]


@app.get("/books")
async def read_all_books():
    return BOOKS


"""
Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
# """


# @app.get("/books/author/{author}")
@app.get("/books/author/")
async def read_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book: dict = Body()):
    BOOKS.append(new_book)
    return new_book


@app.put("/books/update_book")
async def update_book(updates_book: dict = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updates_book.get("title").casefold():
            BOOKS[i] = updates_book
            return BOOKS[i]


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
        return {"message": f"Book '{book_title}' deleted successfully."}


"""
Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
"""
