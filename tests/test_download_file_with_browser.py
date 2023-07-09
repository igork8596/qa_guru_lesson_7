import os
from selenium import webdriver
from selene import browser as b
from os import path as p


def test_download_file_from_browser(way_to_dir, tmp_management):
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

    while True:
        if 'pytest-main.zip' in os.listdir(way_for_uploaded_file):
            break
        else:
            continue

    assert p.exists(p.join(way_for_uploaded_file, 'pytest-main.zip'))
    assert p.getsize(way_for_uploaded_file) == 4096