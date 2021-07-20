"""CSC108 A3 recommender starter code."""

from typing import TextIO, List, Dict

from recommender_constants import (MovieDict, Rating, UserRatingDict, 
                                   MovieUserDict)
from recommender_constants import (MOVIE_FILE_STR, RATING_FILE_STR,
                                   MOVIE_DICT_SMALL, USER_RATING_DICT_SMALL,
                                   MOVIE_USER_DICT_SMALL)

############## HELPER FUNCTIONS

def get_similarity(user1: Rating, user2: Rating) -> float:
    """Return the a similarity score between user1 and user2 based on their
    movie ratings. The returned similarity score is a number between 0 and 1
    inclusive. The higher the number, the more similar user1 and user2 are.

    For those who are curious, this type of similarity measure is called the
    "cosine similarity".

    >>> r1 = {1: 4.5, 2: 3.0, 3: 1.0}
    >>> r2 = {2: 4.5, 3: 3.5, 4: 1.5, 5: 5.0}
    >>> s1 = get_similarity(r1, r1)
    >>> abs(s1 - 1.0) < 0.0001 # s1 is close to 1.0
    True
    >>> s2 = get_similarity(r1, {6: 4.5})
    >>> abs(s2 - 0.0) < 0.0001 # s2 is close to 0.0
    True
    >>> round(get_similarity(r1, r2), 2)
    0.16
    """
    shared = 0.0
    for m_id in user1:
        if m_id in user2:
            shared += user1[m_id] * user2[m_id]
    norm1 = 0.0
    for m_id in user1:
        norm1 = norm1 + user1[m_id] ** 2
    norm2 = 0.0
    for m_id in user2:
        norm2 = norm2 + user2[m_id] ** 2
    return (shared * shared) / (norm1 * norm2)


############## STUDENT CONSTANTS

# write constants here


############## STUDENT HELPER FUNCTIONS

# write helper functions here

############## STUDENT FUNCTIONS

def read_movies(movie_file: TextIO) -> MovieDict:
    """Return a dictionary containing movie id to (movie name, movie genres)
    in the movie_file.

    >>> movfile = open('movies_tiny.csv')
    >>> movies = read_movies(movfile)
    >>> movfile.close()
    >>> 68735 in movies
    True
    >>> movies[124057]
    ('Kids of the Round Table', [])
    >>> len(movies)
    4
    >>> movies == MOVIE_DICT_SMALL
    True
    """

    # Your code here

    movies = {}
    for r in movie_file.readlines()[1:]:
        x = r.strip('\n').split(',')
        movies[int(x[0])] = (x[1], x[4:])
    return movies


def read_ratings(rating_file: TextIO) -> UserRatingDict:
    """Return a dictionary containing user id to {movie id: ratings} for the
    collection of user movie ratings in rating_file.

    >>> rating_file = open('ratings_tiny.csv')
    >>> ratings = read_ratings(rating_file)
    >>> rating_file.close()
    >>> len(ratings)
    2
    >>> ratings[1]
    {2968: 1.0, 3671: 3.0}
    >>> ratings[2]
    {10: 4.0, 17: 5.0}
    """

    # Your code here

    #遍历读取到的文件到列表x
    #如果x[0]不在ratings.keys()中，则把x[0]加入ratings中作为key，还有rates作为ratings的value，
        #其中rates字典中的key是ratings字典中的key对应的x[1]，value为x[2]
    #如果x[0]在ratings.keys()中，则只需要在ratings中的value（即rates）的value中加上x[2]
    
    ratings = {}
    for r in rating_file.readlines()[1:]:
        x = r.strip('\n').split(',')
        if int(x[0]) not in ratings.keys():
            ratings[int(x[0])] = {}

        ratings[int(x[0])][int(x[1])] = float(x[2])
        
    return ratings


def remove_unknown_movies(user_ratings: UserRatingDict, 
                          movies: MovieDict) -> None:
    """Modify the user_ratings dictionary so that only movie ids that are in the
    movies dictionary is remaining. Remove any users in user_ratings that have
    no movies rated.

    >>> small_ratings = {1001: {68735: 5.0, 302156: 3.5, 10: 4.5}, 1002: {11: 3.0}, 1003: {}}
    >>> remove_unknown_movies(small_ratings, MOVIE_DICT_SMALL)
    >>> len(small_ratings)
    1
    >>> small_ratings[1001]
    {68735: 5.0, 302156: 3.5}
    >>> 1002 in small_ratings
    False
    """

    # Your code here

    #先把movies字典中的key值取到于列表
    #再把user_ratings字典中的value中的key取到
    #遍历列表，判断user_ratings字典中的value中的key是否在列表中
    #如果不在列表中，则将值移除该用户user_id;否则保留

    s = []
    for k, v in user_ratings.items():
        for k1, v1 in v.items():
            if k1 not in movies.keys():
                s.append((k, k1))
    for x, y in s:
        user_ratings[x].pop(y)
        if (user_ratings[x] == {}):
            user_ratings.pop(x)

    s1 = []
    for k2, v2 in user_ratings.items():
        if v2 == {}:
            s1.append(k2)
    for i in s1:
        user_ratings.pop(i)

