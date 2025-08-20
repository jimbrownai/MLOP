from s3_dataloader import download_s3_folder
from dataloader import load_datasets 
from datapreprocess import preprocess_dataset 
from model_builder import build_model
from trainer import get_callbacks,train_model_head,train_fine_tune
from utils import plot_history
from config import MODEL_SAVE_PATH,MOBNET_URL,BUCKET,PREFIX,LOCAL_DIR

def main():

    download_s3_folder(BUCKET,PREFIX,LOCAL_DIR)

    train_ds,val_ds,class_names = load_datasets()

    train_ds,val_ds = preprocess_dataset(train_ds=train_ds,val_ds=val_ds)

    mobnet_model = build_model(MOBNET_URL,len(class_names))
    callbacks = get_callbacks()

    history_head = train_model_head(mobnet_model,train_ds,val_ds,callbacks)
    # history_fine_tune = train_fine_tune(mobnet_model,train_ds,val_ds,callbacks)
    mobnet_model.save(MODEL_SAVE_PATH)
    plot_history(history_head)

if __name__ == "__main__":
    main()









