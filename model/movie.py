class Movie:
    def __init__(self,id,titulo,poster,director,generos,actores):
        self.id = id
        self.titulo = titulo
        self.poster = poster
        self.director = director
        self.generos = generos
        self.actores = actores
        
    def to_dict(self):
        return {"Id":self.id, "Titulo":self.titulo,"Poster":self.poster,"Director":self.director,"Generos":self.generos,"Actores":self.actores}