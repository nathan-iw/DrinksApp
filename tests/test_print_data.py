import unittest.mock
import src.tools.print_data as prin
import io
class TestPrint(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_rows(self, mock_stdout):
        # Arrange
        diction = ['Alex', 'Coffee', 'black', 'strong', 0]
        expected_outcome = """| Alex\n| Coffee\n| black\n| strong\n| 0\n"""
        # Act
        prin.print_rows(diction)
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_header(self, mock_stdout):
        # Arrange
        title = "test title"
        expected_outcome = "| TEST TITLE\n"
        # Act
        prin.print_header(title)
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_outline(self, mock_stdout):
        # Arrange
        expected_outcome = "+====================+\n"
        # Act
        prin.print_outline()
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_table_header(self, mock_stdout):
        # Arrange
        title = "test title"
        expected_outcome = "| TEST TITLE\n"
        # Act
        prin.print_header(title)
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_table(self, mock_stdout):
        # Arrange
        test_title = "test title"
        test_data = ['Alex', 'Coffee', 'black', 'strong', 0]
        expected_outcome = """+====================+
| TEST TITLE
+====================+
| Alex
| Coffee
| black
| strong
| 0
+====================+
"""
        # Act
        prin.print_table(test_title,test_data)
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())
