import unittest.mock
from unittest.mock import Mock, patch
import src.ETL.Person as p
# import app
# from app import App
from src.ETL.persistence import Database



class PersonTests(unittest.TestCase):


    def test_save_person(self):
        # arrange
        db = Mock(Database)
        test_person_list = []
        test_first_name = "Test"
        test_last_name = "Daily"
        test_age = 1

        # act
        p.add_person(db, test_person_list,test_first_name,test_last_name,test_age)


        # assert
        db.save_person.assert_called_once_with(test_first_name, test_last_name, test_age)