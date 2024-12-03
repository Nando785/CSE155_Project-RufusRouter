from flask import Flask, request, render_template
from google.cloud import vision
import os




app = Flask(__name__)



# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the relative path to your JSON file
json_key_path = os.path.join(current_dir, 'JJSon', 'KeyForAPI.json')

# Set the environment variable to the relative path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_path


# Define possible campus locations for matching based on general labels
CAMPUS_LOCATIONS = {
    "Sky": "Kolligian Library",
    "Moths and butterflies" : "Student Services Building",
    "Leisure" : "Student Services Building",
    "Arthropod" : "Student Services Building",
    "Pollinator" : "Student Services Building",
}




@app.route('/')
def index():
    # Render the home page with an upload form
    return render_template("index.html")




@app.route('/navigate', methods=["POST"])
def navigate():
    # Ensure an image file was uploaded
    if 'image' not in request.files:
        return "Error: No image uploaded", 400
    

    image_file = request.files['image']
    image_bytes = image_file.read()
    

    try:
        # Initialize the Vision API client
        client = vision.ImageAnnotatorClient()
        image = vision.Image(content=image_bytes)

        # Perform label detection (focus on general labels)
        label_response = client.label_detection(image=image)
        labels = label_response.label_annotations

        # Debugging: Print the full response
        print("FULL API RESPONSE (Label Detection):")
        for label in labels:
            print(f"{label.description} (score: {label.score})")

       # Check if any of the labels match a campus location
        for label in labels:
            if label.description in CAMPUS_LOCATIONS:
                location_name = CAMPUS_LOCATIONS[label.description]
                return render_template("result.html", location_name=location_name)

        # Check text in image to see if it matches a campus location
        text_response = client.text_detection(image=image)
        texts = text_response.text_annotations


        # if no match is found in the labels, check the text in the image
        for text in texts:
            if text.description in CAMPUS_LOCATIONS:
                location_name = CAMPUS_LOCATIONS[text.description]
                return render_template("result.html", location_name=location_name)
        # if no match is found in the text, return a generic response
        return render_template("result.html", location_name="Unknown Location")

    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Debugging log to catch API or file reading issues
        return f"Error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
