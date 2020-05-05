import unittest.mock
from unittest.mock import Mock, patch
import app
import src.ETL.Person as p
import src.ETL.search_table as s
from src.ETL.persistence import Database

class SearchTests(unittest.TestCase):
    print("Round tests running...")

    # def test_search_person(self):
    #     # arrange
    #     TestPerson1 = p.Person("Test","Daily",10,None,None,None)
    #     TestPerson2 = p.Person("Tess", "Durbeyfield", 16, None, None, None)
    #     test_search_term = "Test"
    #     test_list = [TestPerson1, TestPerson2]
    #     expected = [TestPerson1]
    #     # act
    #     actual = s.search_person(test_search_term,test_list)
    #     # assert
    #     self.assertEqual(expected,actual)

    # def test_search_person_partial(self):
    #     # arrange
    #     TestPerson1 = p.Person("Test","Daily",10,None,None,None)
    #     TestPerson2 = p.Person("Tess", "Durbeyfield", 16, None, None, None)
    #     test_search_term = "Tes"
    #     test_list = [TestPerson1, TestPerson2]
    #     expected = [TestPerson1, TestPerson2]
    #     # act
    #     actual = s.search_person(test_search_term,test_list)
    #     # assert
    #     self.assertEqual(expected,actual)

    def test_search_person_absent(self):
        # arrange
        TestPerson1 = p.Person("Test","Daily",10,None,None,None)
        TestPerson2 = p.Person("Tess", "Durbeyfield", 16, None, None, None)
        test_search_term = "Sally"
        test_list = [TestPerson1, TestPerson2]
        expected = []
        # act
        actual = s.search_person(test_search_term,test_list)
        # assert
        self.assertEqual(expected,actual)

