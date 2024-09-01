import unittest
from helper import get_csv

class TestHelperFunctions(unittest.TestCase):

    def test_get_csv(self):
        # Beispielhafte Daten
        data = [
            {"title": "Meeting 1", "category": "Work", "description": "Discuss project, budget, and timeline"},
            {"title": "Meeting 2", "category": "Personal", "description": "Gym, buy groceries"}
        ]
        # Erwartetes CSV Format
        expected_csv = "title,category,description\nMeeting 1,Work,\"Discuss project, budget, and timeline\"\nMeeting 2,Personal,\"Gym, buy groceries\""

        # Vergleiche die Zeilen ohne Zeilenumbrüche
        self.assertEqual(get_csv(data).splitlines(), expected_csv.splitlines())

if __name__ == "__main__":
    unittest.main()