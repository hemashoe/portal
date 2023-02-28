import re
import urllib.request
from datetime import datetime
from time import sleep
from typing import Any, Union
import mysql.connector
from django.template.defaultfilters import slugify
import feedparser
from cleantext import clean
import pandas as pd
from loguru import logger
from newspaper import Article

from utils import remove_unwanted


def parse_posts() -> list:
    try:
        rss_data = feedparser.parse('https://habr.com/ru/rss/all/all/?fl=ru')
        posts_count = len(rss_data.entries)
        posts_parsed = []

        for post in range(posts_count):
            post_content = rss_data.entries[post]
            post_id = re.search(r'post/(\d+)/', post_content.guid).group(1)

            post_parsed: dict[str, Union[str, Any]] = {
                'post_id': post_id,
                'title': post_content.title,
                'link': post_content.guid,
            }
            posts_parsed.append(post_parsed)
        return posts_parsed

    except Exception:
        print("Unable to parse habr.com")

def get_article(posts_parsed : list ) -> None:
    try:
        data_parsed = []
        article_images = []

        for post in posts_parsed:
            article =Article(post['link'])
            article.download()
            article.parse()
            for img in article.images:
                images = "" + img    
            article_images.append(images)
            post_id = re.search(r'post/(\d+)/', post['link']).group(1)

            data = {
                    'post_id': post_id,
                    'title': article.title,
                    'meta_description': article.meta_description,
                    'link': article.url,
                    'body': article.text,
                    'image': article.top_image,
                    'images': article_images,
                }
            data_parsed.append(data)
            dataframe = pd.DataFrame(data_parsed)
        datafile_name = "habr_data" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
        dataframe.to_csv(datafile_name, sep="'", header=True, index=True,index_label="post_id" )

        return data_parsed

    except:
        print("Unable to get article")


def update_db(data_parsed):
    connection = mysql.connector.connect(
                database=("Owren"),
                host=("localhost"),
                user=("hema"),
                password=("P@ssw0rd"))
        
    cursor = connection.cursor()

    cursor.execute("SELECT id from main_profile WHERE user='nicko_b'")
    author = cursor.fetchall()
    print(author[0][0])

    for data in data_parsed:
        cursor.execute(f"SELECT * FROM main_post WHERE source_id={data['post_id']}")
        db_response = cursor.fetchall()

        if len(db_response) == 0:
            try:
                body_text = remove_unwanted(data['body'])
                description_text = remove_unwanted(data['meta_description'])

                cursor.execute("INSERT INTO main_post (title, slug ,description, source_link, source_id, author_id, body, title_image)" 
                            'VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")' % (data['title'], slugify(data['title']), description_text, data['link'], data['post_id'], author[0][0], body_text, data['image']))             

                connection.commit()
                print("Success")

            except NameError as n:
                raise n("Unable to update db")

def main():
    try:
        print("Starting To Parse")
        posts_parsed = parse_posts()
        data_parsed=get_article(posts_parsed)
        update_db(data_parsed)
        print("Finished")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
    sleep(3)