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

config = dotenv_values("home/hema/Code/python/blog/Owren/.env")

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


def update_db(dataframe : list) -> None:
    try:
        connection = mysql.connector.connect(
            password=config.get("DB_PASSWORD"),
            user=config.get("DB_USER"),
            host=config.get("HOST"),
            database=config.get("DATABASE"),)
        
        cursor = connection.cursor()

        for data in dataframe:
            cursor.execute(f'SELECT * FROM main_posts WHERE source_id={data["post_id"]}')
            db_reposonse = cursor.fetchall()
            if not db_reposonse:
                try:
                    cursor.execute(f'INSERT INTO main_posts (title, description, source_link, body, source_id) '
                               f'VALUES (\'{data["title"]}\','
                               f'\'{data["meta_description"]}\','
                               f'\'{data["link"]}\',' 
                               f'\'{data["body"]}\','
                               f'\'{data["post_id"]}\')')
                    connection.commit()
                    print("Inserted New Posts To Database")
                except NameError as n:
                    raise n("Unable to insert data to database")                    

    except Error as e:
        print(e)
        print("Unable to connect to database")

def main():
    try:
        print("Starting To Parse")
        posts_parsed = parse_posts()
        article=get_article(posts_parsed)
        update_db(article)
        print("Finished")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
    sleep(3)