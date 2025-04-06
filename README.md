
# ♻️ Smart E-Waste Detection and Recycling Guidance System

A web-based intelligent system to identify **electronic waste (e-waste)** items and provide the best recycling methods — built using **deep learning (CNN)** and **Flask**.

---

## 🌍 Problem Statement

In today's world, **electronic waste is increasing rapidly**, but many people are unaware of **how to dispose of it properly**. Throwing away gadgets like laptops, phones, or microwaves in regular bins can **harm the environment**.

---

## 🧠 Our Solution

This project introduces an **AI-powered system** that:
1. **Identifies** whether an image contains an **e-waste item** or not.
2. If it's e-waste, it further **classifies the type of item** (e.g., Laptop, Mobile Phone).
3. It then **displays the internal components** of the item (e.g., CPU, Circuit Board).
4. Finally, it suggests the **best recycling method** for each component.

---

## 💡 How It Works

1. **Upload a photo** of any item (e.g., a laptop, a fruit, or a washing machine).
2. The AI model checks if the item is:
   - 🟢 **E-Waste**
   - 🔴 **Non E-Waste** (like apple, tomato — cannot be recycled this way)
3. If it's e-waste, it shows:
   - The **item name** (like “Television”)
   - The **confidence score**
   - A list of internal parts (like “Motherboard”, “Capacitors”)
   - **Recycling method** for each part (e.g., *Hydrometallurgical Processing*)

---

## 🖥️ Tech Stack

| Layer           | Technology Used       |
|----------------|------------------------|
| Frontend       | HTML, CSS (via Flask)  |
| Backend        | Python + Flask         |
| AI Models      | CNN using TensorFlow/Keras |
| Image Classes  | MobileNetV2, EfficientNet |
| Data Storage   | JSON (for mapping components and methods) |

---

## 📂 Project Structure

```
📁 static/
    └── uploads/         # Uploaded images
📁 templates/
    ├── index.html       # Homepage
    └── result.html      # Prediction results
📁 models/
    ├── E-Waste_Non-Ewaste_classifier.h5
    └── ewaste_mobilenetv2.h5
📄 class_labels.json     # E-waste categories
📄 recycling_info.json   # Internal parts & methods
📄 app.py                # Main Flask app
```

---

## 🚀 How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/e-waste-detector.git
cd e-waste-detector
```

2. **Install requirements:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
python app.py
```

4. **Open in browser:**
```
http://127.0.0.1:5000/
```

---

## 🧪 Sample Images

Try uploading:
- ✅ Laptop, Mobile, Refrigerator → gets detailed recycling info.
- ❌ Apple, Banana → shows **"This is non e-waste."**

---

## 🙌 Acknowledgements

- This project is part of an initiative to **promote environmental awareness** and **sustainable e-waste disposal**.
- Special thanks to [Kaggle](https://kaggle.com) and open datasets for training resources.

---


