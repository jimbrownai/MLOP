import tf_keras as keras
from config import EPOCHS_HEAD,CHECKPOINT_PATH

def get_callbacks():
    callback_list = [
        keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
        keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2)
    ]
    return callback_list

def train_model_head(model,train_ds,val_ds,callbacks=None):
    history_head = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS_HEAD,
        callbacks=callbacks
    )
    return history_head

def train_fine_tune(model,train_ds,val_ds,callbacks=None):

    feature_extractor = model.get_layer("keras_layer")
    feature_extractor.trainable = True
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-5),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    # model.summary()

    cbs = [
        keras.callbacks.ModelCheckpoint(
            filepath=CHECKPOINT_PATH,
            monitor="val_accuracy",
            mode="max",
            save_best_only=True
        ),
        keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss", factor=0.5, patience=2, verbose=1, min_lr=1e-6
        ),
        keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=5, restore_best_weights=True, verbose=1
        )
    ]

    history_ft = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=30,           # a ceiling, not a target
        callbacks=cbs
    )
    return history_ft

