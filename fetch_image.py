from pathlib import Path
import requests


def fetch_image(image_name, url, payload=None, folder='images'):
	response = requests.get(url, params=payload)
	response.raise_for_status()
	image_path = Path(folder, image_name) 
	with open(image_path, 'wb') as file:
		file.write(response.content)