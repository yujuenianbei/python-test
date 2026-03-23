"""
简单的数字计算逻辑
包含基本的加减乘除及扩展运算
支持整数和浮点数运算
"""

from typing import Union, Callable
from enum import Enum


class Operator(Enum):
    """支持的运算符枚举"""
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    POWER = '**'
    MODULO = '%'
    FLOOR_DIVIDE = '//'


Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """加法运算
    
    Args:
        a: 第一个数字
        b: 第二个数字
    
    Returns:
        两数之和
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """减法运算
    
    Args:
        a: 第一个数字
        b: 第二个数字
    
    Returns:
        两数之差
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """乘法运算
    
    Args:
        a: 第一个数字
        b: 第二个数字
    
    Returns:
        两数之积
    """
    return a * b


def divide(a: Number, b: Number, tolerance: float = 1e-10) -> float:
    """除法运算
    
    Args:
        a: 被除数
        b: 除数
        tolerance: 浮点数比较容差，用于判断除数是否为零
    
    Returns:
        两数之商
    
    Raises:
        ZeroDivisionError: 当除数为零时抛出
    """
    if abs(b) < tolerance:
        raise ZeroDivisionError("除数不能为零")
    return a / b


def power(a: Number, b: Number) -> Number:
    """幂运算
    
    Args:
        a: 底数
        b: 指数
    
    Returns:
        a 的 b 次幂
    """
    return a ** b


def modulo(a: Number, b: Number) -> Number:
    """取模运算
    
    Args:
        a: 被除数
        b: 除数
    
    Returns:
        余数
    
    Raises:
        ZeroDivisionError: 当除数为零时抛出
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为零")
    return a % b


def floor_divide(a: Number, b: Number) -> int:
    """整除运算
    
    Args:
        a: 被除数
        b: 除数
    
    Returns:
        商的整数部分
    
    Raises:
        ZeroDivisionError: 当除数为零时抛出
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为零")
    return a // b


# 运算符映射表
OPERATORS: dict[str, Callable[[Number, Number], Number]] = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': modulo,
    '//': floor_divide
}


def calculate(a: Number, b: Number, operator: str) -> Number:
    """
    根据运算符执行相应的计算
    
    Args:
        a: 第一个数字（被操作数）
        b: 第二个数字（操作数）
        operator: 运算符字符串 (+, -, *, /, **, %, //)
    
    Returns:
        计算结果
    
    Raises:
        ValueError: 当不支持该运算符或除数为零时抛出
        ZeroDivisionError: 当除数为零时抛出
    
    Examples:
        >>> calculate(10, 5, '+')
        15
        >>> calculate(10, 3, '/')
        3.3333333333333335
        >>> calculate(2, 3, '**')
        8
    """
    if operator not in OPERATORS:
        supported_ops = ', '.join(OPERATORS.keys())
        raise ValueError(f"不支持的运算符: '{operator}'。支持的运算符: {supported_ops}")
    
    return OPERATORS[operator](a, b)


def get_supported_operators() -> list[str]:
    """获取所有支持的运算符列表
    
    Returns:
        运算符列表
    """
    return list(OPERATORS.keys())


if __name__ == "__main__":
    # 示例使用
    num1: Number = 10
    num2: Number = 5
    
    print("=" * 40)
    print("简单计算器示例")
    print("=" * 40)
    print(f"操作数 1: {num1}")
    print(f"操作数 2: {num2}")
    print("-" * 40)
    
    # 测试所有支持的运算符
    test_operators = ['+', '-', '*', '/', '**', '%', '//']
    for op in test_operators:
        try:
            result = calculate(num1, num2, op)
            print(f"{num1} {op} {num2} = {result}")
        except Exception as e:
            print(f"{num1} {op} {num2} 出错: {e}")
    
    print("-" * 40)
    
    # 测试异常情况
    print("\n异常测试:")
    try:
        calculate(10, 0, '/')
    except ZeroDivisionError as e:
        print(f"捕获到除零错误: {e}")
    
    try:
        calculate(10, 5, '^')
    except ValueError as e:
        print(f"捕获到无效运算符错误: {e}")
    
    print("\n支持的运算符:", get_supported_operators())
