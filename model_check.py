import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the trained model
model = load_model("ewaste_mobilenetv2.h5")

# Load class labels
with open("class_labels.json", "r") as f:
    class_labels = json.load(f)

# Load recycling info
with open("recycling_info.json", "r") as f:
    recycling_info = json.load(f)

# Normalize keys for case-insensitive matching
recycling_info = {key.lower(): value for key, value in recycling_info.items()}

# Prediction function
def predict_class(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    confidence = predictions[0][predicted_index]
    predicted_label = class_labels[predicted_index]
    return predicted_label, confidence

# Recycling info lookup
def fetch_recycling_info(item_name, confidence):
    item_key = item_name.lower()

    # If it's an internal component → just show predicted item
    if item_key in recycling_info and isinstance(recycling_info[item_key], str):
        print(f"\n Predicted Item: {item_name} (Confidence: {confidence:.2f})")

    # If it's an external device → show internal components + recycling methods
    elif item_key in recycling_info and isinstance(recycling_info[item_key], dict):
        print(f"\n Predicted Item: {item_name} (Confidence: {confidence:.2f})")
        print(f"\n Internal Components & Recycling Methods for '{item_name.title()}':")
        for component, method in recycling_info[item_key].items():
            print(f" {component.title()} → {method}")
    else:
        print(f"\n Predicted Item: {item_name} (Confidence: {confidence:.2f})")
        

#  Replace with your test image path
test_image_path = "dataset/DATASET/modified-dataset/train/transformer/download (3).jpg"
predicted_label, confidence = predict_class(test_image_path)
fetch_recycling_info(predicted_label, confidence)

