import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load models
binary_model = load_model('E-Waste_Non-Ewaste_classifier.h5')
multiclass_model = load_model("ewaste_mobilenetv2.h5")

# Load class labels
with open("class_labels.json", "r") as f:
    class_labels = json.load(f)

# Load recycling info
with open("recycling_info.json", "r") as f:
    recycling_info = json.load(f)

# Normalize keys for case-insensitive matching
recycling_info = {key.lower(): value for key, value in recycling_info.items()}

# Class labels for binary classifier
binary_labels = ['e-waste', 'non-e-waste']


def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array


def fallback_binary_model(img_array):
    prediction = binary_model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0] if prediction.shape[1] > 1 else int(prediction[0][0] > 0.5)
    return binary_labels[predicted_class]


def predict_with_multiclass_model(img_array):
    predictions = multiclass_model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    confidence = predictions[0][predicted_index]
    predicted_label = class_labels[predicted_index]
    return predicted_label, confidence


def classify_image(image_path):
    img_array = preprocess_image(image_path)

    # Step 1: Use binary model first
    fallback_result = fallback_binary_model(img_array)
    print(f"\n Binary Model says: {fallback_result.upper()}")

    if fallback_result == 'non-e-waste':
        print(" This item is NON E-WASTE and cannot be recycled.")
        return

    # Step 2: If e-waste, run multiclass model
    predicted_label, confidence = predict_with_multiclass_model(img_array)
    predicted_label_lower = predicted_label.lower()

    if predicted_label_lower in recycling_info:
        print(f"\n Detected: {predicted_label} (Confidence: {confidence:.2f})")

        recycling_data = recycling_info[predicted_label_lower]
        if isinstance(recycling_data, dict):
            print("\n Internal Components & Recycling Methods:")
            for component, method in recycling_data.items():
                print(f" - {component.title()} → {method}")
        elif isinstance(recycling_data, str):
            print(f"\n Recycling Method: {recycling_data}")
    else:
        print(f"\n '{predicted_label}' is not in known classes list.")
        print(" It's e-waste, but the type is unknown to our system.")


# === Test it ===
test_image_path = r"dataset/DATASET/modified-dataset/train/computer/aug_0_4006.jpeg"
classify_image(test_image_path)


