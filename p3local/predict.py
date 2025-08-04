import tensorflow as tf 
import numpy as np 
from config import IMG_SIZE, MODEL_SAVE_PATH

def predict_image(image_path, class_names):
    model = tf.keras.models.load_model(MODEL_SAVE_PATH)

    img = tf.keras.preprocessing.image.load_img(image_path,target_size=IMG_SIZE)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array,axis=0)/255.0

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions)
    print(f"Predicted: {predicted_class} ({confidence:.2f})")

from data_loader import load_datasets
_, _, class_names = load_datasets()
predict_image("test_image/01.jpg", class_names)