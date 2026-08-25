import unittest

from src.main.user import User
from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_problem1(self):
        """
        In this test we are querying everything in the users table to ensure that Alexa was successfully
        updated to "Rush".
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("SELECT * FROM site_user;")
            actual_result = [User(row[0], row[1], row[2]) for row in cur.fetchall()]
        except Exception as e:
            print(f"problem1: {e}\n")
            self.fail(str(e))
        finally:
            conn.close()

        expected_result = [
            User(1, "Steve", "Garcia"),
            User(2, "Alexa", "Rush"),
            User(3, "Steve", "Jones"),
            User(4, "Brandon", "Smith"),
            User(5, "Adam", "Jones"),
        ]

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
