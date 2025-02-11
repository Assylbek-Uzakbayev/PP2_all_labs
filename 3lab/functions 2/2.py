def high_score_movies(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]
