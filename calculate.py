#!/usr/bin/env python3
"""
简单的数字计算逻辑
包含基本的加减乘除和进阶计算功能
"""


def add(a, b):
    """加法"""
    return a + b


def subtract(a, b):
    """减法"""
    return a - b


def multiply(a, b):
    """乘法"""
    return a * b


def divide(a, b):
    """除法"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def power(base, exponent):
    """幂运算"""
    return base ** exponent


def modulo(a, b):
    """取模运算"""
    if b == 0:
        raise ValueError("模数不能为零")
    return a % b


def calculate_expression(expression):
    """
    计算简单的数学表达式
    支持 +, -, *, /, **, %
    """
    try:
        # 使用 eval 计算表达式（注意：在生产环境中需要更安全的解析方式）
        result = eval(expression)
        return result
    except Exception as e:
        raise ValueError(f"表达式计算错误: {e}")


def main():
    """主函数 - 演示计算功能"""
    print("=== 简单数字计算逻辑 ===\n")
    
    # 基本运算示例
    a, b = 10, 5
    
    print(f"数字: a = {a}, b = {b}\n")
    print(f"加法: {a} + {b} = {add(a, b)}")
    print(f"减法: {a} - {b} = {subtract(a, b)}")
    print(f"乘法: {a} * {b} = {multiply(a, b)}")
    print(f"除法: {a} / {b} = {divide(a, b)}")
    print(f"幂运算: {a} ** {b} = {power(a, b)}")
    print(f"取模: {a} % {b} = {modulo(a, b)}")
    
    # 表达式计算示例
    print("\n=== 表达式计算 ===")
    expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 ** 2",
        "100 / 4 + 5"
    ]
    
    for expr in expressions:
        result = calculate_expression(expr)
        print(f"{expr} = {result}")


if __name__ == "__main__":
    main()
