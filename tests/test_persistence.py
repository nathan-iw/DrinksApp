import unittest.mock
from unittest.mock import Mock, patch
import src.ETL.Person as p
import app
from app import App
from src.ETL.persistence import Database



class DatabaseTests(unittest.TestCase):



    def test_save_person(self):
        # arrange
        db = Mock(Database)
        test_person_list = []
        test_first_name = "Test"
        test_last_name = "Daily"
        test_age = 1

        # act
        p.add_person(test_person_list,test_first_name,test_last_name,test_age)


        # assert
        db.save_drink.assert_called_once_with(test_person)