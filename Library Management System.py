# Library Management System

# Pre-loaded books
books = ["Harry Potter", "The Hobbit", "Atomic Habits"]

while True:
    print("\n==== Library Management System ====")
    print("1. View Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Search Book")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    # View Books
    if choice == "1":
        print("\n---- Available Books ----")
        if not books:
            print("No books in the library.")
        else:
            for book in books:
                print(book)

    # Add Book
    elif choice == "2":
        book_name = input("Enter book name to add: ")
        books.append(book_name)
        print(f"'{book_name}' added successfully!")

    # Remove Book
    elif choice == "3":
        book_name = input("Enter book name to remove: ")
        if book_name in books:
            books.remove(book_name)
            print(f"'{book_name}' removed successfully!")
        else:
            print("Book not found.")

    # Search Book
    elif choice == "4":
        book_name = input("Enter book name to search: ")
        if book_name in books:
            print(f"'{book_name}' is available.")
        else:
            print("Book not found.")

    # Exit
    elif choice == "5":
        print("Exiting program... Goodbye!")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")
