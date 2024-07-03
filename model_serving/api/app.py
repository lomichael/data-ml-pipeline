from flask import Flask, request, jsonify
from predict import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.json
    prediction = predict(data)
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

