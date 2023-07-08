from csv import writer, reader
from os import path

way_to_csv_file = path.abspath(path.join(path.dirname(__file__), './resources/eggs.csv'))


def test_create_csv_file():
    row_1 = ['Anna', 'Pavel', 'Peter']
    row_2 = ['Alex', 'Serj', 'Yana']

    with open(way_to_csv_file, 'w') as csvfile:
        csvwriter = writer(csvfile, delimiter=',')
        csvwriter.writerow(row_1)
        csvwriter.writerow(row_2)

    assert path.exists(way_to_csv_file)

    with open(way_to_csv_file, 'r') as csvfile:
        csvreader = reader(csvfile)
        assert row_1 in csvreader
        assert row_2 in csvreader
