import re
import urllib.request
from datetime import datetime
from time import sleep
from typing import Any, Union
from django.template.defaultfilters import slugify
import feedparser
from cleantext import clean, fix_bad_unicode
import pandas as pd
from loguru import logger
from newspaper import Article




def remove_unwanted(text) -> str:
    text = clean(text, fix_unicode=True, no_emoji=True)
    text = fix_bad_unicode(text)

    return text


def download_title_img(img_url) -> str:
    image = urllib.request.urlretrieve(str(img_url), "")
    

    return image
    
def download_multiple_images(images) -> str or list:
    images_downloaded = []
    for image in images:
        image_downloaded = download_title_img(image)
        images_downloaded.append(image_downloaded)
    return images_downloaded