import unittest.mock
from unittest.mock import Mock, patch
import app
from app import App
from src.ETL.persistence import Database




class IntegrationTest(unittest.TestCase):

    def test_save_csv_customers(self):
        # Arrange
        db = Mock(Database)
        app = App(db)
        # Act
        app.save_csv_customers(db, "tests/test.csv")
        # Assert
        db.save_to_db.assert_called_once_with([('Roy', 'Lewis', 97)])

if __name__ == "__main__":
    unittest.main()