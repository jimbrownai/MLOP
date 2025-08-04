import tensorflow as tf 
from config import EPOCHS, CHECKPOINT_PATH, LOG_DIR

def get_callbacks():
    tensorboard_cb = tf.keras.callbacks.TensorBoard(log_dir=LOG_DIR,histogram_freq=1)
    return [
        tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
        tf.keras.callbacks.ModelCheckpoint(CHECKPOINT_PATH,save_best_only=True),
        tensorboard_cb
    ]

def train_model(model, train_ds,val_ds, callbacks=None):
    history = model.fit(
        train_ds,
        validation_data = val_ds,
        epochs = EPOCHS,
        callbacks = callbacks
    )
    return history