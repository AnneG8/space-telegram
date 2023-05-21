from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote, urljoin
import requests
import os
import pprint
import re


def get_file_extension(url):
	filename = urlsplit(unquote(url)).path.split("/")[-1]
	return os.path.splitext(filename)[1]


def fetch_image(image_name, url, payload={}, folder='images/'):
	response = requests.get(url, params=payload)
	response.raise_for_status()
	image_path = os.path.join(folder, image_name)
	with open(image_path, 'wb') as file:
		file.write(response.content)


def fetch_spacex_last_launch():
	url = 'https://api.spacexdata.com/v5/launches/latest'
	response = requests.get(url)
	response.raise_for_status()
	images = response.json()['links']['flickr']['original']
	for image_num, image_url in enumerate(images):
		fetch_image(f'spacex{image_num}.jpg', image_url)


def fetch_nasa_apod_images(token):
	url = 'https://api.nasa.gov/planetary/apod'
	payload = {
		'api_key': token,
		'count': 20,
	}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	#image_urls = [answer['url'] for answer in response.json()]
	for num, answer  in enumerate(response.json()):
		ext = get_file_extension(answer['url'])
		if ext:
			fetch_image(f'nasa_apod{num}{ext}', answer['url'])


def fetch_nasa_epic_images(token):
	url = 'https://api.nasa.gov/EPIC/api/natural/images'
	#url = 'https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png'
	payload = {'api_key': token}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	#pprint.pprint(response.json())
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
	#fetch_spacex_last_launch()
	nasa_token = os.getenv('API_NASA_TOKEN')
	#fetch_nasa_apod_images(nasa_token)
	fetch_nasa_epic_images(nasa_token)
	
	


if __name__ == '__main__':
    main()
