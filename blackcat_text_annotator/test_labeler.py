import unittest
from threading import Thread
from blackcat_text_annotator.language_labeler import LanguageLabeler

class TestLanguageLabeler(unittest.TestCase):
    def setUp(self):
        self.labeler = LanguageLabeler()

    def test_basic_functionality(self):
        test_data = [  # 测试数据保持不变
            ("python", {"Python"}),
            ("C/C++开发", {"C", "C++"}),
            ("GOLANG工程师", {"Go"}),
            ("", set())
        ]
        for input_str, expected in test_data:
            with self.subTest(input=input_str):  # 保持subTest的测试标识
                result = set(self.labeler.label([input_str])[0].split(','))
                self.assertEqual(result, expected if expected else {'None'})

    def test_dynamic_extension(self):
        self.labeler.add_language('Rust', ['rs'])
        self.assertIn('Rust', self.labeler.label(['rs项目'])[0])

    def test_thread_safety(self):
        def concurrent_adding():  # 并发添加的测试方法
            for i in range(100):
                self.labeler.add_language(f'Lang{i}', [f'l{i}'])

        threads = [Thread(target=concurrent_adding) for _ in range(5)]
        for t in threads: t.start()
        for t in threads: t.join()

        # 验证最后添加的语言存在
        self.assertIn('Lang99', self.labeler.label(['l99'])[0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
