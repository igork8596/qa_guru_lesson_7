import os
from os import path as p
import requests


def test_download_file_with_requests(way_to_dir, tmp_management):
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    path_to_file = p.join(way_to_dir, './tmp/selenium_logo.png')
    response = requests.get(url)

    with open(path_to_file, 'wb') as file:
        file.write(response.content)

    assert p.exists(path_to_file)
    assert p.getsize(path_to_file) == 30803