from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urljoin
from datetime import datetime
import requests
import os

from fetch_image import fetch_image


def fetch_nasa_epic_images(token):
	url = 'https://api.nasa.gov/EPIC/api/natural/images'
	payload = {'api_key': token}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	for num, answer in enumerate(response.json()):
		image = answer['image']
		date = datetime.fromisoformat(answer['date'])
		url = urljoin(
			'https://api.nasa.gov/EPIC/archive/natural/',
			'{0:%Y}/{0:%m}/{0:%d}/png/{1}.png'.format(date, image)
		)
		fetch_image(f'nasa_epic{num}.png', url, payload)


def main():
	load_dotenv()
	books_dir = 'images'
	Path(books_dir).mkdir(parents=True, exist_ok=True)
	nasa_token = os.environ['API_NASA_TOKEN']
	fetch_nasa_epic_images(nasa_token)


if __name__ == '__main__':
    main()