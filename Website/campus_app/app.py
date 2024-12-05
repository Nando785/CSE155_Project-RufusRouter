from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dijkstra import Graph
from graph import graph
from google.cloud import vision
import os

app = Flask(__name__)
CORS(app)
# Store the start and end points for the Dijkstra algorithm
startNode = None
endNode = None

storedOutput = []

@app.route('/storage', methods=['POST'])
def receive_data():
    global startNode, endNode, storedOutput
    data = request.get_json()
    
    # Get the location and destination from the request data
    startNode = data['location']
    endNode = data['destination']
    
    # Create graph
    g = Graph(len(graph))
    g.setup_graph(graph)
        
    # Trigger the Dijkstra algorithm with the provided start and end nodes
    # Convert node names to their respective indices
    startIndex = g.vertex_map[startNode]
    endIndex = g.vertex_map[endNode]

    # Find the path using Dijkstra
    pathCoords = g.dijkstra(startIndex, endIndex)
    
    # Store output into variable to send to output endpoint
    storedOutput = {"coords":pathCoords}

    # Return the path coordinates as a JSON response
    return jsonify({"Message": "Success", "pathCoords": pathCoords})

# Debug, store dijkstra output in output endpoint
@app.route('/output', methods=['GET'])
def get_output():
    if storedOutput:
        return jsonify(storedOutput)
    else:
        return jsonify({"1) Error": "No output stored", "3) Start Node": startNode, "4) End Node": endNode, "2) Path List": storedOutput}), 404


# Debug, allow dev to view storage endpoint contents
@app.route('/storage', methods=['GET'])
def get_storage_data():
    return jsonify({"startNode": startNode, "endNode": endNode})

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the ACS page
@app.route('/acs')
def acs():
    return render_template('acs.html')

# Route for the cob1 page
@app.route('/cob1')
def cob1():
    return render_template('cob1.html')

# Route for the cob2 page
@app.route('/cob2')
def cob2():
    return render_template('cob2.html')

# Route for the library1 page
@app.route('/library1')
def library1():
    return render_template('library1.html')

# Route for the se2 page
@app.route('/se2')
def se2():
    return render_template('se2.html')

# Route for the ssm page
@app.route('/ssm')
def ssm():
    return render_template('ssm.html')

# Route for the ssb page
@app.route('/ssb')
def ssb():
    return render_template('ssb.html')

if __name__ == '__main__':
    app.run(debug=True)

# ====== MACHINE LEARNING CODE ======

# Sets the currently directory to Website/campus_app/app.py
current_dir = os.path.dirname(os.path.abspath(__file__))


# Sets the path for the JSON file which I have stored in a folder JJSon
json_key_path = os.path.join(current_dir, 'JJSon', 'KeyForAPI.json')


# Use Google SDK to set up the credentials that allow API to be used and functional 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_path




# Matching what the API sees in pictures sent to certain buildings on campus
CAMPUS_LOCATIONS = {
    "Moths and butterflies" : "ssb",
    "Leisure" : "ssb",
    "Arthropod" : "ssb",
    "Pollinator" : "ssb",
    "Tower block" :  "library1",
    "Asphalt" : "ssb",
    "Tail" : "cob2",
    "Terrestial animal": "cob2",
    "Aluminium"  : "ssb",
}

@app.route('/navigate', methods=["POST"])
def navigate():
    # Check for the target location value from the dropdown
    dropdown_location = request.form.get('location')  # 'location' is the name of the dropdown in HTML

    # Check if an image is uploaded
    image_file = request.files.get('image')  # None if no file uploaded

    if image_file and image_file.filename:  # If an image is uploaded
        image_bytes = image_file.read()

        try:
            # Run the ML code with the uploaded image
            client = vision.ImageAnnotatorClient()
            image = vision.Image(content=image_bytes)

            # Perform label detection
            label_response = client.label_detection(image=image)
            labels = label_response.label_annotations

            # Debugging: Print the full response
            print("FULL API RESPONSE (Label Detection):")
            for label in labels:
                print(f"{label.description} (score: {label.score})")

            # Check if any labels match a campus location
            for label in labels:
                if label.description in CAMPUS_LOCATIONS:
                    location_name = CAMPUS_LOCATIONS[label.description]
                    # return render_template("result.html", location_name=location_name)
                    return jsonify({"location": location_name}), 404

            # Perform text detection
            text_response = client.text_detection(image=image)
            texts = text_response.text_annotations

            # If no match is found
            # return render_template("result.html", location_name="Unknown Location")
            return jsonify({"location": location_name}), 404

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return f"Error occurred: {str(e)}", 500

    elif dropdown_location:  # If no image is uploaded but dropdown has a value
        # if dropdown_location in CAMPUS_LOCATIONS.values():
        #     # Validate and return the dropdown location
        #     return render_template("result.html", location_name=dropdown_location)
        # else:
        #     # If the dropdown value does not match any location
            # return render_template("result.html", location_name="Invalid Location")
            return jsonify({"location": dropdown_location}), 404

    else:
        # If neither an image nor a dropdown value is provided
        # return "Error: No input provided. Please upload an image or select a location.", 400
        return jsonify({"location": "No location found"}), 404