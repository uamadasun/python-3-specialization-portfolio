"""This code uses the OMDB and Tastedive APIs to recommend similar movies to the movie the user inputs and sort them based on their Rotten Tomatoes score."""

import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    baseURL = "https://tastedive.com/api/similar"
    paramDiction = {"q": movie, "type":"movies", "limit":5}
    fullURL = requests_with_caching.get(baseURL, params=paramDiction, permanent_cache_file = 'permanent_cache.txt')
    return fullURL.json()

def extract_movie_titles(dictionary):
    movieName = dictionary['Similar']['Results']
    movieNameList = []
    for item in movieName:
        movieNameList.append(item['Name'])
    return movieNameList

def get_related_titles(lst):
    movieList = []
    for movie in lst:
        getRelated = get_movies_from_tastedive(movie)
        getTitles = extract_movie_titles(getRelated)
        for item in getTitles:
            if item not in movieList:
                movieList.append(item)
    return movieList

def get_movie_data(movieTitle):
    baseURL = "http://www.omdbapi.com/"
    paramDict = {'apikey':'9692cfb7', "t": movieTitle, "r": 'json'}
    fullURL = requests_with_caching.get(baseURL, params = paramDict, permanent_cache_file = 'permanent_cache.txt')
    #print (fullURL.url)
    return fullURL.json()

def get_movie_rating(dictionary):
    ratings = dictionary['Ratings']
    for rating in ratings:
        if rating["Source"] == "Rotten Tomatoes":
            rating = (int((rating['Value']).strip('%')))
            break
        else:
            rating = 0
    return rating

def get_sorted_recommendations(lst):
    relatedMovies = get_related_titles(lst)
    newDict = {}
    for movie in relatedMovies:
        getMovieData = get_movie_data(movie) #Turns to dictionary of movie data that will need to be converted to a rating
        #print (getMovieData)
        getMovieRating = get_movie_rating(getMovieData)
        #print (getMovieRating)
        if movie not in newDict:
            newDict[movie] = getMovieRating
    newDictSort = sorted(newDict.items(), key = lambda x: (x[1], x[0]), reverse = True)
    print (newDictSort)
    newList = []
    for item in newDictSort:
        newList.append(item[0])
    print (newList)
    return newList
    
