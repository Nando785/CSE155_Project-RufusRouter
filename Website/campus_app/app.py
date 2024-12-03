from flask import Flask, render_template, request, jsonify
import json
import dijkstra 

app = Flask(__name__)
# Store the start and end points for the Dijkstra algorithm
startNode = None
endNode = None

@app.route('/storage', methods=['POST'])
def receive_data():
    global startNode, endNode
    data = request.get_json()
    
    # Get the location and destination from the request data
    startNode = data['location']
    endNode = data['destination']
    
    # Now, trigger the Dijkstra algorithm with the provided start and end nodes
    # Convert node names to their respective indices
    startIndex = dijkstra.g.vertex_map[startNode]
    endIndex = dijkstra.g.vertex_map[endNode]

    # Find the path using Dijkstra
    pathCoords = dijkstra.g.dijkstra(startIndex, endIndex)

    # Return the path coordinates as a JSON response
    return jsonify({"Message": "Success", "pathCoords": pathCoords})

@app.route('/storage', methods=['GET'])
def get_storage_data():
    return jsonify({"startNode": startNode, "endNode": endNode})

@app.route('/')
def home():
    return render_template('index.html')

# Route for the ACS page
@app.route('/acs')
def acs():
    return render_template('acs.html')

# Add other routes as needed
@app.route('/cob1')
def cob1():
    return render_template('cob1.html')

@app.route('/cob2')
def cob2():
    return render_template('cob2.html')

@app.route('/library1')
def library1():
    return render_template('library1.html')

@app.route('/se2')
def se2():
    return render_template('se2.html')

@app.route('/ssm')
def ssm():
    return render_template('ssm.html')

@app.route('/ssb')
def ssb():
    return render_template('ssb.html')

if __name__ == '__main__':
    app.run(debug=True)
