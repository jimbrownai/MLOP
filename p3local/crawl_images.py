import os
from PIL import Image
from PIL import Image, UnidentifiedImageError
from icrawler.builtin import GoogleImageCrawler

def download_images(keyword, dir_name, max_num=100):
    crawler = GoogleImageCrawler(storage={'root_dir': f'dataset/{dir_name}'})
    crawler.crawl(keyword=keyword, max_num=max_num)



def clean_folder(folder_path):
    supported_exts = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Check extension
            if not file.lower().endswith(supported_exts):
                print(f"🗑️ Removing unsupported file format: {file_path}")
                os.remove(file_path)
                continue
            # Check if it's a valid image
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Check for corruption
            except (UnidentifiedImageError, IOError, SyntaxError):
                print(f"Removing unreadable/corrupt image: {file_path}")
                os.remove(file_path)


def main():
    
    download_images('beach landscape', 'beach', max_num=15)
    download_images('snowy mountains', 'mountains', max_num=15)
    download_images('dense forest', 'forest', max_num=15)
    download_images('city skyline', 'city', max_num=15)
    
    clean_folder("dataset/")

if __name__ == '__main__' :
    main()