import pytest
from blackcat_text_annotator.language_labeler import LanguageLabeler

@pytest.fixture(scope="module")
def base_labeler():
    """提供默认配置的标注器"""
    return LanguageLabeler()

@pytest.fixture
def extended_labeler():
    """已扩展JavaScript和Rust的标注器"""
    labeler = LanguageLabeler()
    labeler.add_language('JavaScript', ['js', 'ES6'])
    labeler.add_language('Rust', ['rs'])
    return labeler