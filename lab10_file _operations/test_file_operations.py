import unittest
import os
from file_operations import read_file, write_file, append_file, email_read


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.filename = "test_file.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_file(self):
        msg = "Daniel Oluwasina"
        with open(self.filename, "w") as f:
            f.write(msg)

        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as f:
            result = f.read()

        self.assertEqual(result, msg)

    def test_read_file(self):
        expected_content = "Read me!"
        with open(self.filename, "w") as file:
            file.write(expected_content)

        with open(self.filename, "r") as file:
            data = file.read()

        self.assertEqual(data, expected_content)

    def test_append_file(self):
        initial_content = "Line one"
        append_content = "\nLine two"

        with open(self.filename, "w") as f:
            f.write(initial_content)

        with open(self.filename, "a") as f:
            f.write(append_content)

        with open(self.filename, "r") as f:
            final_data = f.read()

        self.assertEqual(final_data, initial_content + append_content)

    def test_email_read(self):
        email_ex = "JDoe@gmail.com"
        with open(self.filename, "w") as f:
            f.write(email_ex)

        with open(self.filename, "r") as f:
            email = f.read()

        self.assertEqual(email, email_ex)


if __name__ == "__main__":
    unittest.main()
