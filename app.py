'''import os
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing import image

# ---------------------------------
# Flask App Initialization
# ---------------------------------
app = Flask(__name__)
# ---------------------------------
# Upload Folder (auto created)
# ---------------------------------
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ---------------------------------
# Load Trained CNN Model
# ---------------------------------
MODEL_PATH = "model/model_trained.keras"   # ✅ correct path
model = tf.keras.models.load_model(MODEL_PATH)

print("✅ Model loaded successfully")

# ---------------------------------
# Class Names (MUST MATCH TRAINING ORDER)
# ---------------------------------
class_names = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']

# ---------------------------------
# Image Parameters
# ---------------------------------
IMG_SIZE = 128   # same as training

# ---------------------------------
# Image Preprocessing Function
# ---------------------------------
def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# ---------------------------------
# Routes
# ---------------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"})

    # Save uploaded image
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # Prepare image & predict
    img = prepare_image(file_path)
    predictions = model.predict(img)

    predicted_index = np.argmax(predictions)
    predicted_class = class_names[predicted_index]
    confidence = float(np.max(predictions)) * 100

    return jsonify({
        "prediction": predicted_class,
        "confidence": f"{confidence:.2f}%"
    })

# ---------------------------------
# Run Flask App
# ---------------------------------
if __name__ == "__main__":
    app.run(debug=True)
'''
import os
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing import image

# ---------------------------------
# Flask App Initialization
# ---------------------------------
app = Flask(__name__)

# ---------------------------------
# Upload Folder
# ---------------------------------
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------------------------
# Load Trained CNN Model (ONCE)
# ---------------------------------
MODEL_PATH = "model/model_trained.keras"   # ✅ correct path
model = tf.keras.models.load_model(MODEL_PATH)
print("✅ Model loaded successfully")

# ---------------------------------
# Class Names (SAME AS STREAMLIT)
# ---------------------------------
class_names = [
 'Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy'
]

# ---------------------------------
# Image Parameters
# ---------------------------------
IMG_SIZE = 128

# ---------------------------------
# SAME AS Streamlit model_prediction()
# ---------------------------------
def model_prediction(img_path):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    input_arr = image.img_to_array(img)
    input_arr = np.array([input_arr])  # batch
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100
    return result_index, confidence

# ---------------------------------
# Routes
# ---------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("file")

    if file is None or file.filename == "":
        return render_template("index.html", error="No file uploaded")

    # Save image
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # Predict
    result_index, confidence = model_prediction(file_path)
    disease = class_names[result_index]

    return render_template(
        "index.html",
        image_path=file_path,
        disease=disease,
        confidence=f"{confidence:.2f}%"
    )

# ---------------------------------
# Run Flask App
# ---------------------------------
if __name__ == "__main__":
    app.run(debug=True)
