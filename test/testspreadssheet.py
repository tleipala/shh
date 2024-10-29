from unittest import TestCase
from spreadsheet import SpreadSheet

class TestSpreadsSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "A2")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

