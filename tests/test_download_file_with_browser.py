import os
from selenium import webdriver
from selene import browser as b
from os import path as p
import time


def test_download_file_with_browser(way_to_dir, tmp_management):
    way_for_uploaded_file = p.join(way_to_dir, 'tmp')

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": way_for_uploaded_file,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    b.config.driver_options = options

    b.open('/pytest-dev/pytest')
    b.element(".d-none .Button-label").click()
    b.element('[data-open-app="link"]').click()

    timeout = round(time.time()) + 10
    while time.time() <= timeout:
        if p.exists(p.join(way_for_uploaded_file,'pytest-main.zip')):
            break
        else:
            continue

    assert p.exists(p.join(way_for_uploaded_file, 'pytest-main.zip'))
    assert p.getsize(p.join(way_for_uploaded_file, 'pytest-main.zip')) == 1582717