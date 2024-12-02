from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import io  # For handling image data in memory
from ML import detect_landmarks
import dijkstra  # Assuming dijkstra.py is imported here

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

@app.route('/upload', methods=['POST'])
def image_upload():
    # Check if the file is part of the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']

    # If no file is selected
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Read the file as a byte stream in memory
    image_bytes = file.read()

    # Call the function to detect landmarks directly from the image bytes
    image_description = detect_landmarks(image_bytes)

    # Render the result template and pass the detected landmarks
    return render_template('result.html', image_description=image_description)

if __name__ == '__main__':
    app.run(debug=True)
