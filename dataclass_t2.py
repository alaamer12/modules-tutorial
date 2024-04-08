from dataclasses import dataclass, field, fields, asdict, astuple, make_dataclass  # Import necessary functions and classes from the dataclasses module
import random  # Import the random module for generating random ages

# Define a simple dataclass for representing a person
@dataclass
class Person:
    name: str  # Define a field for the person's name
    age: int  # Define a field for the person's age
    email: str  # Define a field for the person's email address

# Define a dataclass for representing a book, with default values and field metadata
@dataclass
class Book:
    title: str  # Define a field for the book's title
    author: str = "Unknown"  # Define a field for the book's author, with a default value of "Unknown"
    pages: int = field(default=0, metadata={"description": "Total number of pages"})  # Define a field for the total number of pages, with a default value of 0 and metadata describing the field

# Define a dataclass for representing a user, with a default factory function for the age field
def random_age():  # Define a function for generating a random age
    return random.randint(20, 60)  # Return a random integer between 20 and 60

@dataclass
class User:
    name: str  # Define a field for the user's name
    age: int = field(default_factory=random_age)  # Define a field for the user's age, with a default factory function to generate a random age

# Define a dataclass for representing a student, inheriting from the Person dataclass
@dataclass
class Student(Person):
    student_id: int  # Define a field for the student's ID

def main():  # Define the main function
    # Create instances of the dataclasses
    person = Person(name="Alice", age=30, email="alice@example.com")  # Create a Person instance
    book = Book(title="Python Programming", pages=300)  # Create a Book instance
    user = User(name="Bob")  # Create a User instance

    # Print the fields and values of the dataclass instances
    print("Fields and values of Person:", asdict(person))  # Convert the Person instance to a dictionary and print it
    print("Fields and values of Book:", asdict(book))  # Convert the Book instance to a dictionary and print it
    print("Fields and values of User:", asdict(user))  # Convert the User instance to a dictionary and print it

    # Convert a dataclass instance to a tuple
    print("Person as tuple:", astuple(person))  # Convert the Person instance to a tuple and print it

    # Get the fields of a dataclass
    print("Fields of Person:", [field.name for field in fields(Person)])  # Get the names of the fields in the Person dataclass and print them

    # Create a new dataclass dynamically
    Movie = make_dataclass("Movie", [("title", str), ("director", str)])  # Dynamically create a new dataclass for representing a movie with the specified fields
    movie = Movie(title="Inception", director="Christopher Nolan")  # Create an instance of the dynamic Movie dataclass
    print("Dynamic dataclass Movie:", movie)  # Print the Movie instance

if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Call the main function if the script is being run directly
