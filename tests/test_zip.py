import os
from zipfile import ZipFile
from os import path as p


def test_zip_file(way_to_dir, tmp_management):
    way_to_zip_file = p.join(way_to_dir, 'tmp')
    way_to_res = p.join(way_to_dir, 'resources')

    with ZipFile(p.join(way_to_zip_file, 'test_zip_file'), mode='w') as zip_file:
        for file in os.listdir(p.join(way_to_dir, 'resources')):
            zip_file.write(p.join(way_to_res, file))

    with ZipFile(p.join(way_to_zip_file, 'test_zip_file'), mode='r') as zip_file:
        for i in range(len(zip_file.namelist())):
            assert p.basename(zip_file.namelist()[i]) in os.listdir(way_to_res)
