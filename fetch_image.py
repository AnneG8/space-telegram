import requests
import os


def fetch_image(image_name, url, payload=None, folder='images/'):
	if payload is None:
		payload = {}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	image_path = os.path.join(folder, image_name)
	with open(image_path, 'wb') as file:
		file.write(response.content)