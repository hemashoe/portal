import re
from datetime import datetime
from time import sleep
from typing import Any, Dict, Union

import feedparser
import mysql.connector
import pandas as pd
from dotenv import dotenv_values
from loguru import logger
from mysql.connector import Error
from newspaper import Article

config = dotenv_values(".env")

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
            article_images.append(article.images)
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
            print(dataframe)
        dataframe.to_csv("habr_data"+ datetime.now().strftime('%Y-%m-%d_%H:%M') + ".csv", sep="'", header=True, index=True,index_label="post_id" )
        return dataframe

    except:
        print("Unable to get article")


def update_db(posts_parsed : list) -> None:
    try:
        connection = mysql.connector.connect(dbname=config.get("DATABASE"),
                              user=config.get("DB_USER"),
                              password=config.get("DB_PASSWORD"),
                              host="db")
        cursor = connection.cursor()

    except Error as e:
        print(e)
        print("Unable to connect to database")

def main():
    try:
        print("Starting To Parse")
        posts_parsed = parse_posts()
        get_article(posts_parsed)
        print("Finished")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
    sleep(3)