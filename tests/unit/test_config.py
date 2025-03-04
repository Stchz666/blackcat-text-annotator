import unittest
from blackcat_text_annotator.language_labeler import LanguageLabeler

class TestConfiguration(unittest.TestCase):
    original_mapping = None

    @classmethod
    def setUpClass(cls):
        cls.original_mapping = LanguageLabeler.mapping.copy()

    def tearDown(self):
        # 恢复原始配置
        LanguageLabeler.mapping = self.original_mapping.copy()

    def test_add_new_language(self):
        """新增语言支持测试"""
        LanguageLabeler.mapping["Ruby"] = {"rb", "ruby"}
        labeler = LanguageLabeler()
        self.assertEqual(
            labeler.label(["rb脚本"]),
            ["Ruby"]
        )
