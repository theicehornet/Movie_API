import os
import json
import random
from model.movie import Movie


def get_movies():
    if os.path.exists("movies.json"):
        with open("movies.json","r", encoding="utf-8") as file:
            movies_data = json.load(file)
        if len(movies_data) == 0:
            return {"movie": "no movies"}
        return movies_data
    else:
        movies = [Movie("asd123","Hunger Games","https://movieguide.b-cdn.net/wp-content/uploads/2012/06/98068201-0cc9-42ed-81ee-dcd480c4cba8-768x1152.jpg","Gary Ross",["Acciones","Aventura"],["Jennifer Lawrence"," Josh Hutcherson","Liam Hemsworth"]).to_dict()]
        with open("movies.json","w", encoding="utf-8") as file:
            json.dump(movies,file)
        return {"movie":"no movies"}        


def verificar_movie_existencia(movietoperform):
    movies = get_movies()
    for movie in movies:
        if movie["Titulo"] == movietoperform["Titulo"] or movie["Id"] == movietoperform["Id"]:
            return True
    return False


def verificar_datos(data):
    campos_necesarios = ["Id", "Titulo", "Poster", "Director", "Generos", "Actores"]
    for campo in campos_necesarios:
        if campo not in data:
            raise Exception(f"Falta el campo {campo} en los datos")
    movie = Movie(data["Id"],data["Titulo"],data["Poster"],data["Director"],data["Generos"],data["Actores"])
    moviedict = movie.to_dict()
    if verificar_movie_existencia(moviedict):
        raise Exception("La pelicula ya existe")
    return moviedict


def add_movie(data):
    movie = verificar_datos(data)
    if os.path.exists("movies.json"):
        movies_data = get_movies()
        movies_data.append(movie)
    else:
        movies_data = [movie]
    
    with open("movies.json","w") as file:
        json.dump(movies_data,file)
    return {"Exito":"se creo la pelicula exitosamente","movie":movie}


def update_movie(data):
    movieupdate = verificar_datos(data)
    movies = get_movies()
    i = 0
    while i < len(movies):
        if movies[i]["Id"] == movieupdate["Id"]:
             movies[i]["Titulo"]=movieupdate["Titulo"],
             movies[i]["Poster"]=movieupdate["Poster"],
             movies[i]["Director"]=movieupdate["Director"],
             movies[i]["Generos"]=movieupdate["Generos"],
             movies[i]["Actores"]=movieupdate["Actores"]
             with open("movies.json","w") as file:
                json.dump(movies,file)
             return {"Success":"movie updated","movie":movieupdate}
        i += 1
    raise Exception("movie not found")
    

def movie_exist(id):
    movies = get_movies()
    for movie in movies:
        if movie["id"] == id:
            return True
    return False


def delete_movie(id):
    if movie_exist():
        movies = get_movies()
        new_movies = [movie for movie in movies if movie["id"] != id]
        with open("movies.json","w") as file:
            json.dump(new_movies,file)
        return {"Succes":"Movie deleted"}
    raise Exception("not found")


def get_random_movie():
    movies = get_movies()
    random_movie = random.choice(movies)
    return random_movie


def get_movie_by_id(id):
    movies = get_movies()
    for movie in movies:
        if movie["id"] == id:
            return {"movie":movie}
    raise Exception("not found")
