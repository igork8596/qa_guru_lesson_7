from csv import writer, reader
from os import path as p


def test_create_csv_file(way_to_dir):
    way_to_csv_file = p.join(way_to_dir, './resources/eggs.csv')

    row_1 = ['Anna', 'Pavel', 'Peter']
    row_2 = ['Alex', 'Serj', 'Yana']

    with open(way_to_csv_file, 'w') as csvfile:
        csvwriter = writer(csvfile, delimiter=',')
        csvwriter.writerow(row_1)
        csvwriter.writerow(row_2)

    assert p.exists(way_to_csv_file)

    with open(way_to_csv_file, 'r') as csvfile:
        csvreader = reader(csvfile)
        assert row_1 in csvreader
        assert row_2 in csvreader
