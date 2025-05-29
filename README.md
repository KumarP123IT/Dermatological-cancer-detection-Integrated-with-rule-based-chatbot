# 🧬 Skin Disease Detection System

A web-based application that uses deep learning to detect skin diseases from uploaded images. The system also features a chatbot that provides additional information about detected diseases and related dermatological conditions.

---

## 🚀 Features

- 🔍 **Skin Disease Prediction**: Upload a skin image to detect the possible skin condition using a trained deep learning model.
- 💬 **AI Chatbot Integration**: Interact with a smart chatbot for detailed information on various skin diseases.
- 📊 **Result Dashboard**: Displays predicted disease, confidence score, and tips for care.
- 📁 **User-Friendly UI**: Built with HTML, CSS, and JavaScript using Flask backend.
- 📜 **Disease Information Pages**: Static pages about common skin conditions for public awareness.

---

## 🛠️ Tech Stack

**Frontend**:
- HTML5, CSS3, JavaScript
- Bootstrap for responsive design

**Backend**:
- Python 3.x
- Flask Web Framework

**Machine Learning**:
- TensorFlow / Keras
- OpenCV for image preprocessing

**Chatbot**:
- Rule-based or NLP-integrated (custom implementation)

---

## 🧪 Model Details

- Dataset: Kaggle dermatology dataset (custom-processed)
- Preprocessing: Image resizing, normalization
- Architecture: Convolutional Neural Network (CNN)
- Metrics: Accuracy, Precision, Recall

---

## 🖼️ Project Structure

skin-disease-detection/
├── static/
│ ├── css/
│ ├── js/
│ └── uploads/
├── templates/
│ ├── index.html
│ ├── result.html
│ └── about.html
├── chatbot/
│ └── chatbot.py
├── model/
│ └── skin_disease_model.h5
├── app.py
├── requirements.txt
└── README.md


---

## 🧑‍💻 Getting Started

### 🔧 Prerequisites

- Python 3.7+
- pip

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone ...
   cd skin-disease-detection
   ```

2. Create and activate a virtual environment:
    ```bash 
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    python app.py
    ```


5. Open the browser and visit:

   http://127.0.0.1:5000/


### 💬 Usage

   - On the homepage, upload a skin image.

   - The model will predict the most likely disease.

   - View the result and related advice.

   - Use the chatbot for more details or symptom clarification.


### 🔐 Security and Ethics

   - Privacy: All uploaded images are temporarily stored and can be automatically removed for user safety.

   - Disclaimer: This is not a substitute for professional medical advice. Always consult a dermatologist.


### 📈 Future Improvements

    ✅ Add multilingual support in chatbot

    ✅ Expand dataset for more skin conditions

    ✅ Deploy on cloud (Heroku / Render / AWS)

    ✅ Mobile responsiveness improvements


### 🤝 Contributing

    Contributions are welcome! Please fork the repository and submit a pull request. For major changes, please open an issue first to discuss the ideas.

### 🧪 Model Details

   - Model Architecture: MobileNetV2 – lightweight and efficient CNN optimized for mobile and web apps.

   - Dataset: Custom-processed dataset sourced from Kaggle (Train, Validation, Test splits).

   - Accuracy Achieved: 75–85% on test data (varies by class).

   - Image Preprocessing: Resized to 224x224 pixels, normalization, data augmentation (flip, rotate).

   - Frameworks Used: TensorFlow & Keras

   - Inference Time: Optimized for fast predictions (<1s)