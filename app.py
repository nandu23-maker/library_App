class Library:
    
    book_count = 0
    book_list = {}
    
    def __init__(self, bid, bname):
        self.bid = bid
        self.bname = bname

class Books(Library):
    
    def __init__(self, bid, bname, author):
        super().__init__(bid, bname)
        self.author = author
        self.availibility = True
        self.return_status = False
        
        Library.book_list.update({bname: bid})
        print(f"New book '{bname}' by {author} is added")
        Library.book_count += 1
    
    def checkout(self):
        if self.availibility:
            print(f"Book '{self.bname}' with ID {self.bid} is checked out")
            self.availibility = False
            Library.book_count -= 1
        else:
            print(f"Book '{self.bname}' is not available for checkout")
            
    def return_book(self):
        if not self.availibility:
            print(f"Book '{self.bname}' with ID {self.bid} is returned")
            self.availibility = True
            Library.book_count += 1
        else:
            print(f"Book '{self.bname}' was not issued to anyone")
        
    def book_info(self):
        status = "Available" if self.availibility else "Checked out"
        print(f"Book information:\n Book Name: {self.bname}\n Book ID: {self.bid}\n Author: {self.author}\n Status: {status}")

    @staticmethod
    def display_book_list():
        if not Library.book_list:
            print("No books in the library")
        else:
            print("Books in the library:")
            for book_name, book_id in Library.book_list.items():
                print(f"ID: {book_id}, Name: {book_name}")

def main():
    books = []
    
    while True:
        print("\nLibrary Menu:")
        print("1. Add a new book")
        print("2. Checkout a book")
        print("3. Return a book")
        print("4. Display book information")
        print("5. Display all books in the library")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            bid = int(input("Enter book ID: "))
            bname = input("Enter book name: ")
            author = input("Enter author name: ")
            new_book = Books(bid, bname, author)
            books.append(new_book)
            
        elif choice == '2':
            bname = input("Enter the book name to checkout: ")
            for book in books:
                if book.bname == bname:
                    book.checkout()
                    break
            else:
                print(f"No book found with the name '{bname}'")
                
        elif choice == '3':
            bname = input("Enter the book name to return: ")
            for book in books:
                if book.bname == bname:
                    book.return_book()
                    break
            else:
                print(f"No book found with the name '{bname}'")
                
        elif choice == '4':
            bname = input("Enter the book name to display information: ")
            for book in books:
                if book.bname == bname:
                    book.book_info()
                    break
            else:
                print(f"No book found with the name '{bname}'")
                
        elif choice == '5':
            Books.display_book_list()
            print(f"\nTotal books in the library: {Library.book_count}")
            
        elif choice == '6':
            print("Exiting the library system.")
            break
            
        else:
            print("Invalid choice, please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
