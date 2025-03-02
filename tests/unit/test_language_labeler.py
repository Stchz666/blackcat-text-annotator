import pytest
from blackcat_text_annotator.language_labeler import LanguageLabeler


class TestInitialization:
    def test_default_config(self):
        labeler = LanguageLabeler()
        assert labeler.config == {
            'Python': {'py'},
            'Java': set(),
            'C': set(),
            'C++': {'cpp'},
            'Go': {'golang'}
        }

    def test_custom_config_override(self):
        custom_config = {'Ruby': {'rb'}}
        labeler = LanguageLabeler(config=custom_config)
        assert labeler.config == custom_config


class TestAddLanguage:
    def test_add_new_language(self):
        labeler = LanguageLabeler()
        labeler.add_language('Rust', ['rs'])
        assert 'Rust' in labeler.config
        assert labeler.config['Rust'] == {'rs'}

    def test_add_existing_language(self, base_labeler):
        base_labeler.add_language('Python', ['python3'])
        assert base_labeler.config['Python'] == {'py', 'python3'}


class TestLabelFunction:
    @pytest.mark.parametrize("input_text, expected", [
        ("Python开发", "Python"),
        ("Golang项目", "Go"),
        ("C/C++系统编程", "C,C++"),
        ("无关文本", "None"),
        ("PYTHON工程师", "Python"),  # 大小写测试
        ("", "None"),  # 空字符串
        ("Java和JavaScript", "Java")  # 子串测试
    ])
    def test_basic_cases(self, base_labeler, input_text, expected):
        result = base_labeler.label([input_text])[0]
        assert sorted(result.split(',')) == sorted(expected.split(','))

    def test_extended_cases(self, extended_labeler):
        assert extended_labeler.label(["ES6特性"])[0] == "JavaScript"
        assert extended_labeler.label(["Rust编程"])[0] == "Rust"


class TestEdgeCases:
    def test_long_text(self, base_labeler):
        long_text = "Python" * 1000
        assert base_labeler.label([long_text])[0] == "Python"

    def test_special_characters(self, base_labeler):
        assert base_labeler.label(["Python@3.11"])[0] == "Python"
        assert base_labeler.label(["C++/C#比较"])[0] == "C,C++"


class TestThreadSafety:
    def test_concurrent_access(self, base_labeler):
        from concurrent.futures import ThreadPoolExecutor

        def stress_test(_):
            return base_labeler.label(["Python和Golang"])[0]

        with ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(stress_test, range(100)))

        assert all(r == "Go,Python" for r in results)