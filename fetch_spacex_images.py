import argparse
import requests
from pathlib import Path
from urllib.parse import urljoin
from fetch_image import fetch_image


def fetch_spacex_launch(launch_id=''):
    base_url = 'https://api.spacexdata.com/v5/launches/'
    if launch_id:
        launch_id = 'latest'
    url = urljoin(base_url, launch_id)
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    for image_num, image_url in enumerate(images):
        fetch_image(f'spacex{image_num}.jpg', image_url)


def main():
    books_dir = 'images'
    Path(books_dir).mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-id',
        type=str,
        default='', const='',
        nargs='?'
    )
    args = parser.parse_args()
    fetch_spacex_launch(args.id)


if __name__ == '__main__':
    main()
