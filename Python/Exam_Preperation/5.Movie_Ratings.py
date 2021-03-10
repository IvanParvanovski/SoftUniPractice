import sys
lowest_rating = sys.maxsize
lowest_rating_film = ""
highest_rating = -sys.maxsize
highest_rating_film = ""
film_count = int(input())
total_rating = 0
average = 0


for counter in range(film_count):
    film_name = input()
    film_rating = float(input())

    total_rating += film_rating

    if film_rating > highest_rating:
        highest_rating = film_rating
        highest_rating_film = film_name
    if film_rating < lowest_rating:
        lowest_rating = film_rating
        lowest_rating_film = film_name
average = total_rating / film_count

print(f"{highest_rating_film} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_film} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average:.1f}")