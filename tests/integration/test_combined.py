import unittest
from blackcat_text_annotator.language_labeler import LanguageLabeler

class TestWorkflowIntegration(unittest.TestCase):
    def test_dynamic_config_workflow(self):
        """完整配置变更工作流测试"""
        # 初始状态验证
        default_labeler = LanguageLabeler()
        self.assertEqual(
            default_labeler.label(["cpp"]),
            ["C++"]
        )

        # 修改配置
        LanguageLabeler.mapping["C++"].add("cplusplus")
        updated_labeler = LanguageLabeler()
        self.assertEqual(
            updated_labeler.label(["cplusplus"]),
            ["C++"]
        )

        # 恢复配置（可选）
        LanguageLabeler.mapping["C++"].remove("cplusplus")
