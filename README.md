# Автопубликация фотографий в Telegram-канале

Праграмма публикует изображения, сохраненные локально, в Telegram-канал. По одной, с определенным промежутком. 
Изображения можно загрузить самостоятельно, или воспользоваться помощью программы - она скачает фотографии космической тематики от SpaceX и NASA.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ = значение`. 

Для публикации изображений в канал:
- `TELEGRAM_TOKEN` — API-токен Telegram-бота, можно получить при [регистрации](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html).
- `CHAT_ID` — имя Telegram-канала (начинается с `@`). Например, `@sameplaceinspace`.

Для скачивания изображений от NASA (используя файлы `main.py`, `fetch_nasa_apod_images.py` или `fetch_nasa_epic_images.py`):
- `API_NASA_TOKEN` — API-токен NASA, получить можно [здесь](https://api.nasa.gov/).

### Аргументы

1) Для файла `telegram_bot.py`:
- `-hr` (`--hours`) — промежуток между отправкой изображений, измеряется в часах (по-умолчанию равен 4).
- `-d` (`--dir`) — директория, из которой брать фотографии для публикации (по-умолчанию `images`).

2) Для файла `fetch_spacex_images.py`:
- -`id` — позволяет скачать фото с запуска с соответствующим ID (по-умолчанию качает фото с последнего запуска).
**Внимание!** Иногда по-умолчанию может не оказаться фотографий.

### Запуск

Для автоматизации публикации изображений в Telegram-канале необходимо предварительно иметь Telegram-канал, [создать Telegram-бот](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html) и иметь сохраненные локально фотографии.

Запустите основную программу командой

```bash
$ python telegram_bot.py -hr HOURS -d DIR
```

> Об аргументах смотрите в соответствующем разделе.

В случае, отсутствия изображений в указанной папке или самой папки, программа выдаст ошибку.

**Дополнительно** Можно удалять файлы из папки с изображениями не прерывая программу. Ошибки не будет. 
**Дополнительно** Можно докладывать новые изображения в папку, не перезагружая программу. Отправив все имеющиеся при запуске фотографии 1 раз, программа проверит документы в папке повторно.

Если нет желания искать изображения самостоятельно, можно воспользоваться одним из имеющихся скриптов:

Скачать фотографии запуска SpaceX:
```bash
$ python fetch_spacex_images.py -id ID
```
> Об аргументе смотрите в соответствующем разделе.

Скачать фотографии NASA APOD (Astronomy Picture of the Day):
```bash
$ python fetch_nasa_apod_images.py 
```

Скачать фотографии NASA EPIC (Earth Polychromatic Imaging Camera):
```bash
$ python fetch_nasa_epic_images.py 
```

Или отовсюду сразу:
```bash
$ python main.py 
```

**Внимание!** Скачивание файлов происходит в директорию по-умолчанию `images`, возможность задать свою директорию отсутствует.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).