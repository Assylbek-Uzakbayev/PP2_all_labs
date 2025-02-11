def average_imdb_score(movies):
    if not movies:
        return 0
    return sum(movie['imdb'] for movie in movies) / len(movies)
