import unittest
from blackcat_text_annotator.language_labeler import LanguageLabeler

class TestErrorCases(unittest.TestCase):
    def setUp(self):
        self.labeler = LanguageLabeler()

    def test_empty_input(self):
        """空输入处理"""
        self.assertEqual(
            self.labeler.label([""]),
            ["None"]
        )

    def test_invalid_type(self):
        """错误输入类型防护"""
        with self.assertRaises(AttributeError):
            self.labeler.label([123])  # 输入非字符串
