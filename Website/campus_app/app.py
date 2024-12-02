from flask import Flask, request, render_template
from google.cloud import vision
import os

# Initialize the Flask app
app = Flask(__name__)

# Set Google Vision API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Steven Murillo\Desktop\CSE Project 155 2\CSE155_Project-RufusRouter\Website\campus_app\JJSon\KeyForAPI.json"

# Define possible campus locations for matching based on general labels
CAMPUS_LOCATIONS = {
    "Kolligian Library": "Library",
    "Student Services Building": "SSB",
    "Building": "General Building",  # Can match with "building", "office", etc.
    "Urban design": "Urban Area",  # general urban term
    "Facade": "Building Facade",  # buildings' exteriors
    "City": "Campus City Area",  # general city term
    "Campus": "Campus Area",  # match for "campus" label
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
    print(f"Image uploaded: {image_file.filename}")  # Debugging log to check image upload
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

        # Check if any labels match known locations
        for label in labels:
            if label.description in CAMPUS_LOCATIONS:
                location_name = CAMPUS_LOCATIONS[label.description]
                return render_template("result.html", location_name=location_name)

        # If no match is found, return "unknown"
        return render_template("result.html", location_name="unknown")

    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Debugging log to catch API or file reading issues
        return f"Error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
