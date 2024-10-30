from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadsSheet(TestCase):

    #GA14-TDD does not work??

    #story1

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "A2")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1,5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

        #story 2

    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "Apple")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

        #story 3

    def test_formula_evaluate_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_formula_evaluate_non_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=5")
        self.assertEqual(5, spreadsheet.evaluate("A1"))

    def test_formula_evaluate_invalid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

        #story 4

    def test_simple_formulas_with_references(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B2")
        spreadsheet.set("B2", "42")
        self.assertEqual(42, spreadsheet.evaluate("A1"))

    def test_simple_formulas_with_references_error(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B2")
        spreadsheet.set("B2", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

        #story 5

    def test_formula_with_arithmetic_operator(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3")
        spreadsheet.set("=1+3", "4")
        self.assertEqual(4, spreadsheet.evaluate("A1"))

    def test_formula_with_arithmetic_operator_error(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_formula_with_arithmetic_operator_error2(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1/0")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))


















