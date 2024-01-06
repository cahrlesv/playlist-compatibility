from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET', 'POST'])
def handle_compatibility_check():
    if request.method == 'POST':
        # Assuming you want to process the form data here
        data = request.form
        playlist1 = data.get('playlist1')
        playlist2 = data.get('playlist2')

        # Perform compatibility check or process the received data as needed
        # For now, let's generate a random compatibility percentage
        compatibility_percentage = random.randint(0, 100)

        return jsonify({'compatibility': compatibility_percentage})
    else:
        return jsonify({'message': 'Hello from the server!'})

if __name__ == '__main__':
    app.run(debug=True, port=3000)

