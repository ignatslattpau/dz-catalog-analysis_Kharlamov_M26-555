movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

'''Этап 1. Разминка: переменные, числа, math'''
from math import ceil


def average_rating(movies):
    """Возвращает среднюю оценку по каталогу, округленную до одного знака"""

    sum_ratings = sum([film["rating"] for film in movies])
    len_ratings = len(movies)

    return round(sum_ratings / len_ratings, 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее) по возрасту фильмов"""

    films_ages = [current_year - film["year"] for film in movies]

    return max(films_ages), min(films_ages), ceil(sum(films_ages) / len(films_ages))


def duration_in_hours(minutes):
    """Переводит минуты в формат "2ч 35м"""

    return f'{minutes // 60}ч {minutes % 60}м'

# Проверки работы функций
# print(average_rating(movies))
# print(catalog_age_stats(movies))
# print(duration_in_hours(301))

'''Этап 2. Условия и match'''
def rating_tier(rating):
    """Возвращает категорию фильма по его оценке"""

    if rating >= 9:
        return 'шедевр'
    elif rating >= 7:
        return 'хорошо'
    else:
        return 'слабо' if rating < 5 else 'средне'


def decade_label(year):
    """Возвращает метку возраста фильма"""
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if year < 2015:
            return 'старые'
        case _:
            return 'недавние'

# Проверки работы функций
# print(rating_tier(9.2))
# print(decade_label(2014))

'''Этап 3. Циклы'''
for film in movies:
    if 'comedy' in film["genres"]:
        continue
    print(film["title"])

i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(movies[i]["title"])
        break
    i += 1
else:
    print('Шедевров не найдено')


def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее заданного количества минут"""
    res_count = 0

    for film in movies:
        if film["duration_min"] > threshold:
            res_count += 1

    return res_count

# print(count_long_movies(movies))

'''Этап 4. Строки'''
def normalize_title(title):
    """Которая приводит строку к формату Title Case (каждое слово с заглавной буквы)"""
    words = title.split(' ')
    title_words = [word[0].upper() + word[1:] for word in words]

    return ' '.join(title_words)


def make_slug(title):
    """Превращает нормализованное название в «слаг»"""
    return title.lower().replace(' ', '-')


def format_report_line(movie):
    """Возвращает строку с описанием фильма"""
    return (f'"{normalize_title(movie["title"])}" ({movie["year"]}) - {movie["rating"]}/10, '
            f'{duration_in_hours(movie["duration_min"])}, жанры: {', '.join(sorted(list(movie["genres"])))}')


# Проверки работы функций
# print(normalize_title("silent hours"))
# print(make_slug("Silent Hours"))
# print(format_report_line(movies[7]))

'''Этап 5. Списки'''
def sorted_movies_info_by_rating(movies):
    """
    Вспомогательная функция (не по заданию), сортирует список с полной информацией по фильмам,
    переиспользуется в функциях по заданию
    """
    return sorted(movies, key=lambda x: x["rating"], reverse=True)


def titles_sorted_by_rating(movies):
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга"""
    return [film["title"] for film in sorted_movies_info_by_rating(movies)]


def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) — топ по рейтингу"""
    sorted_movies = sorted_movies_info_by_rating(movies)

    return [(sorted_movies[i]["title"], sorted_movies[i]["rating"]) for i in range(n)]

# Проверки работы функций
# print(titles_sorted_by_rating(movies))
# print(top_n_by_rating(movies, 3))

'''Этап 6. Словари'''
def count_by_genre(movies):
    """Возвращает словарь с количеством фильмов каждого жанра"""
    genres_count = {}

    for film in movies:
        for genre in film["genres"]:
            genres_count[genre] = genres_count.get(genre, 0) + 1

    return genres_count


def actor_filmography(movies):
    """Словарь со списком фильмов каждого актера"""
    actors_films = {}

    for film in movies:
        for actor in film["actors"]:
            films = actors_films.get(actor, [])
            films.append(film["title"])
            actors_films[actor] = films

    return actors_films

# ловарь для фильмов с рейтингом выше среднего
titles_ratings = {film["title"]: film["rating"] for film in movies if film["rating"] > average_rating(movies)}

# Проверки работы функций
# print(titles_ratings)
# print(actor_filmography(movies))
# print(count_by_genre(movies))

'''Этап 7. Множества'''
def all_genres(movies):
    """Возвращает множество уникальных жанров каталога"""
    result = set()

    for film in movies:
        result.update(film["genres"])

    return result


def common_actors(movie1, movie2):
    """Возвращает множество актеров, снимавшихся в обоих фильмах"""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры встречающиеся в первой группе фильмов, но не встречающихся во второй группе фильмов"""
    genres_a = set()
    genres_b = set()

    for film in movies_a:
        genres_a.update(film["genres"])
    for film in movies_b:
        genres_b.update(film["genres"])

    return genres_a - genres_b

# Проверки работы функций
# print(all_genres(movies))
# print(common_actors(movies[0], movies[3]))       # {"O. Isaac"}
# print(genres_only_in_one(movies[5:6], movies[:5]))  # {"mystery"}

'''Этап 8. Итераторы и генераторы'''
def iter_high_rated(movies, min_rating=8.0):
    """Генератор информации по фильмам, с рейтингом не ниже мнинмального"""
    for film in movies:
        if film["rating"] >= min_rating:
            yield film


sum_duration_good_films = sum(m["duration_min"] for m in movies if m["rating"] > 7)

# for movie in iter_high_rated(movies):
#     print(format_report_line(movie))
# # "The Dune Chronicles" (2021) — 8.6/10, 2ч 35м, жанры: drama, sci-fi
# # "Midnight In Oslo" (2020) — 8.9/10, 2ч 4м, жанры: mystery, thriller
# # "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi
#
# print(sum_duration_good_films)  # 713