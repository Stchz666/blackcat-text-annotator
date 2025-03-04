import re

class LanguageLabeler:
    # 调整后的映射配置（注意C++的别名）
    mapping = {
        'Python': {'py', 'python'},
        'Java': {'java'},
        'C': {'c'},
        'C++': {'cpp', 'c++', 'cplusplus'},
        'Go': {'go', 'golang'}
    }

    def __init__(self):
        # 预处理：语言关键词转为小写集合
        self.keywords = {
            lang: {kw.lower() for kw in keywords}
            for lang, keywords in self.mapping.items()
        }

    def label(self, texts):
        results = []
        for text in texts:
            # 使用正则提取所有字母数字（保留C++中的+号）
            words = re.findall(r'[a-z0-9+]+', text.lower())  # 修改行
            matches = []
            for lang in self.mapping:
                if any(kw in words for kw in self.keywords[lang]):
                    matches.append(lang)
            results.append(', '.join(matches) or 'None')
        return results
