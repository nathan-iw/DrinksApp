import unittest.mock
from unittest.mock import Mock, patch
import src.drinks.Drink as d
# import app
# from app import App
from src.ETL.persistence import Database

class PersonTests(unittest.TestCase):

    @patch("builtins.input")
    def test_milk(self, input_details):
        # arrange
        input_details.side_effect = [1]
        expected = "extra milk"
        # act
        actual = d.milk_sugar()

        # assert
        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_sugar(self, input_details):
        # arrange
        input_details.side_effect = [2]
        expected = "with sugar"
        # act
        actual = d.milk_sugar()

        # assert
        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_straight_up(self, input_details):
        # arrange
        input_details.side_effect = [3]
        expected = "-"
        # act
        actual = d.milk_sugar()

        # assert
        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_size_large(self, input_details):
        # arrange
        input_details.side_effect = [1]
        expected = "large"
        # act
        actual = d.size()

        # assert
        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_size_small(self, input_details):
        # arrange
        input_details.side_effect = [2]
        expected = "small"
        # act
        actual = d.size()

        # assert
        self.assertEqual(expected, actual)


