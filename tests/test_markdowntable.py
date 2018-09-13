import unittest
from core.markdowntable import (get_headers_from_lines,
                                generate_table_of_contents,
                                generate_index,
                                Header)


class TestMarkdownTable(unittest.TestCase):

    def test_reading_headers(self):
        lines = [
            '# One',
            '* Something',
            '* Something',
            '* Something',
            '* Something',
            '## One one',
            'Hello World',
            '### One one one',
            'Hello World',
            '# Two',
            'Hello World',
            '* Something',
            '* Something',
            '## Two one',
            'Hello World',
            '### Two one one',
            'Hello World',
            '### Two one two',
            '### Two two',
        ]

        headers = get_headers_from_lines(lines)

        self.assertEqual(8, len(headers))

    def test_table_of_contents(self):
        headers = [
            Header(1, 'Lorem'),
            Header(2, 'Ipsum'),
            Header(2, 'Dolor'),
            Header(1, 'Sit amet consectetur'),
            Header(2, 'AAA'),
            Header(3, 'AAA A'),
            Header(3, 'AAA B')
        ]

        table = generate_table_of_contents(headers, separator=' ', indent=2)
        self.assertEqual("""<b>1. [Lorem](#lorem)</b><br/>
   1.1 [Ipsum](#ipsum)<br/>
   1.2 [Dolor](#dolor)<br/>
<b>2. [Sit amet consectetur](#sit-amet-consectetur)</b><br/>
   2.1 [AAA](#aaa)<br/>
     2.1.1 [AAA A](#aaa-a)<br/>
     2.1.2 [AAA B](#aaa-b)<br/>""", table)

    def test_generating_table(self):
        headers = [
            Header(1, 'Lorem'),
            Header(2, 'Ipsum'),
            Header(2, 'Dolor'),
            Header(1, 'Sit amet consectetur')
        ]

        table = generate_index(headers)
        self.assertEqual("""1. [Lorem](#lorem)
    1. [Ipsum](#ipsum)
    1. [Dolor](#dolor)
1. [Sit amet consectetur](#sit-amet-consectetur)""", table)

    def test_generating_table_with_special_characters(self):
        headers = [
            Header(1, 'Sit, amet: consectetur')
        ]

        table = generate_index(headers)
        self.assertEqual("1. [Sit, amet: consectetur](#sit%2c-amet%3a-consectetur)", table)
