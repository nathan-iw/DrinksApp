import unittest.mock
from unittest.mock import Mock, patch
import app
import src.drinks.Drink as d
import src.round.Round as r
import src.ETL.Person as p
from src.ETL.persistence import Database

class RoundTests(unittest.TestCase):
    print("Round tests running...")

    def test_unique(self):
        # arrange
        TestDrink = d.Drink("Test Type","Test Name","Test Details","Test Price")
        test_list = [TestDrink, TestDrink]
        expected = ["Test Name"]
        # act
        actual = r.unique(test_list,"Test Type")
        # assert
        self.assertEqual(expected,actual)

    # @patch("src.ETL.Person.identify_item_in_list")
    # @patch("builtins.input")
    # def test_same_again_yes(self, input_call, id_list):
    #     # arrange
    #     db = Mock(Database)
    #     mock_brewer = Mock(p.Person)
    #     mock_drink = Mock(d.Drink)
    #     test_list = [mock_drink]
    #     test_round = r.Round(db,mock_brewer,test_list)
    #     input_call.side_effect = ["y"]
    #     id_list.side_effect = [0]
    #     expected =  mock_drink
    #     # act
    #     actual = test_round.same_again(1, "Hot")
    #
    #     # assert
    #     self.assertEqual(expected, actual)


    # @patch("src.ETL.Person.identify_item_in_list")
    # @patch("src.drinks.Drink.make_drink")
    # @patch("builtins.input")
    # def test_same_again_no(self, input_call, making_drink, identify_item):
    #     # arrange
    #     db = Mock(Database)
    #     mock_brewer = Mock(p.Person)
    #     mock_drink = Mock(d.Drink)
    #     test_list = []
    #     identify_item
    #     test_round = r.Round(db,mock_brewer,test_list)
    #     input_call.side_effect = ["n"]
    #     making_drink.side_effect = [mock_drink]
    #     expected = mock_drink
    #     # act
    #     actual = test_round.same_again(1, "Hot")
    #
    #     # assert
    #     self.assertEqual(expected, actual)

    @patch("src.drinks.Drink.make_drink")
    def test_same_again_wo_fav(self, making_drink):
        # arrange
        db = Mock(Database)
        mock_brewer = Mock(p.Person)
        mock_drink = Mock(d.Drink)
        test_list = []
        test_round = r.Round(db,mock_brewer,test_list)
        making_drink.side_effect = [mock_drink]
        expected = mock_drink
        # act
        actual = test_round.same_again(None, "Hot")

        # assert
        self.assertEqual(expected, actual)


    @patch("builtins.input")
    def test_drink_type_hot(self, got_input):
        # arrange
        db = Mock(Database)
        mock_brewer = Mock(p.Person)
        test_list = []
        test_round = r.Round(db, mock_brewer, test_list)
        got_input.side_effect = ["H"]
        expected = "Hot"
        # act
        actual = test_round.get_drink_type()
        # assert
        self.assertEqual(expected, actual)

    # @patch("builtins.input")
    # def test_drink_type_come_again(self, got_input):
    #     # arrange
    #     db = Mock(Database)
    #     mock_brewer = Mock(p.Person)
    #     test_list = []
    #     test_round = r.Round(db, mock_brewer, test_list)
    #     got_input.side_effect = ["X", "H"]
    #     expected = "Hot"
    #     # act
    #     actual = test_round.drink_type()
    #     # assert
    #     self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_drink_type_soft(self, got_input):
        # arrange
        db = Mock(Database)
        mock_brewer = Mock(p.Person)
        test_list = []
        test_round = r.Round(db, mock_brewer, test_list)
        got_input.side_effect = ["S"]
        expected = "Soft"
        # act
        actual = test_round.get_drink_type()
        # assert
        self.assertEqual(expected, actual)

    @patch("builtins.input")
    def test_drink_type_alc(self, got_input):
        # arrange
        db = Mock(Database)
        mock_brewer = Mock(p.Person)
        test_list = []
        test_round = r.Round(db, mock_brewer, test_list)
        got_input.side_effect = ["A"]
        expected = "Alcoholic"
        # act
        actual = test_round.get_drink_type()
        # assert
        self.assertEqual(expected, actual)

    @patch.object(r.Round,"same_again")
    @patch.object(r.Round, "get_drink_type")
    def test_choose_drink(self, get_drink_type, same_again):
        # arrange
        db = Mock(Database)
        get_drink_type.return_value = "Hot"
        mock_brewer = Mock(p.Person)
        mock_brewer.fav_hd_id = 30
        drinky = Mock(d.Drink)
        same_again.return_value = drinky
        test_list = []
        test_round = r.Round(db, mock_brewer, test_list)
        expected = drinky

        # act
        actual = test_round.choose_drink(mock_brewer)

        # assert
        self.assertEqual(expected, actual)
        same_again.assert_called_once_with(30,"Hot")

    @patch.object(r.Round, "same_again")
    @patch.object(r.Round, "get_drink_type")
    def test_choose_drink(self, get_drink_type, same_again):
        # arrange
        db = Mock(Database)
        get_drink_type.return_value = "Alcoholic"
        mock_brewer = Mock(p.Person)
        mock_brewer.fav_ad_id = 1
        drinky = Mock(d.Drink)
        same_again.return_value = drinky
        test_list = []
        test_round = r.Round(db, mock_brewer, test_list)
        expected = drinky

        # act
        actual = test_round.choose_drink(mock_brewer)

        # assert
        self.assertEqual(expected, actual)
        same_again.assert_called_once_with(1, "Alcoholic")

    @patch.object(r.Round, "same_again")
    @patch.object(r.Round, "get_drink_type")
    def test_choose_drink(self, get_drink_type, same_again):
        # arrange
        db = Mock(Database)
        get_drink_type.return_value = "Soft"
        mock_brewer = Mock(p.Person)
        mock_brewer.fav_sd_id = 14
        drinky = Mock(d.Drink)
        same_again.return_value = drinky
        test_list = []
        test_round = r.Round(db, mock_brewer, test_list)
        expected = drinky

        # act
        actual = test_round.choose_drink(mock_brewer)

        # assert
        self.assertEqual(expected, actual)
        same_again.assert_called_once_with(14, "Soft")