def movies_to_users(user_ratings: UserRatingDict) -> MovieUserDict:
    """Return a dictionary of movie ids to list of users who rated the movie,
    using information from the user_ratings dictionary of users to movie
    ratings dictionaries.

    >>> result = movies_to_users(USER_RATING_DICT_SMALL)
    >>> result == MOVIE_USER_DICT_SMALL
    True
    """

    # Your code here

    #新建一个字典d={}
    #在user_ratings字典中取到对应的key
    #在user_ratings字典中取到value字典中的key，比较key有没有相等的
    #有相等的，则作为d的key，在user_ratings字典中取到对应的每一个key作为d的value

    movie_users = {}
    for k, v in user_ratings.items():
        for k1, v1 in v.items():
            if k1 not in movie_users:
                movie_users[k1] = [k]
            else:
                movie_users[k1].append(k)
    return movie_users


def get_users_who_watched(movie_ids: List[int],
                          movie_users: MovieUserDict) -> List[int]:
    """Return the list of user ids in moive_users who watched at least one
    movie in moive_ids.

    >>> get_users_who_watched([68735, 302156], MOVIE_USER_DICT_SMALL)
    [1, 2]
    >>> lst = get_users_who_watched([68735, 302156], MOVIE_USER_DICT_SMALL)
    >>> len(lst)
    2
    """

    # Your code here

    # 遍历movie_ids列表取到每一部电影的id，id作为movie_users字典中的key
    # 通过key获取到对应的value，判断value中的值至少一个，返回该value列表

    s = []
    for mid in movie_ids:
        s += movie_users[mid]
    s1 = []
    for x in s:
        if x not in s1:
            s1.append(x)
    return s1


def get_similar_users(target_rating: Rating,
                      user_ratings: UserRatingDict,
                      movie_users: MovieUserDict) -> Dict[int, float]:
    """Return a dictionary of similar user ids to similarity scores between the
    similar user's movie rating in user_ratings dictionary and the
    target_rating. Only return similarites for similar users who has at least
    one rating in movie_users dictionary that appears in target_Ratings.

    >>> sim = get_similar_users({293660: 4.5}, USER_RATING_DICT_SMALL, MOVIE_USER_DICT_SMALL)
    >>> len(sim)
    1
    >>> round(sim[2], 2)
    0.86
    """

    # Your code here

    # 根据target_rating字典中的key拿到电影id
    # movie_users字典中的value中的用户id
    # user_ratings字典中的value那个字典
    # 需要用到get_smilarity函数计算用户相似度

    d = {}
    similar_users = get_users_who_watched(target_rating.keys(), movie_users)
    for uid in similar_users:
        ratings = user_ratings[uid]
        x = get_similarity(target_rating, ratings)
        d[uid] = x
    return d

    
def recommend_movies(target_rating: Rating,
                     movies: MovieDict, 
                     user_ratings: UserRatingDict,
                     movie_users: MovieUserDict,
                     num_movies: int) -> List[int]:
    """Return a list of num_movies movie id recommendations for a target user 
    with target_rating of previous movies. The recommendations come from movies
    dictionary, and are based on movies that "similar users" data in
    user_ratings / movie_users dictionaries.

    >>> recommend_movies({302156: 4.5}, MOVIE_DICT_SMALL, USER_RATING_DICT_SMALL, MOVIE_USER_DICT_SMALL, 2)
    [68735]
    >>> recommend_movies({68735: 4.5}, MOVIE_DICT_SMALL, USER_RATING_DICT_SMALL, MOVIE_USER_DICT_SMALL, 2)
    [302156, 293660]
    """

    # Your code here

    similar_users = get_similar_users(target_rating, user_ratings, movie_users)

    test = lambda x: len([k for k, v in x.items() if v >= 3.5])

    candidate = {}
    for k, v in similar_users.items(): # k为用户id
        for k1, v1 in user_ratings[k].items(): # k1为电影id
            if v1 >= 3.5 and k1 not in target_rating and k1 in movies:
                num_user_movie = test(user_ratings[k])
                movie_popularity = len(movie_users[k1])
                user_similarity_score = v 
                contribution = user_similarity_score / (num_user_movie * movie_popularity)
                if k1 not in candidate:
                    candidate[k1] = contribution
                else:
                    candidate[k1] += contribution

    mid = []
    for k, v in candidate.items():
        found = False 
        for i in range(len(mid)):
            if v > mid[i][1] or (v == mid[i][1] and k < mid[i][0]):
                mid.insert(i, (k, v))
                found = True 
        if not found:
            mid.append((k, v))

    return [k for k, _ in mid][:num_movies]


if __name__ == '__main__':
    """Uncomment to run doctest"""
    import doctest
    doctest.testmod()