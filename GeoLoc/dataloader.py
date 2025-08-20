import tensorflow as tf
import os
import tensorflow_hub as hub

from config import IMG_SIZE,BATCH_SIZE,VALIDATION_SPLIT,SEED,LOCAL_DIR

data_dir = LOCAL_DIR

def load_datasets(data_dir="train/"):

    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=VALIDATION_SPLIT,   # 80% train, 20% val
        subset="training",
        seed=SEED,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=VALIDATION_SPLIT,
        subset="validation",
        seed=SEED,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )
    class_names = train_ds.class_names
    return train_ds,val_ds,class_names

