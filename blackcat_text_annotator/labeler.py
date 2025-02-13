from flashtext import KeywordProcessor  # 导入关键词提取库

# 定义编程语言词典（标准名称 : 别名列表）
LANGUAGES = {
    "Python": ["py"],
    "Java": [],
    "C": [],
    "C++": ["cpp"],
    "Go": ["golang"],
    "Rust": []
}

# 初始化关键词处理器（不区分大小写）
kp = KeywordProcessor(case_sensitive=False)

# 将语言名称和别名加入处理器
for lang, aliases in LANGUAGES.items():
    kp.add_keyword(lang)  # 添加标准名称，如"Python"
    for alias in aliases:  # 添加别名，如"py"对应到Python
        kp.add_keyword(alias)


def label(data):
    results = []  # 存储最终结果

    # 遍历输入的每个文本
    for text in data:
        # 在文本中查找匹配的编程语言（自动转小写匹配）
        found = list(set(kp.extract_keywords(text)))  # 用set去重

        # 处理如"C/C++"这样的组合形式，拆分成["C", "C++"]
        expanded = []
        for item in found:
            expanded.extend(item.split('/'))  # 用斜杠拆分

        # 格式化结果：如果没有找到返回"None"，否则用逗号连接
        result = "None" if not expanded else ",".join(sorted(expanded))
        results.append(result)

    return results


# 以下为DeepSeek为实现四个条件而改进的代码
# """高内聚设计
#
# LanguageLabeler类封装所有相关操作
# 将词典加载、关键词处理、标注逻辑集中管理
# 支持通过构造函数注入不同配置
# 低耦合实现
#
# 主程序通过类实例交互，不依赖内部实现
# 语言配置可动态替换（如从文件/数据库读取）
# 输入输出使用标准数据类型（List[str]）
# 防御性编程
#
# 类型检查（isinstance校验）
# 空值处理（strip()过滤空白）
# 异常捕获（处理非法输入和提取错误）
# 错误隔离（单个文本错误不影响整体流程）
# 可维护性提升
#
# 类型注解（Type Hints）
# 分离配置与逻辑
# 明确的错误消息定位问题"""

# from flashtext import KeywordProcessor
# from typing import List, Dict, Union
#
# # 将词典定义为常量（可后续改为从配置文件加载）
# DEFAULT_LANGUAGES = {
#     "Python": ["py"],
#     "Java": [],
#     "C": [],
#     "C++": ["cpp"],
#     "Go": ["golang"],
#     "Rust": []
# }
#
#
# class LanguageLabeler:
#     """高内聚的编程语言标注器（线程安全）"""
#
#     def __init__(self, lang_config: Dict[str, List[str]] = None):
#         self.kp = KeywordProcessor(case_sensitive=False)
#         self._load_config(lang_config or DEFAULT_LANGUAGES)
#
#     def _load_config(self, config: Dict[str, List[str]]):
#         """防御性加载语言配置"""
#         if not isinstance(config, dict):
#             raise TypeError("Language config must be a dictionary")
#
#         for lang, aliases in config.items():
#             if not isinstance(lang, str) or not lang.strip():
#                 raise ValueError(f"Invalid language name: {lang}")
#
#             # 添加标准名称
#             self.kp.add_keyword(lang.strip())
#
#             # 处理别名
#             if not isinstance(aliases, list):
#                 raise TypeError(f"Aliases for {lang} must be a list")
#
#             for alias in aliases:
#                 if not isinstance(alias, str) or not alias.strip():
#                     raise ValueError(f"Invalid alias for {lang}: {alias}")
#                 self.kp.add_keyword(alias.strip())
#
#     def label(self, texts: Union[List[str], str]) -> List[str]:
#         """带防御性校验的标注方法"""
#         # 统一输入格式
#         inputs = [texts] if isinstance(texts, str) else texts
#
#         if not isinstance(inputs, (list, tuple)):
#             raise TypeError("Input must be a string or list of strings")
#
#         results = []
#         for idx, text in enumerate(inputs, 1):
#             try:
#                 if not isinstance(text, str):
#                     raise TypeError(f"Item {idx} is not a string: {type(text)}")
#
#                 found = self.kp.extract_keywords(text.lower())
#                 expanded = []
#                 for item in set(found):  # 去重处理
#                     expanded.extend(item.split('/'))
#
#                 result = "None" if not expanded else ",".join(sorted(expanded))
#                 results.append(result)
#
#             except Exception as e:
#                 results.append("Error")
#                 print(f"Error processing item {idx}: {str(e)}")
#
#         return results
