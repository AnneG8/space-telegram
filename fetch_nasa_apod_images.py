from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote
import requests
import os

from fetch_image import fetch_image


def get_file_extension(url):
    filename = urlsplit(unquote(url)).path.split("/")[-1]
    return os.path.splitext(filename)[1]


def fetch_nasa_apod_images(token, count=20):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': token,
        'count': count,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for num, answer in enumerate(response.json()):
        ext = get_file_extension(answer['url'])
        if ext:
            fetch_image(f'nasa_apod{num}{ext}', answer['url'])


def main():
    load_dotenv()
    books_dir = 'images'
    Path(books_dir).mkdir(parents=True, exist_ok=True)
    nasa_token = os.environ['API_NASA_TOKEN']
    fetch_nasa_apod_images(nasa_token)


if __name__ == '__main__':
    main()
