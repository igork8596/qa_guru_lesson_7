import os
from os import path as p
import pytest
from selene import browser as b


@pytest.fixture(scope='function', autouse=False)
def way_to_dir():
    return p.dirname(__file__)


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    b.config.base_url = 'https://github.com'
    b.config.window_width = 1440
    b.config.window_height = 2160

    yield

    b.quit()


@pytest.fixture(scope='function', autouse=False)
def tmp_management():
    way_to_tmp = p.join(p.dirname(__file__), 'tmp')

    if len(os.listdir(way_to_tmp)) != 0:
        files_list = os.listdir(way_to_tmp)
        for i in range(len(files_list)):
            os.remove(p.join(way_to_tmp, files_list[i]))

    yield

    files_list = os.listdir(way_to_tmp)
    for i in range(len(files_list)):
        os.remove(p.join(way_to_tmp, files_list[i]))


