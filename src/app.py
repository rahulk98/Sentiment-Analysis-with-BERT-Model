from flask import Flask, request, jsonify
from predict import predict_sentiment
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    # Your prediction logic here
    sentiment = predict_sentiment(text)  # Your existing function
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
