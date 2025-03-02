from blackcat_text_annotator.language_labeler import LanguageLabeler

def demo_labeler_capability(labeler: LanguageLabeler):
    # 测试数据包含不同大小写和组合形式
    test_cases = [
        "Python开发需要掌握C/C++基础",
        "GO和GOLANG有什么区别",
        "JAVA工程师招聘",
        "无关文本"
    ]

    # 执行标注并展示结果
    print("标注结果：")
    for text, label in zip(test_cases, labeler.label(test_cases)):
        print(f"[{label}]\t{text}")


if __name__ == '__main__':
    print("=== 基础版 ===")
    basic_labeler = LanguageLabeler()
    demo_labeler_capability(basic_labeler)

    print("\n=== 扩展版 ===")
    extended_labeler = LanguageLabeler()
    extended_labeler.add_language('JavaScript', ['js', 'ES6'])
    extended_labeler.add_language('Rust', ['rs'])
    demo_labeler_capability(extended_labeler)
