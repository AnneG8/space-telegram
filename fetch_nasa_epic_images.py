from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urljoin
import requests
import re

from fetch_image import fetch_image


def fetch_nasa_epic_images(token):
	url = 'https://api.nasa.gov/EPIC/api/natural/images'
	payload = {'api_key': token}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	for num, answer in enumerate(response.json()):
		image = answer['image']
		date = re.split('-| ', answer['date'])
		url = urljoin(
			'https://api.nasa.gov/EPIC/archive/natural/',
			f'{date[0]}/{date[1]}/{date[2]}/png/{image}.png'
		)
		fetch_image(f'nasa_epic{num}.png', url, payload)


def main():
	load_dotenv()
	books_dir = 'images'
	Path(books_dir).mkdir(parents=True, exist_ok=True)
	nasa_token = os.getenv('API_NASA_TOKEN')
	fetch_nasa_epic_images(nasa_token)


if __name__ == '__main__':
    main()