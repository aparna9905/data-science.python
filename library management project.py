
import re


# ---------------- BOOK CLASS ---------------- #
class Book:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f"{self.book_id},{self.title},{self.author},{self.status}"


# ---------------- LIBRARY CLASS ---------------- #
class Library:
    def __init__(self, filename="library.txt"):
        self.filename = filename

    # -------- ADD BOOK -------- #
    def add_book(self):
        try:
            book_id = input("Enter Book ID (Format: B001): ")

            # REGEX validation (B followed by 3 digits)
            if not re.match(r"^B\d{3}$", book_id):
                raise ValueError("Invalid Book ID format! Use B followed by 3 digits (Example: B101)")

            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            # Check duplicate ID
            with open(self.filename, "a+") as file:
                file.seek(0)
                for line in file:
                    if book_id in line:
                        raise Exception("Book ID already exists!")

                book = Book(book_id, title, author)
                file.write(str(book) + "\n")

            print("Book added successfully!")

        except Exception as e:
            print("Error:", e)

    # -------- VIEW BOOKS -------- #
    def view_books(self):
        try:
            with open(self.filename, "r") as file:
                data = file.readlines()

                if not data:
                    print("No books available.")
                    return

                for line in data:
                    book_id, title, author, status = line.strip().split(",")
                    print(f"\nID: {book_id}")
                    print(f"Title: {title}")
                    print(f"Author: {author}")
                    print(f"Status: {status}")

        except FileNotFoundError:
            print("No records found. File does not exist yet.")
        except Exception as e:
            print("Error:", e)

    # -------- SEARCH BOOK -------- #
    def search_book(self):
        try:
            search_title = input("Enter title to search: ").lower()
            found = False

            with open(self.filename, "r") as file:
                for line in file:
                    book_id, title, author, status = line.strip().split(",")

                    if search_title in title.lower():
                        print(f"\nID: {book_id}")
                        print(f"Title: {title}")
                        print(f"Author: {author}")
                        print(f"Status: {status}")
                        found = True

            if not found:
                print("Book not found.")

        except Exception as e:
            print("Error:", e)

    # -------- ISSUE BOOK -------- #
    def issue_book(self):
        try:
            book_id_input = input("Enter Book ID to issue: ")
            updated_lines = []
            found = False

            with open(self.filename, "r") as file:
                for line in file:
                    book_id, title, author, status = line.strip().split(",")

                    if book_id == book_id_input:
                        found = True
                        if status == "Available":
                            status = "Issued"
                            print("Book issued successfully!")
                        else:
                            raise Exception("Book already issued.")

                    updated_lines.append(f"{book_id},{title},{author},{status}\n")

            if not found:
                print("Book ID not found.")
                return

            with open(self.filename, "w") as file:
                file.writelines(updated_lines)

        except Exception as e:
            print("Error:", e)

    # -------- RETURN BOOK -------- #
    def return_book(self):
        try:
            book_id_input = input("Enter Book ID to return: ")
            updated_lines = []
            found = False

            with open(self.filename, "r") as file:
                for line in file:
                    book_id, title, author, status = line.strip().split(",")

                    if book_id == book_id_input:
                        found = True
                        if status == "Issued":
                            status = "Available"
                            print("Book returned successfully!")
                        else:
                            raise Exception("Book was not issued.")

                    updated_lines.append(f"{book_id},{title},{author},{status}\n")

            if not found:
                print("Book ID not found.")
                return

            with open(self.filename, "w") as file:
                file.writelines(updated_lines)

        except Exception as e:
            print("Error:", e)


# ---------------- MAIN PROGRAM ---------------- #

def main():
    library = Library()

    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.issue_book()
        elif choice == "5":
            library.return_book()
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice!")



main()





# In[ ]:




