from google.cloud import vision
import io  # For handling byte streams

def detect_landmarks(image_bytes):
    try:
        client = vision.ImageAnnotationClient()

        # Create an Image object using the bytes from the uploaded file
        image = vision.Image(content=image_bytes)

        # Call the Google Vision API to detect landmarks
        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations

        print("Landmarks detected: ")

        # Collect the landmark descriptions
        image_description = []
        for landmark in landmarks:
            image_description.append(landmark.description)
            print(f"- {landmark.description}")
        
        return image_description  # Return the list of landmark descriptions

    except Exception as e:
        print(f"Error during landmark detection: {e}")
        return []  # Return an empty list if something goes wrong
