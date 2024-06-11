# Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be: 
# "Itinerary 1: Alice - From New York to London"
# "Itinerary 2: Bob - From Tokyo to San Francisco"

def flight_itineraries(flights):
    for idx, flight in enumerate(flights, 1):
        print(f'Itinerary {idx}: {flight[0]} - From {flight[1]} to {flight[2]}')

flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

flight_itineraries(flights) 

print("=" * 100)

# You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")] # here are the initial books in the library

# Creating function to add books to the library

def add_book(book, name):
    if (book, name) not in library:
        library.append((book, name))
        print(f'{book} by {name} has been added to the library.')
    else:
        print(f'{book} by {name} is already in the library.')

# Creating function to exit the library system and display the current books in the library

def exit(library):
    print("Thank you for using our library. Here is what we currently have for you: ")
    for idx, book in enumerate(library, 1):
        print(f'{idx}. {book[0]} by {book[1]}')
    
    print("Have a nice day!")

# Creating main function to add books to the library


def main():
    while True:
        title = input('Enter the title of the book: ')
        author = input('Enter the author of the book: ')
        add_book(title, author)
        leave = input('Would you like to add another book? (y/n)')
        if leave.lower() == 'n':
            exit(library)
            break



main()