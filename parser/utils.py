import os
import urllib.request
from pathlib import Path

import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

config = load_dotenv("/home/hema/main/Owren/.env")

BASE_DIR = Path(__file__).resolve().parent.parent
HABR_DIR = os.path.join(BASE_DIR, "parser/habr_csv/")
TPROGER_DIR = os.path.join(BASE_DIR, "parser/tproger_csv/")
MEDIA_STORE = os.path.join(str(BASE_DIR), "media/post/")


def connect_to_db():
    connection = None
    try:
        connection = psycopg2.connect(
            database=os.environ.get("DATABASE"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
        )
    except OperationalError as e:
        print(f"The error '{e}' occurred")

    return connection


def remove_unwanted(text) -> str:
    text = "".join(text)
    text = text.replace('"', "'")

    return str(text)


def download_img(img_url, post_id) -> str:
    path = os.path.join(MEDIA_STORE, (post_id))
    Path(path).mkdir(parents=True, exist_ok=True)
    try:
        image = urllib.request.urlretrieve(
            str(img_url), os.path.join(str(path), str(img_url.split("/")[-1]))
        )

        return image[0]
    except Exception:
        image = ""

        return image


def download_title_img(img_url, post_id) -> str:
    try:
        path = os.path.join(MEDIA_STORE, (post_id))
        Path(path).mkdir(parents=True, exist_ok=True)
        image = urllib.request.urlretrieve(
            str(img_url), os.path.join(str(path), str(img_url.split("/")[-1]))
        )
        img_db_name = image[0].split("/")[-3:]
        name = os.path.join(img_db_name[0], img_db_name[1], img_db_name[2])
        return name

    except Exception:
        name = ""

        return name


def download_multiple_images(images: list, post_id: str):
    for image in images:
        downloaded = download_img(str(image), post_id)
        if downloaded:
            msg = f"Image {image} downloaded"
        else:
            msg = ""

        return msg


def check_duplication(post_id):
    try:
        connection, cursor = connect_to_db()
        query = f"SELECT source_id FROM public.main_post WHERE source_id='{post_id}'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 0:
            return False
        else:
            return True

    except OperationalError as err:
        print(err)


def check_duplication_title(title):
    try:
        connection, cursor = connect_to_db()
        query = f"SELECT title FROM public.main_post WHERE title='{title}'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 0:
            return False
        else:
            return True

    except OperationalError as err:
        print(err)


def author_profile():
    author = "nicko_b"
    try:
        connection, cursor = connect_to_db()
        query = f"SELECT id FROM public.main_profile WHERE user='{author}'"
        cursor.execute(query)
        result = cursor.fetchone()

        return result

    except NameError as n:
        n("No Profile Nicko_B")
