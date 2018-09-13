import unittest
from core.exceltomarkdown import write_table, get_longest_values_by_column, generate_tables_from_excel_file


class TestExcelToMarkdownTables(unittest.TestCase):

    def test_get_longest_values_by_columns(self):
        lines = [
            ['A', 'B', 'C'],
            ['1', '300', '5'],
            ['Hello', '4', 'Lorem ipsum'],
        ]
        v = get_longest_values_by_column(lines)
        self.assertEqual({0: 'Hello', 1: '300', 2: 'Lorem ipsum'}, v)

    def test_write_table(self):
        lines = [
            ['A', 'B', 'C'],
            ['1', '300', '5'],
            ['Hello', '4', 'Lorem ipsum'],
        ]
        table = write_table(lines)
        self.assertEqual("""| A     | B   | C           |
| ----- | --- | ----------- |
| 1     | 300 | 5           |
| Hello | 4   | Lorem ipsum |""", table)
