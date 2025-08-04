import tensorflow as tf 
from config import IMG_SIZE, BATCH_SIZE, VALIDATION_SPLIT, SEED

def load_datasets(data_dir='dataset/'):
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split = VALIDATION_SPLIT,
        subset = 'training',
        seed = SEED,
        image_size = IMG_SIZE,
        batch_size = BATCH_SIZE
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split = VALIDATION_SPLIT,
        subset = 'validation',
        seed = SEED,
        image_size = IMG_SIZE,
        batch_size = BATCH_SIZE
    )
    class_names = train_ds.class_names
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    
    return train_ds,val_ds,class_names