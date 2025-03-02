from typing import List, Dict, Iterable
from threading import Lock
from flashtext import KeywordProcessor
from .base_labeler import BaseTextLabeler


class LanguageLabeler(BaseTextLabeler):
    """支持动态扩展的线程安全标注器"""

    @property
    def default_config(self) -> Dict:
        return {
            'Python': {'py'},
            'Java': set(),
            'C': set(),
            'C++': {'cpp'},
            'Go': {'golang'}
        }

    def __init__(self, config: Dict = None):
        self._lock = Lock()
        super().__init__(config)

    def _init_processor(self):
        self.processor = KeywordProcessor(case_sensitive=False)
        self._add_keywords(self.config)

    def _add_keywords(self, config: Dict):
        """原子化关键词添加操作"""
        with self._lock:
            for lang, aliases in config.items():
                self.processor.add_keyword(lang)
                for alias in aliases:
                    self.processor.add_keyword(alias)

    def add_language(self, lang: str, aliases: Iterable[str] = ()):
        """动态添加新语言"""
        self._add_keywords({lang: set(aliases)})
        self.config[lang] = aliases

    def label(self, texts: Iterable[str]) -> List[str]:
        def process(text: str):
            found = {kw.split('/')[0] for kw in self.processor.extract_keywords(text)}
            return ','.join(sorted(found)) if found else 'None'

        return [process(text) for text in texts]
