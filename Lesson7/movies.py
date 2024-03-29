from settings import *
import json

# Initiate our database
db = SQLAlchemy(app)    

class Movie(db.Model):
    __tablename__ = 'movies'  # create a table name
    id = db.Column(db.Integer, primary_key=True) # this is the primary key
    title = db.Column(db.String(80), nullable = False)  # column can't be empty
    year = db.Column(db.Integer, nullable = False)
    genre = db.Column(db.String(80),  nullable = False)

    def json(self):
        return {
            'id':self.id, 'title' : self.title, 'year': self.year, 'genre' : self.genre
        }
    
    def add_movie(_title, _year, _genre):
        '''
        function to add movie to database using _title, _year, _genre
        '''
        new_movie = Movie(title=_title, year = _year, genre = _genre)
        db.session.add(new_movie)       # add new movie to database session
        db.session.commit()             # commit changes to session

    def get_all_movies():
        '''
        function to get all movies in our database
        '''
        return [Movie.json(movie) for movie in Movie.query.all()]
    
    def get_movie(_id):
        '''
        function to get movie using the id of the movie as parameter
        '''
        return [Movie.json(Movie.query.filter_by(id=_id).first())]
    
    def update_movie(_id, _title, _year, _genre):
        '''
        function to update the detail of a movie using the id, title, year and genre
        '''
        movie_to_update = Movie.query.filter_by(id=_id).first()
        movie_to_update.title = _title
        movie_to_update.year = _year
        movie_to_update.genre = _genre
        db.session.commit()

    def delete_movie(_id):
        '''
        function to delete a movie from our database using the id of the movie as the parameter
        '''
        Movie.query.filter_by(id=_id).delete()
        db.session.commit() # commit the new change to our database
