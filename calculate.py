"""
简单的数字计算逻辑示例
支持基础四则运算，包含类型检查、异常处理和扩展性设计
"""

from typing import Union, Callable
from decimal import Decimal, getcontext

# 设置高精度计算上下文（可选）
getcontext().prec = 10

# 定义数值类型别名
Number = Union[int, float, Decimal]


def validate_numbers(*args) -> None:
    """验证输入是否为有效数字类型"""
    for arg in args:
        if not isinstance(arg, (int, float, Decimal)) or isinstance(arg, bool):
            raise TypeError(f"无效的数字类型: {type(arg).__name__}")


def add(a: Number, b: Number) -> Number:
    """加法运算"""
    validate_numbers(a, b)
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """减法运算"""
    validate_numbers(a, b)
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """乘法运算"""
    validate_numbers(a, b)
    return a * b


def divide(a: Number, b: Number, precision: int = 2) -> float:
    """
    除法运算
    
    参数:
        a: 被除数
        b: 除数
        precision: 结果保留小数位数（默认2位）
    
    返回:
        除法结果（保留指定精度）
    """
    validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("除数不能为零")
    result = a / b
    return round(float(result), precision)


def power(base: Number, exponent: Number) -> Number:
    """幂运算"""
    validate_numbers(base, exponent)
    return base ** exponent


def modulo(a: Number, b: Number) -> Number:
    """取模运算"""
    validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("模数不能为零")
    return a % b


# 运算符映射表
OPERATORS: dict[str, Callable] = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': modulo
}


def calculate(a: Number, b: Number, operator: str, **kwargs) -> Number:
    """
    根据运算符执行相应的计算
    
    参数:
        a: 第一个数字
        b: 第二个数字
        operator: 运算符 (+, -, *, /, **, %)
        **kwargs: 传递给具体运算函数的额外参数（如 precision）
    
    返回:
        计算结果
    
    异常:
        TypeError: 输入类型无效
        ZeroDivisionError: 除数为零
        ValueError: 不支持的运算符
    """
    if operator not in OPERATORS:
        supported = ', '.join(OPERATORS.keys())
        raise ValueError(f"不支持的运算符: {operator}。支持的运算符: {supported}")
    
    # 特殊处理除法，传递精度参数
    if operator == '/' and 'precision' in kwargs:
        return OPERATORS[operator](a, b, precision=kwargs['precision'])
    
    return OPERATORS[operator](a, b)


def calculate_expression(expression: str) -> Number:
    """
    计算简单表达式字符串（格式：数字 运算符 数字）
    
    参数:
        expression: 表达式字符串，如 "10 + 5"
    
    返回:
        计算结果
    """
    parts = expression.strip().split()
    if len(parts) != 3:
        raise ValueError("表达式格式错误，应为：数字 运算符 数字")
    
    try:
        a = float(parts[0]) if '.' in parts[0] else int(parts[0])
        operator = parts[1]
        b = float(parts[2]) if '.' in parts[2] else int(parts[2])
    except ValueError as e:
        raise ValueError(f"无法解析表达式: {e}")
    
    return calculate(a, b, operator)


if __name__ == "__main__":
    print("=== 优化版数字计算器 ===\n")
    
    # 基础运算示例
    num1, num2 = 10, 5
    print(f"[基础运算] {num1} + {num2} = {add(num1, num2)}")
    print(f"[基础运算] {num1} - {num2} = {subtract(num1, num2)}")
    print(f"[基础运算] {num1} * {num2} = {multiply(num1, num2)}")
    print(f"[基础运算] {num1} / {num2} = {divide(num1, num2)}")
    
    # 新增运算
    print(f"\n[幂运算] 2 ** 8 = {power(2, 8)}")
    print(f"[取模运算] 17 % 5 = {modulo(17, 5)}")
    
    # 通用计算函数
    print("\n[通用计算]")
    test_cases = [
        (15, 7, '+'),
        (20, 8, '-'),
        (6, 9, '*'),
        (100, 4, '/'),
        (2, 10, '**'),
        (17, 5, '%')
    ]
    
    for a, b, op in test_cases:
        result = calculate(a, b, op)
        print(f"  {a} {op} {b} = {result}")
    
    # 高精度除法
    print(f"\n[高精度除法] 10 / 3 = {calculate(10, 3, '/', precision=5)}")
    
    # 表达式解析
    print("\n[表达式解析]")
    expressions = ["10 + 5", "20 - 8", "6 * 9", "100 / 4"]
    for expr in expressions:
        result = calculate_expression(expr)
        print(f"  '{expr}' = {result}")
    
    # 错误处理演示
    print("\n[错误处理测试]")
    try:
        calculate(10, 0, '/')
    except ZeroDivisionError as e:
        print(f"  ✓ 捕获除零错误: {e}")
    
    try:
        calculate(10, 5, '^')
    except ValueError as e:
        print(f"  ✓ 捕获无效运算符: {e}")
    
    try:
        add("10", 5)
    except TypeError as e:
        print(f"  ✓ 捕获类型错误: {e}")
    
    print("\n=== 计算完成 ===")
