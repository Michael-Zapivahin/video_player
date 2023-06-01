import os
import time



def main():
    # load_dotenv()
    books_dir = os.getenv('BOOKS_DIR', default='books')
    os.makedirs(books_dir, exist_ok=True)
    images_dir = os.getenv('IMAGES_DIR', default='images')
    os.makedirs(images_dir, exist_ok=True)
    comments_dir = os.getenv('COMMENTS_DIR', default='comments')
    os.makedirs(comments_dir, exist_ok=True)




if __name__ == '__main__':
    main()
