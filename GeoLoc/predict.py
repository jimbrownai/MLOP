import tensorflow as tf 
import tf_keras as keras
import tensorflow_hub as hub
import numpy as np
from tensorflow.keras.preprocessing import image

from config import RESNET_SAVED_MODEL,IMG_SIZE

import json
f = open('class_names.json')
class_names = json.load(f)

loaded_model = keras.models.load_model(
    RESNET_SAVED_MODEL,
    custom_objects={'KerasLayer': hub.KerasLayer}
)

def load_and_preprocess(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = img_array / 127.5 - 1.0   # normalize to [-1,1]
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension
    return img_array

def predict_image(model, img_path, class_names):
    img = load_and_preprocess(img_path)
    preds = model.predict(img)                # shape: (1, 50)
    pred_class_idx = np.argmax(preds, axis=1)[0]
    confidence = preds[0][pred_class_idx]
    pred_class_name = class_names[pred_class_idx]
    return pred_class_name, confidence

img_path = "resources/50_most_famous_places/Atomium/0a52b43208.jpg"
pred_class, confidence = predict_image(loaded_model, img_path, class_names)
print(f"Predicted class: {pred_class}, Confidence: {confidence:.2f}")