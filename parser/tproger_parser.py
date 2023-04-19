import random
import string
from datetime import datetime
from typing import Any, Union

import feedparser
import pandas as pd
from loguru import logger
from newspaper import Article
from slugify import slugify
from utils import (TPROGER_DIR, author_profile, check_duplication_title,
                   connect_to_db, download_multiple_images, download_title_img,
                   remove_unwanted)

FILE_NAME = str(TPROGER_DIR + "tproger_data" + datetime.now().strftime("%m-%d_%H:%M") + ".csv")


def parse_posts() -> list:
    try:
        rss_data = feedparser.parse('https://tproger.ru/rss/')
        posts_count = len(rss_data.entries)
        posts_parsed = []

        for post in range(posts_count):
            post_content = rss_data.entries[post]
            post_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))

            post_parsed: dict[str, Union[str, Any]] = {
                'post_id': post_id,
                'title': post_content.title,
                'link': post_content.link,
            }
            posts_parsed.append(post_parsed)

        logger.info(f"Start parsing {post_parsed['post_id']} was succesfully")
        return posts_parsed

    except Exception as e:
        logger.error("Unable to get RSS info from  tproger.ru {e}")
        print(e)


def get_everything(post_parsed: list) -> None:
    try:
        data_parsed = []
        logger.info("Parsing articles")

        for post in post_parsed:
            article = Article(post['link'])
            article.download()
            article.parse()
            images = ['' + img for img in article.images]

            data = {
                'post_id': post['post_id'],
                'title': post['title'],
                'body': article.text,
                'source_link': article.url,
                'image': article.top_image,
                'images': images,
            }
            data_parsed.append(data)

        dataframe = pd.DataFrame(data_parsed)
        dataframe.to_csv(FILE_NAME, sep="'", header=True, index=True)
        logger.success(f"Successfully saved articles in {FILE_NAME}")
        return data_parsed

    except NameError as n:
        logger.error(f"Unable to get more info from URLs {n}")
        raise n("Unable to get more info from URLs ")


def update_db(data_parsed):
    logger.info("Connecting to database and updating")
    connection, cursor = connect_to_db()
    logger.info(f"DB connection is {cursor}")
    author = author_profile()

    for data in data_parsed:
        check_duplication = check_duplication_title(data['title'])

        if check_duplication is False:
            try:
                body_text = remove_unwanted(data['body'])
                slug = slugify(data['title'])
                title_img = download_title_img(data['image'], data['post_id'])
                download_multiple_images(data['images'], data['post_id'])
                query = f"INSERT INTO main_post (title, slug, source_link, source_id, body, title_image, published, author_id)" \
                        f'VALUES ("{data["title"]}", "{slug}", "{data["source_link"]}", "{data["post_id"]}", "{body_text}", "{title_img}", "0", "{author}")'
                cursor.execute(query)
                connection.commit()
                print(f"Post {data['title']} added to database")
                logger.success(f"Post {data['title']} added to database")

            except NameError as n:
                logger.error(f"Some error occured in {data['title']}")
                raise n(f"Unable to update db. Problem in {data['title']}")


def main():
    logger.add('../logs/tproger_parser.log', format='{time} __|__ {level} __|__ {message}', level='INFO', rotation='100 MB', compression='zip')

    try:
        posts_parsed = parse_posts()
        data_parsed = get_everything(posts_parsed)
        update_db(data_parsed)

        logger.success("Successfully finished")

    except Exception as e:
        logger.error("Unable to parse tproger.ru", 'Could not Connect To Dev')
        print(e)


if __name__ == "__main__":
    main()
