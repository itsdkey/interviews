from unittest import TestCase
from unittest.mock import patch

from .task import lottery_generator


class FooTestCase(TestCase):
    def setUp(self) -> None:
        self.generator = lottery_generator

    @patch("app.task.random.randint")
    def test_1(self, m_randint):
        values = [1, 2, 3, 4, 5, 6, 7, 8]
        m_randint.side_effect = values
        expected_result = values

        result = self.generator()

        self.assertEqual(result, expected_result)

    @patch("app.task.random.randint")
    def test_duplicates(self, m_randint):
        m_randint.side_effect = [1, 1, 2, 2, 3, 3, 7, 8, 12]

        self.generator()

        self.assertEqual(m_randint.call_count, 9)
