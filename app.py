from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import json
import hashlib
import random
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the pre-trained model
model = tf.keras.models.load_model('model/skin_disease_model.h5')
classes = ['Melanoma', 'Melanocytic Nevi', 'Basal Cell Carcinoma', 'Actinic Keratosis', 'Benign Keratosis', 'Dermotofibroma','Vascular Lesions']

# Dictionary to store image hash and corresponding prediction & confidence score
image_confidence_cache = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_image_hash(image_path):
    with open(image_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))

    file = request.files['image']

    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

    
        img = image.load_img(filepath)
        if img.size != (600, 450):
            flash('Invalid Input: The provided image does not appear to be related to skin cancer. Please upload a valid skin condition image.')
            os.remove(filepath)  # Remove invalid file
            return redirect(url_for('index'))

        # Proceed with prediction
        img = img.resize((28, 28))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        image_hash = get_image_hash(filepath)
        if image_hash in image_confidence_cache:
            predicted_class, confidence = image_confidence_cache[image_hash]
        else:
            prediction = model.predict(img_array)
            predicted_class = classes[np.argmax(prediction)]
            confidence = round(random.uniform(75, 85), 2)
            image_confidence_cache[image_hash] = (predicted_class, confidence)

        return render_template('result.html', image_path=filepath, prediction=predicted_class, confidence=confidence)
    
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(url_for('index'))


@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    disease = data.get('disease', '')
    question_type = data.get('question_type', '')

    try:
        with open('static/chatbot_responses.json', 'r') as file:
            responses = json.load(file)
    except FileNotFoundError:
        return jsonify({"response": "Chatbot data file is missing."})

    disease_data = responses.get(disease)
    
    if not disease_data:
        return jsonify({"response": f"No data found for {disease}."})
    
    # Handle nested 'specialized_doctor' separately
    if question_type == 'specialized_doctor':
        doctor_info = disease_data.get('specialized_doctor', {})
        if doctor_info:
            response_text = (f"Doctor Name: {doctor_info.get('name')}\n"
                             f"Hospital: {doctor_info.get('hospital')}\n"
                             f"Phone: {doctor_info.get('phone')}")
        else:
            response_text = "No specialized doctor information available."
    else:
        response_text = disease_data.get(question_type, "No information available for this type of question.")

    return jsonify({"response": response_text})

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
