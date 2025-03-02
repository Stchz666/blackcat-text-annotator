import pytest


def test_label_speed(benchmark, base_labeler):
    # 生成测试数据：1000条样本
    texts = ["Python和C++混合编程"] * 1000
    benchmark(base_labeler.label, texts)


def test_memory_usage(base_labeler):
    import tracemalloc

    tracemalloc.start()

    # 记录初始内存
    snapshot1 = tracemalloc.take_snapshot()

    # 执行内存敏感操作
    base_labeler.add_language('Scala', ['sc'])
    _ = base_labeler.label(["Scala函数式编程"] * 1000)

    # 计算内存差异
    snapshot2 = tracemalloc.take_snapshot()
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')

    assert top_stats[0].size_diff < 1024 * 100  # 内存增长应小于100KB
