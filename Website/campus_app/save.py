from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/storage', methods=['POST'])
def recieve_data():
    data = request.get_json()
    return jsonify

def process_user_input(user_input):
    # Example function to process input
    return f"Received input: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)