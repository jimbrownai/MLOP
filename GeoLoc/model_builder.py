import tf_keras as keras
import tensorflow_hub as hub
from config import MOBNET_URL,IMG_SIZE,NUM_CLASSES



def build_model(url,num_classes):
    feature_extractor_layer = hub.KerasLayer(
        url,
        trainable=False,       # freeze initially
        input_shape=IMG_SIZE + (3,)
    )
    mobnet_model = keras.Sequential([
        feature_extractor_layer,
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(num_classes, activation='softmax')
    ])

    mobnet_model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-4),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    # mobnet_model.summary()
    return mobnet_model
