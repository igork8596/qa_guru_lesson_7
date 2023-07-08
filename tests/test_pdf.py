from pypdf import PdfReader
from os import path as p


def test_pdf_file(way_to_dir):
    way_to_pdf_file = p.join(way_to_dir, './resources/docs-pytest-org-en-latest.pdf')

    reader = PdfReader(way_to_pdf_file)
    first_page_text = reader.pages[0].extract_text()

    assert p.getsize(way_to_pdf_file) == 1739253
    assert len(reader.pages) == 412
    assert first_page_text == 'pytest Documentation\nRelease 0.1\nholger krekel, trainer and consultant, https://merlinux.eu/\nJul 14, 2022'
