# CBMM 2013 - Assignment 1
# Movie Collection Manager (Starter Template)
# Lecturer: Mohd Faiz bin Alias

movies = []

# Example movie structure:
# {"title": "Movie Name", "genre": "Genre", "rating": "8"}

def show_menu():
    print("\nMovie Collection Manager")
    print("1. Add movie")
    print("2. View movies")
    print("3. Search movie")
    print("4. Exit")

def add_movie():
    # Ask user for title, genre and rating
    title = input("Enter movie title: ")
    genre = input("Enter genre: ")
    rating = input("Enter rating: ")
    
    # It stores the data in your list
    movies.append({"title": title, "genre": genre, "rating": rating})
    print("Movie added successfully!")

def view_movies():
    # FIXED LOGICAL ERROR: movies is a list [], not an empty string "" 
    if not movies:
        print("No movies available")
   
else:
        #Loop and display the movies
        print("\n--- Current Movie Collection ---")
        for movie in movies:
            print(f"Title: {movie['title']} | Genre: {movie['genre']} | Rating: {movie['rating']}")




def search_movie():
    # TODO: ask user for movie title
    # TODO: search movie in the list
    # TODO: display result
    pass


def main():
    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            add_movie()

        elif choice == "2":
            view_movies()

        elif choice == "3":
            search_movie()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


main()
