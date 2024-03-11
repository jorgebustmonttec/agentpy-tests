from flask import Flask, jsonify, request
from flask_cors import CORS
from addition import add  # Import the add function from addition.py
from intersection import run_intersection_model  # Import your model function
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/sum', methods=['GET'])
def sum_xy():
    # Retrieve x and y from the query parameters and convert them to integers
    x = int(request.args.get('x', 0))
    y = int(request.args.get('y', 0))
    # Use the add function from addition.py to calculate the sum
    z = add(x, y)
    print(f"The sum of {x} and {y} is {z}")
    return jsonify(z=z)


@app.route('/run_model', methods=['GET'])
def run_model():
    parameters = {
        'dimensions': int(request.args.get('dimensions', 16)),
        'steps': int(request.args.get('steps', 20)),
        'max_cars': int(request.args.get('max_cars', 3)),
        'spawn_rate': float(request.args.get('spawn_rate', 1)),
        'chance_run_yellow_light': float(request.args.get('chance_run_yellow_light', 0.5)),
        'chance_run_red_light': float(request.args.get('chance_run_red_light', 0.5)),
    }
    results = run_intersection_model(parameters)
    intersection_matrix = results['reporters']['intersection_matrix'][0]
    total_steps = results['reporters']['total_steps'][0]

    # Ensure total_steps is a native Python int
    total_steps = int(total_steps)

    # If intersection_matrix contains NumPy data types, convert them to Python lists with native int/float
    if isinstance(intersection_matrix, np.ndarray):
        intersection_matrix = intersection_matrix.tolist()
    
    # Convert all elements in intersection_matrix to native Python types if necessary
    intersection_matrix = [[float(cell) if isinstance(cell, np.floating) else int(cell) if isinstance(cell, np.integer) else cell for cell in row] for row in intersection_matrix]

    print(intersection_matrix)
    print(total_steps)

    return jsonify({'intersection_matrix': intersection_matrix, 'total_steps': total_steps})

if __name__ == '__main__':
    app.run(debug=True, port=6000)
