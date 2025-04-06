import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the trained model
model = load_model('E-Waste_Non-Ewaste_classifier.h5')  # Update path if needed

# Define class labels
class_labels = ['e-waste', 'non-e-waste']  # Change this order if needed

# Paste your image path here
image_path = r'class/test/nonewaste/pen/images (1).jpg'  # Example path

# Load and preprocess the image
img = image.load_img(image_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0  # Normalize

# Predict using the model
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction, axis=1)[0] if prediction.shape[1] > 1 else int(prediction[0][0] > 0.5)

# Get and print the label
label = class_labels[predicted_class]
print(f" Predicted Class: {label}")



