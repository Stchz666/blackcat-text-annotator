import unittest
from threading import Thread
from blackcat_text_annotator.language_labeler import LanguageLabeler


class TestLanguageLabeler(unittest.TestCase):
    def setUp(self):
        self.labeler = LanguageLabeler()

    def test_基础功能(self):
        测试数据 = [
            ("python", {"Python"}),
            ("C/C++开发", {"C", "C++"}),
            ("GOLANG工程师", {"Go"}),
            ("", set())
        ]
        for 输入, 预期 in 测试数据:
            with self.subTest(输入=输入):
                结果 = set(self.labeler.label([输入])[0].split(','))
                self.assertEqual(结果, 预期 if 预期 else {'None'})

    def test_动态扩展(self):
        self.labeler.add_language('Rust', ['rs'])
        self.assertIn('Rust', self.labeler.label(['rs项目'])[0])

    def test_线程安全(self):
        def 并发添加():
            for i in range(100):
                self.labeler.add_language(f'Lang{i}', [f'l{i}'])

        threads = [Thread(target=并发添加) for _ in range(5)]
        for t in threads: t.start()
        for t in threads: t.join()

        # 验证最后添加的语言存在
        self.assertIn('Lang99', self.labeler.label(['l99'])[0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
