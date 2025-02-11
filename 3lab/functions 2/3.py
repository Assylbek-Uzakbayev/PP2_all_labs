def movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]