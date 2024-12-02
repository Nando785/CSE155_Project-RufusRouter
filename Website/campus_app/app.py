from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import dijkstra 

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/navigate', methods=['POST'])
def navigate():
    data = request.get_json()
    location = data.get('location')
    destination = data.get('destination')

    if not location or not destination:
        return jsonify({'error': 'Invalid input'}), 400

    path = dijkstra.find_route(location, destination)

    if not path:
        return jsonify({'error': 'No path found'}), 404

    return jsonify({'path': path})



if __name__ == '__main__':
    app.run(debug=True)
