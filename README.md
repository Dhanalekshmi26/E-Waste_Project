
# ♻️ E-WASTE ANALYSIS AND PREDICTING RECYCLING METHOD
![project-banner](https://img.shields.io/github/languages/top/Dhanalekshmi26/Smart-E-Waste-System?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

> 🚀 A Machine Learning-based web application to detect **electronic waste items** and recommend safe and effective **recycling methods** for each component — built with TensorFlow, Flask, and deep learning.

---

## 🌍 Why This Project Matters

E-waste is one of the fastest-growing waste streams worldwide. Most people don't know what qualifies as e-waste or how to dispose of it responsibly.

This intelligent system helps users:
- Detect if an item is **e-waste or not**
- Identify the **type of e-waste** (e.g., laptop, printer)
- Show **internal components** of the device
- Recommend **correct recycling methods** (e.g., pyrometallurgical, lithium recovery)

---

## 📸 Live Demo Screenshot

<img src="static/demo_result.jpg" alt="E-Waste Detection Screenshot" width="80%">

---

## 🧠 How It Works (Simple Steps)

1. **Upload any image** (e.g., mobile, banana, remote, etc.)
2. The system first classifies it as:
   - ✅ **E-Waste**
   - ❌ **Non E-Waste** (e.g., fruits or people)
3. If E-Waste, it identifies the **specific device type**
4. Based on the device, it fetches:
   - 📦 Internal components (like battery, screen, circuit)
   - ♻️ Recycling method for each

---

## 🔍 Methodology

### 🧪 1. E-Waste vs. Non-E-Waste Classification
- **Model:** MobileNetV2
- **Input:** Uploaded image
- **Output:** Binary prediction (`e-waste` or `non-e-waste`)

### 🧠 2. Specific E-Waste Detection
- **Model:** EfficientNet-B3
- **Output:** Device type (e.g., Laptop, Microwave)
- **Confidence Score:** e.g., 98.76%

### 🔧 3. Component Analysis & Recycling Suggestions
- Based on internal database (`recycling_info.json`)
- Maps each device to its internal components
- Shows recommended **eco-friendly recycling methods**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core backend |
| TensorFlow / Keras | Model training & prediction |
| Flask | Web framework |
| HTML/CSS | Frontend UI |
| JSON | Internal knowledge base for recycling info |

---

## 📂 Project Structure

```
📁 static/
    └── uploads/       # Uploaded images
📁 templates/
    ├── index.html     # Upload UI
    └── result.html    # Result display
📁 models/
    ├── E-Waste_Non-Ewaste_classifier.h5
    └── ewaste_mobilenetv2.h5
📄 recycling_info.json  # Maps devices to recycling details
📄 app.py               # Main Flask app
📄 README.md
```

---

## 💡 Sample Output

**Uploaded Image:** `laptop.jpg`  
**Detected:** *Laptop*  
**Confidence:** `98.45%`

| Component    | Recycling Method               |
|--------------|-------------------------------|
| Battery      | Lithium Recovery              |
| Motherboard  | Hydrometallurgical Processing |
| Screen       | Glass Shredding               |

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.10
- TensorFlow
- Flask
- NumPy, Pillow, etc.

### 🖥️ Run Locally

```bash
git clone https://github.com/Dhanalekshmi26/Smart-E-Waste-System.git
cd Smart-E-Waste-System
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 📈 Model Performance

| Stage                    | Model         | Accuracy |
|--------------------------|---------------|----------|
| E-Waste Classification   | MobileNetV2   | ~95%     |
| E-Waste Type Detection   | EfficientNet-B3 | ~92%     |

---

## 🧠 Future Enhancements

- 🔄 Replace JSON with SQL/NoSQL database
- 🧰 Add more e-waste categories
- 🌐 Deploy as a hosted web app (Render, Heroku, etc.)
- 📱 Build mobile app version

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for more info.

---

## 🙌 Acknowledgements

Special thanks to:
- TensorFlow/Keras community
- Electronics recycling researchers
- Open image datasets from Kaggle

-----





