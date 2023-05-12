from movies import *

# define route to get all movies
@app.route('/movies', methods =['GET'])
def get_movies():
    '''
    Function to get all the movies in the database
    '''
    return jsonify({'Movies': Movie.get_all_movies()})

# route to get movie by id
@app.route('/movies/<int:id>', methods = ['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)

# route to add new movie
@app.route('/movies', methods =['POST'])
def add_movie():
    '''
    Function to add new movie to our database
    '''
    request_data = request.get_json()
    Movie.add_movie(request_data["title"], request_data["year"], request_data["genre"])
    response = Response("Movie is added", 201, mimetype='application/json')
    return response

# route to update movie by id with PUT method
@app.route('/movies/<int:id>', methods = ['PUT'])
def update_movie(id):
    '''
    Function to edit movie in our databasse using movie id
    '''
    request_data = request.get_json()
    Movie.update_movie(id, request_data['title'], request_data['year'], request_data['genre'])
    response = Response("Movie is updated", status=200, mimetype='application/json')
    return response

# route to delete movie using DELETE method
@app.route('/movies/<int:id>', methods = ['DELETE'])
def remove_movie(id):
    '''
    Function to delete movie from our database
    '''
    Movie.delete_movie(id)
    response = Response("Movie is deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=1234, debug= True)
    