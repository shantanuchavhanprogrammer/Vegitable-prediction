import json
import os

import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'vegitable_classification.keras')
CLASS_MAP_PATH = os.path.join(os.path.dirname(__file__), 'predicting_vegitable_classes.json')
IMAGE_SIZE = (64, 64)

model = tf.keras.models.load_model(MODEL_PATH)


def get_all_classes():
    with open(CLASS_MAP_PATH, 'r') as f:
        return json.load(f)


def preprocess_image(image_file):
    image = Image.open(image_file.stream).convert('RGB')
    image = image.resize(IMAGE_SIZE)
    image_array = np.array(image, dtype=np.float32) / 255.0
    return np.expand_dims(image_array, axis=0)


def predict_vegetable(image_file):
    image_array = preprocess_image(image_file)
    prediction = model.predict(image_array, verbose=0)[0]
    predicted_index = int(np.argmax(prediction))
    print(predicted_index)
    confidence = float(prediction[predicted_index])
    class_name = get_all_classes().get(str(predicted_index), 'Unknown')
    return class_name, confidence