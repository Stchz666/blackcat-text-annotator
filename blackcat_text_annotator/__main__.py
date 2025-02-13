from labeler import label  # 导入写好的标注函数


def main():
    # 测试数据：包含5个示例文本
    data = [
        "这是一个测试文本。",
        "大模型可以帮助我们进行文本标注。",
        "Python是一门强大的编程语言。",
        "学习C/C++能更好理解计算机系统。",
        "Go和Golang是同一个语言吗？"
    ]

    # 调用标注函数处理全部文本
    results = label(data)

    # 打印输入和输出的对应结果
    print("输入文本：")
    for text in data:
        print(f" - {text}")

    print("\n检测结果：")
    for res in results:
        print(f" - {res}")


# 当直接运行此文件时执行main函数
if __name__ == "__main__":
    main()

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

# from labeler import LanguageLabeler
# from typing import List
#
#
# def main():
#     # 初始化标注器（可轻松替换配置）
#     labeler = LanguageLabeler()
#
#     # 测试数据集
#     test_data = [
#         "这是一个测试文本。",
#         "大模型可以帮助我们进行文本标注。",
#         12345,  # 故意加入错误数据测试防御性
#         "Python是一门强大的编程语言。",
#         "学习C/C++能更好理解计算机系统。",
#         "Go和Golang是同一个语言吗？"
#     ]
#
#     try:
#         results = labeler.label(test_data)
#     except Exception as e:
#         print(f"Fatal error during labeling: {str(e)}")
#         return
#
#     # 可视化结果
#     print("\n安全检测结果：")
#     for text, result in zip(test_data, results):
#         status = "✓" if result != "Error" else "✗"
#         print(f"{status} 输入：{str(text)[:20]}... → 输出：{result}")
#
#
# if __name__ == "__main__":
#     main()
