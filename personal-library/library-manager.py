import json  #to save or load the json file data
import os #systemoperations and file handling

data_file = 'library.txt'

def load_lilrary():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return [] 

def save_lilrary(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == 'yes'

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(new_book)
    save_lilrary(library)
    print(f"Book '{title}' added to the library.")   #f string ka mtlb hai k hum k idr hum string , variable int erpolation kar sakty hain     

def remove_book(library):
        title = input("Enter the title of the book to remove: ")
        initial_length = len(library)
        library[:] = [book for book in library if book['title'].lower() != title] 
        if len(library) < initial_length:
            save_lilrary(library)
            print(f"Book '{title}' removed from the library.")
        else:
            print(f"Book '{title}' not found in the library.")

def sreach_library(library):
    search_by  = input("Search by (title/author/genre): ").lower()
    search_term = input("Enter the {search_by} ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]
    if results:
        print(f"Books found matching '{search_term}':")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
    else:
        print(f"No books found matching '{search_term}'.")


def display_all_books(library):
    if library:
        print("Books in the library:")
        for book in library:
            print(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("No books in the library.")


def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
   
    print(f"Total books: {total_books}")
    print(f"Percentage of books read: {percentage_read:.2f}%")

def main():
    library = load_lilrary()
    while True:
        print("Welcome to the Library Manager!📚")
        print("Menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library) 
        elif choice == '3':
            sreach_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()            

   