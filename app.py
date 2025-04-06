from flask import Flask, render_template, request, redirect
import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

# Flask setup
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load models
binary_model = load_model('E-Waste_Non-Ewaste_classifier.h5')
multiclass_model = load_model('ewaste_mobilenetv2.h5')

# Load class labels
with open("class_labels.json", "r") as f:
    class_labels = json.load(f)

# Load recycling info
with open("recycling_info.json", "r") as f:
    recycling_info = json.load(f)
recycling_info = {key.lower(): value for key, value in recycling_info.items()}

# Binary class labels
binary_labels = ['e-waste', 'non-e-waste']

# Preprocess image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

# Binary classifier
def fallback_binary_model(img_array):
    prediction = binary_model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0] if prediction.shape[1] > 1 else int(prediction[0][0] > 0.5)
    return binary_labels[predicted_class]

# Multiclass classifier
def predict_with_multiclass_model(img_array):
    predictions = multiclass_model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    confidence = predictions[0][predicted_index]
    predicted_label = class_labels[predicted_index]
    return predicted_label, confidence

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Preprocess and classify
        img_array = preprocess_image(filepath)
        fallback_result = fallback_binary_model(img_array)

        if fallback_result == 'non-e-waste':
            return render_template('result.html',
                                   device_type="Non E-Waste",
                                   ewaste_type=None,
                                   internal_components=None,
                                   image_path=filename)
        else:
            predicted_label, confidence = predict_with_multiclass_model(img_array)
            predicted_label_lower = predicted_label.lower()

            if predicted_label_lower in recycling_info:
                info = recycling_info[predicted_label_lower]
                if isinstance(info, dict):
                    components = [{'component': k.title(), 'recycling_method': v} for k, v in info.items()]
                else:
                    components = [{'component': predicted_label.title(), 'recycling_method': info}]

                return render_template('result.html',
                                       device_type="E-Waste",
                                       ewaste_type=predicted_label,
                                       internal_components=components,
                                       image_path=filename)
            else:
                # e-waste but unknown type
                return render_template('result.html',
                                       device_type="E-Waste",
                                       ewaste_type=predicted_label,
                                       internal_components=None,
                                       image_path=filename)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


