from flask import Flask, request, render_template
from google.cloud import vision
import os


app = Flask(__name__)



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






@app.route('/')
def index():
    # What the user will see when they first enter Rufus Router
    return render_template("index.html")


@app.route('/navigate', methods=["POST"])
# When someone sends  in a file /navigate will handle this 
def navigate():
    if 'image' not in request.files:
        # Checks to see if a user has uploaded an image
        return "Error: No image uploaded", 400
        # Returns error 400 if a user does not uplaod an image
        


    image_file = request.files['image']
    # Grabs the image that user uploaded 
    image_bytes = image_file.read()
    # Reads the contents of the image as bytes that will later be used by API
    


    try:
       
        client = vision.ImageAnnotatorClient()
        # Connects the vision API to the variable client, responsible for the communication between the image sent and Google's API
        image = vision.Image(content=image_bytes)
        # Puts the image bytes into the Image object from Google preparing it to be analyzed by the API


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