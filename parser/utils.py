import os
import urllib.request
import re
from pathlib import Path

import mysql.connector
import emoji
from dotenv import find_dotenv, load_dotenv

config = load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = os.path.join(BASE_DIR, 'parser/habr_csv/')
MEDIA_STORE = os.path.join(str(BASE_DIR), 'media/post/')


def connect_to_db():
    connection = mysql.connector.connect(
                database=os.environ["DATABASE"],
                host=os.environ["DB_HOST"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"])

    cursor = connection.cursor()

    return connection, cursor


def remove_unwanted(text) -> str:
    prepared_text = []
    
    text = emoji.demojize(text)
    text = text.encode('utf-8', 'ignore').decode('utf-8')
    prepared_text.append(text)

    return prepared_text


def download_img(img_url, post_id) -> str:
    path = os.path.join(MEDIA_STORE,(post_id))
    Path(path).mkdir(parents=True, exist_ok=True)
    image = urllib.request.urlretrieve(str(img_url), os.path.join(str(path),str(img_url.split("/")[-1])))

    return image[0]


def download_title_img(img_url, post_id) -> str:
    try:
        path = os.path.join(MEDIA_STORE,(post_id))
        Path(path).mkdir(parents=True, exist_ok=True)
        image = urllib.request.urlretrieve(str(img_url), os.path.join(str(path),str(img_url.split("/")[-1])))
        img_db_name = image[0].split("/")[-3:]
        name = os.path.join(img_db_name[0], img_db_name[1], img_db_name[2])

        return name

    except Exception:

        name = ''
        
        return name


def download_multiple_images(images : list, post_id : str):
    for image in images: 
        downloaded = download_img(str(image), post_id)

        if downloaded:
            msg = f"Image {image} downloaded"

        else:
            msg = f"Image {image} not downloaded"
        
        return msg


def check_duplication(post_id):
    try:
        connection, cursor = connect_to_db()
        query = f"SELECT source_id FROM main_post WHERE source_id='{post_id}'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 0:
            return False
        else:
            return True

    except mysql.connector.Error as err:
        print(err)


def author_profile():
    author = "nicko_b"
    try:
        connection, cursor = connect_to_db()
        query = f"SELECT id FROM main_profile WHERE user='{author}'"
        cursor.execute(query)
        result = cursor.fetchall()

        return result[0][0]

    except NameError as n:
        n("No Profile Nicko_B")