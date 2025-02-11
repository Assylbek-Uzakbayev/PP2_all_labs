def average_category_score(movies, category):
    category_movies = [movie for movie in movies if movie['category'] == category]
    if not category_movies:
        return 0
    return sum(movie['imdb'] for movie in category_movies) / len(category_movies)
