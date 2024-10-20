import os

import requests


def download(url, file_output):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(file_output, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 2):
                file.write(chunk)
        return os.path.getsize(file_output)
    except Exception as err:
        print(f'Ошибка при скачивании файла {url}:\n{err}')
    return 0


def info_url(url):
    try:
        response = requests.head(url)
        response.raise_for_status()
        file_info = {'url': url,
                     'status_code': response.status_code,
                     'content_type': response.headers.get('Content-Type'),
                     'content_length': response.headers.get('Content-Length'),
                     'last_modified': response.headers.get('Last-Modified')}
        return file_info
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None


def size_url(url):
    try:
        response = requests.head(url)
        response.raise_for_status()
        return int(response.headers.get('Content-Length'))
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None


url = 'https://icdn.lenta.ru/images/2024/10/20/09/20241020092401960/owl_detail_620_f013e963dd6b76faa71d4c30f3399634.jpg'
print(f'Информация о файле: {info_url(url)}')
print(f'Размер файла: {round(size_url(url) / 1024, 2)} Кб')
file = 'pic from lenta.jpg'
if download(url, file):
    print(f"Файл '{file}' скачан в текущую папку")
