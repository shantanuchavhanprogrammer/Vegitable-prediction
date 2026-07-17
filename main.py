from flask import Flask, jsonify, request, render_template
from utils import predict_vegetable

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    image_file = request.files.get('image')
    if not image_file or not image_file.filename:
        return jsonify({'error': 'No image uploaded'}), 400

    predicted_class_name, confidence = predict_vegetable(image_file)
    print(f"Predicted Class: {predicted_class_name}, Confidence: {confidence:.4f}")
    return jsonify({
        'vegetable': predicted_class_name,
        'confidence': round(confidence, 4)
    })


if __name__ == '__main__':
    app.run(debug=True)