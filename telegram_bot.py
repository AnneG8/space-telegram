from dotenv import load_dotenv
from pathlib import Path
import telegram
import os
import argparse
import random
import time


def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-hr', '--hours',
		type=float,
		default=4, const=4, 
		nargs='?'
	)
	parser.add_argument(
		'-d', '--dir',
		type=str,
		default='images', const='images', 
		nargs='?'
	)
	return parser


def is_dir_valid(images_dir):
	path = Path(images_dir)
	if not (path.exists() and path.is_dir()):
		print(f'Отсутствует папка {images_dir}')
		return False
	if not next(os.scandir(images_dir), None):
		print(f'В папке {images_dir} отсутствуют файлы')
		return False
	return True


def get_images_for_dir(images_dir):
	images = list()
	for address, dirs, files in os.walk(images_dir):
		for name in files:
			images.append(os.path.join(address, name))
	return images


def post_image(image, token, chat_id):
	bot = telegram.Bot(token=token)
	with open(image, 'rb') as file:
		bot.send_photo(chat_id=chat_id, photo=file)


def main():
	load_dotenv()
	telegram_token = os.environ['TELEGRAM_TOKEN']
	chat_id = os.environ['TG_CHAT_ID']

	parser = create_parser()
	args = parser.parse_args()

	period = args.hours
	images_dir = args.dir
	if not is_dir_valid(images_dir):
		return

	while True:
		images = get_images_for_dir(images_dir)
		random.shuffle(images)
		for image in images:
			path = Path(image)
			if not (path.exists() and path.is_file()):
				continue
			while True:
				try:
					post_image(image, telegram_token, chat_id)
					time.sleep(period * 3600)
					break
				except telegram.error.NetworkError:
					time.sleep(3)


if __name__ == '__main__':
    main()