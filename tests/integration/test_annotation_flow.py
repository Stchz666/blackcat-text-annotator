from blackcat_text_annotator.language_labeler import LanguageLabeler

def test_full_workflow():
    # 初始化并扩展配置
    labeler = LanguageLabeler()
    labeler.add_language('TypeScript', ['ts'])
    labeler.add_language('Ruby', ['rb'])

    # 测试数据
    inputs = [
        "Python和TypeScript项目",
        "Ruby工程师招聘",
        "TS类型系统研究",
        "C/C++底层开发"
    ]

    # 执行标注
    results = labeler.label(inputs)

    # 验证结果
    assert results == [
        "Python,TypeScript",
        "Ruby",
        "TypeScript",
        "C,C++"
    ]
