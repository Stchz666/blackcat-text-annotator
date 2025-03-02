from abc import ABC, abstractmethod
from typing import List, Dict, Iterable


class BaseTextLabeler(ABC):
    def __init__(self, config: Dict = None):
        self.config = config or self.default_config
        self._init_processor()

    @property
    @abstractmethod
    def default_config(self) -> Dict:
        """子类必须提供的默认配置"""

    @abstractmethod
    def _init_processor(self):
        """初始化处理引擎"""

    @abstractmethod
    def label(self, texts: Iterable[str]) -> List[str]:
        """核心标注方法"""