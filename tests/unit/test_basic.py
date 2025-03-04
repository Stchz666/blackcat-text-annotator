import unittest
from blackcat_text_annotator.language_labeler import LanguageLabeler

class TestCoreFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.labeler = LanguageLabeler()

    def test_language_detection(self):
        """基本语言检测功能"""
        test_data = [
            ("Python项目", ["Python"]),
            ("Java和C++", ["Java, C++"]),
            ("Golang开发", ["Go"]),
            ("C编程", ["C"])
        ]
        for text, expected in test_data:
            with self.subTest(text=text):
                self.assertEqual(self.labeler.label([text]), expected)

    def test_case_insensitive(self):
        """不区分大小写"""
        self.assertEqual(
            self.labeler.label(["PYTHON"]),
            ["Python"]
        )
