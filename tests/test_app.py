import unittest.mock
from unittest.mock import Mock, patch
import app
import src.drinks.Drink as d
import src.ETL.Person as p
from src.ETL.persistence import Database


class AppTests(unittest.TestCase):
    print("App tests running...")

    def test_bye_mate(self):
        # arrange
        expected = """
$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$'`$adiosamigo$'`$$$$
$$$$$$  $$$$$$$$$$$  $$$$
$$$$$$$  '$/ `/ `$' .$$$$
$$$$$$$$. i  i  /! .$$$$$
$$$$$$$$$.--'--'   $$$$$$
$$^^$$$$$'        J$$$$$$
$$$   ~""   `.   .$$$$$$$
$$$$$e,      ;  .$$$$$$$$
$$$$$$$$$$$.'   $$$$$$$$$
$$$$$$$$$$$$.    $$$$$$$$
$$$$$$$$$$$$$    $$$$$$$$"""
        # act
        actual = app.bye_mate()
        # assert
        self.assertEqual(expected, actual)

    def test_unique(self):
        # arrange
        db = Mock(Database)
        MockApp = app.App(db)
        TestDrink = d.Drink("Test Type","Test Name","Test Details","Test Price")
        test_list = [TestDrink, TestDrink]
        expected = ["Test Name"]
        # act
        actual = MockApp.unique(test_list,"Test Type")
        # assert
        self.assertEqual(expected,actual)

    # @patch("builtins.input")
    # def test_same_again_yes(self, input_call):
    #     # arrange
    #     db = Mock(Database)
    #     MockApp = app.App(db)
    #     input_call.side_effect = "y"
    #     expected = 1
    #     # act
    #     actual = MockApp.same_again(1,"Hot")
    #
    #     #assert
    #     self.assertEqual(expected, actual)
    #
    # @patch("src.drinks.Drink.make_drink")
    # @patch("builtins.input")
    # def test_same_again_no(self, input_call, making_drink):
    #     # arrange
    #     db = Mock(Database)
    #     MockApp = app.App(db)
    #     input_call.side_effect = "n"
    #     making_drink.side_effect = Mock(d.Drink)
    #     expected = Mock(d.Drink)
    #     # act
    #     actual = MockApp.same_again(1, "Hot")
    #
    #     # assert
    #     making_drink.assert_called_once_with(db, 1, "Hot")
    #     self.assertEqual(expected, actual)

    @patch("app.App.get_input")
    def test_drink_type_hot(self, got_input):
        # arrange
        db = Mock(Database)
        MockApp = app.App(db)
        got_input.side_effect = ["H"]
        expected = "Hot"

        # act
        actual = MockApp.drink_type()

        # assert
        self.assertEqual(expected,actual)

    @patch("app.App.get_input")
    def test_drink_type_soft(self, got_input):
        # arrange
        db = Mock(Database)
        MockApp = app.App(db)
        got_input.side_effect = ["S"]
        expected = "Soft"

        # act
        actual = MockApp.drink_type()

        # assert
        self.assertEqual(expected,actual)

    @patch("app.App.get_input")
    def test_drink_type_alc(self, got_input):
        # arrange
        db = Mock(Database)
        MockApp = app.App(db)
        got_input.side_effect = ["A"]
        expected = "Alcoholic"

        # act
        actual = MockApp.drink_type()

        # assert
        self.assertEqual(expected, actual)

#     @patch("app.App.same_again")
#     @patch("app.App.drink_type")
#     def test_choose_drink(self, drink_type, same_again):
#         # arrange
#         db = Mock(Database)
#         MockApp = app.App(db)
#         TestPerson1 = p.Person("Test", "Daily", 10, 30, 14, 1)
#         expected = 30
#         drink_type.side_effect = ["Hot"]
#         same_again.side_effect = [30]
#
#         # act
#         actual = MockApp.choose_drink(TestPerson1)
#
#         # assert
#         self.assertEqual(expected, actual)
#         same_again.assert_called_once_with(30, "Hot")
#
#     @patch("app.App.same_again")
#     @patch("app.App.drink_type")
#     def test_choose_drink_alc(self, drink_type, same_again):
#         # arrange
#         db = Mock(Database)
#         MockApp = app.App(db)
#         TestPerson1 = Mock(p.Person)
#         TestPerson1.fav_ad_id = 1
#         expected = 14
#         drink_type.side_effect = ["Soft"]
#         same_again.side_effect = [14]
#
#         # act
#         actual = MockApp.choose_drink(TestPerson1)
#
#         # assert
#         self.assertEqual(expected, actual)
#         same_again.assert_called_once_with(14, "Soft")
#
#     @patch("app.App.same_again")
#     @patch("app.App.drink_type")
#     def test_choose_drink_alc(self, drink_type, same_again):
#         # arrange
#         db = Mock(Database)
#         MockApp = app.App(db)
#         TestPerson1 = Mock(p.Person)
#         TestPerson1.fav_ad_id = 1
#         expected = 1
#         drink_type.side_effect = ["Alcoholic"]
#         same_again.side_effect = [1]
#
#         # act
#         actual = MockApp.choose_drink(TestPerson1)
#
#         # assert
#         self.assertEqual(expected, actual)
#         same_again.assert_called_once_with(1, "Alcoholic")
#
#
# class IntegrationTest(unittest.TestCase):
#     print("Integration tests running...")
#
#     def test_save_csv_customers(self):
#         # Arrange
#         db = Mock(Database)
#         MockApp = app.App(db)
#         # Act
#         MockApp.save_csv_customers(db, "tests/test.csv")
#         # Assert
#         db.save_to_db.assert_called_once_with([('Roy', 'Lewis', 97)])
#
#
# class IntegrationTest(unittest.TestCase):
#     print("Integration tests running...")
#
#     def test_create_round(self):
#         # Arrange
#         db = Mock(Database)
#         MockApp = app.App(db)
#         db.save_to_db
#         # Act
#         MockApp.root()
#
#         # Assert
#         db.save_to_db.assert_called_once_with([('Roy', 'Lewis', 97)])


if __name__ == "__main__":
    unittest.main()
