from pathlib import Path
from dotenv import load_dotenv
import os

from fetch_spacex_images import fetch_spacex_launch
from fetch_nasa_apod_images import fetch_nasa_apod_images
from fetch_nasa_epic_images import fetch_nasa_epic_images


def main():
	load_dotenv()
	images_dir = 'images'
	Path(images_dir).mkdir(parents=True, exist_ok=True)
	fetch_spacex_launch()
	nasa_token = os.getenv('API_NASA_TOKEN')
	fetch_nasa_apod_images(nasa_token)
	fetch_nasa_epic_images(nasa_token)
	

if __name__ == '__main__':
    main()
		