from flask import Flask, jsonify

app = Flask(__name__)

movies = [
	{"id": 1, "name": "Phantom Menace"},
	{"id": 2, "name": "Attack of the Clones"},
	{"id": 3, "name": "Revenge of the Sith"}
]

@app.route('/movies/<int:id>', methods=["GET"])
def get_movie(id):
	for movie in movies:
		if movie["id"] == id:
			return jsonify(movie), 200
	return jsonify({"message": "Not Found"}), 404

@app.route('/movies', methods=["GET"])
def get_movies():
	return jsonify(movies), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
