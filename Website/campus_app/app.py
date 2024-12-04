from flask import Flask, render_template, request, jsonify
from graph import *
from flask_cors import CORS
from dijkstra import *
import json

# DEBUG: Import test functions
from test import returnNodes

app = Flask(__name__)
CORS(app)
# Store the start and end points for the Dijkstra algorithm
startNode = None
endNode = None

# DEBUG: test for return value
temp = None

storedOutput = [] ##

@app.route('/storage', methods=['POST'])
def receive_data():
    global startNode, endNode, storedOutput, temp
    data = request.get_json()
    
    # VERIFIED: START AND END LOCATIONS GRABBED CORRECTLY
    # Get the location and destination from the request data
    startNode = data['location']
    endNode = data['destination']
    
    # Create graph
    g = Graph(len(graph))
    
    # DEBUG: Run test functions for function return values
    temp = returnNodes(startNode, endNode)
        
    # Trigger the Dijkstra algorithm with the provided start and end nodes
    # Convert node names to their respective indices
    startIndex = g.vertex_map[startNode]
    endIndex = g.vertex_map[endNode]

    # Find the path using Dijkstra
    pathCoords = g.dijkstra(startIndex, endIndex)
    
    # Store output into variable to send to output endpoint
    storedOutput = {"Message": "Success", "pathCoords": temp}##

    # Return the path coordinates as a JSON response
    return jsonify({"Message": "Success", "pathCoords": pathCoords})

# Debug, store dijkstra output in output endpoint
@app.route('/output', methods=['GET'])
def get_output():
    #Retrieve and return the stored result
    if storedOutput:
        return jsonify(storedOutput)
    else:
        return jsonify({"1) Error": "No output stored", "3) Start Node": startNode, "4) End Node": endNode, "2) Path List": temp}), 404


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
