from flask import Flask, request, render_template
from google.cloud import vision
import os
from heic2png import HEIC2PNG
from PIL import Image
import pillow_heif
import io
# Initialize the Flask app
app = Flask(__name__)

# Set Google Vision API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Steven Murillo\Desktop\CSE Project 155 2\CSE155_Project-RufusRouter\Website\campus_app\JJSon\KeyForAPI.json"


# Define possible campus locations for matching based on general labels
CAMPUS_LOCATIONS = {
    "Sky": "Kolligian Library",
    "Moths and butterflies" : "Student Services Building",
    "Leisure" : "Student Services Building",
    "Arthropod" : "Student Services Building",
    "Pollinator" : "Student Services Building",
}


# def convert_heic_to_PNG(heic_image_bytes):
#     # Use pillow_heif to read the HEIC image
#     heif_file = pillow_heif.read_heif(heic_image_bytes)

#     # Convert the HEIC file to a PIL Image
#     image = Image.open(io.BytesIO(heif_file))

#     # Save the image as PNG in a BytesIO buffer
#     byte_arr = io.BytesIO()
#     image.save(byte_arr, format="PNG")
#     byte_arr.seek(0)  # Reset the pointer to the beginning of the byte array

#     return byte_arr.getvalue()

@app.route('/')
def index():
    # Render the home page with an upload form
    return render_template("index.html")


# @app.route("/upload", methods=["POST"])
# def upload():

#     print("Upload request received")
#     file = request.files['file']
#     print("File received")
#     if file.filename.endswith('.heic'):
#         print("File is HEIC")
#         print("HEIC file detected")
#         heic_image = file.read()
#         print("HEIC image read")
#         byte_arr = convert_heic_to_PNG(heic_image)
#         print("HEIC converted to PNG")
#         return byte_arr
    
#     file_bytes = file.read()
#     return file_bytes

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
