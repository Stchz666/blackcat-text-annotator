from blackcat_text_annotator.language_labeler import LanguageLabeler

def 演示标注器能力(标注器: LanguageLabeler):
    # 测试数据包含不同大小写和组合形式
    测试案例 = [
        "Python开发需要掌握C/C++基础",
        "GO和GOLANG有什么区别",
        "JAVA工程师招聘",
        "无关文本"
    ]

    # 执行标注并展示结果
    print("标注结果：")
    for 文本, 标签 in zip(测试案例, 标注器.label(测试案例)):
        print(f"[{标签}]\t{文本}")


if __name__ == '__main__':
    print("=== 基础版 ===")
    基础标注器 = LanguageLabeler()
    演示标注器能力(基础标注器)

    print("\n=== 扩展版 ===")
    扩展标注器 = LanguageLabeler()
    扩展标注器.add_language('JavaScript', ['js', 'ES6'])
    扩展标注器.add_language('Rust', ['rs'])
    演示标注器能力(扩展标注器)