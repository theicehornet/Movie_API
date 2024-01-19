from flask import Flask, jsonify, request
from utils.utilities import add_movie, get_movies, get_random_movie, get_movie_by_id, delete_movie, update_movie

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
     
@app.route("/Create/", methods=["POST"])
def CreateMovie():
    """Crea una pelicula y la retorna"""
    try:
        message = add_movie(request.json)
        return jsonify(message)
    except Exception as e:
        return jsonify({"err":f"{e}"})
        


@app.route("/", methods=["GET"])
def GetMovies():
    """Retorna todas las peliculas""";
    try:
        message = get_movies()
    except Exception as e:
        message = f"Error: {e}",500
    finally:
        return jsonify({"movies":message})


@app.route("/Update/", methods=["PATCH"])
def UpdateMovie():
    try:
        message = update_movie(request.json)
    except Exception as e:
        message = f"Error: {e}",500
    finally:
        return jsonify({"movie":message})


@app.route("/Delete/", methods=["DELETE"])
def DeleteMovie():
    """Retorna una pelicula con un id en especifico"""
    try:
        message = delete_movie(request.json)
    except Exception as e:
        message = f"Error: {e}",500
    finally:
        return jsonify(message)
    

@app.route("/<string:id>", methods=["GET"])
def GetMovie(id):
    """Retorna una pelicula con un id en especifico"""
    try:
        message = get_movie_by_id(id)
    except Exception as e:            
        message = f"Error: {e}",500
    finally:
        return jsonify(message)


@app.route("/random", methods=["GET"])
def RandomMovie():
    """Retorna una pelicula random"""
    try:
        message = get_random_movie()
    except Exception as e:
        message = f"Error: {e}",500
    finally:
        return jsonify(message)


if __name__ == "__main__":
    app.run(port=4520,debug=True)
