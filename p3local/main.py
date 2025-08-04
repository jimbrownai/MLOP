from data_loader import load_datasets
from model_builder import build_model
from trainer import train_model,get_callbacks
from utils import plot_history
from config import MODEL_SAVE_PATH

def main():
    train_ds, val_ds, class_names = load_datasets()
    model = build_model(num_classes=len(class_names))
    callbacks = get_callbacks()

    history = train_model(model,train_ds,val_ds,callbacks)
    model.save(MODEL_SAVE_PATH)
    plot_history(history)

if __name__ == '__main__':
    main()