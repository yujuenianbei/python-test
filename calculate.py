#!/usr/bin/env python3
"""
优化的数字计算模块
提供基本的数学运算和表达式计算功能
"""

import ast
import operator
from typing import Union, List


# 定义支持的运算符映射
SUPPORTED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """加法运算"""
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """减法运算"""
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """乘法运算"""
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """幂运算"""
    return base ** exponent


def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """取模运算"""
    if b == 0:
        raise ValueError("模数不能为零")
    return a % b


def square_root(n: Union[int, float]) -> float:
    """平方根运算"""
    if n < 0:
        raise ValueError("不能对负数开平方")
    return n ** 0.5


def average(numbers: List[Union[int, float]]) -> float:
    """计算平均值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return sum(numbers) / len(numbers)


def _eval_ast_node(node: ast.AST) -> Union[int, float]:
    """安全地评估 AST 节点（递归）"""
    if isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError(f"不支持的常量类型：{type(node.value)}")
    elif isinstance(node, ast.BinOp):
        left = _eval_ast_node(node.left)
        right = _eval_ast_node(node.right)
        op_type = type(node.op)
        
        if op_type not in SUPPORTED_OPERATORS:
            raise ValueError(f"不支持的运算符：{op_type.__name__}")
        
        return SUPPORTED_OPERATORS[op_type](left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = _eval_ast_node(node.operand)
        op_type = type(node.op)
        
        if op_type not in SUPPORTED_OPERATORS:
            raise ValueError(f"不支持的一元运算符：{op_type.__name__}")
        
        return SUPPORTED_OPERATORS[op_type](operand)
    else:
        raise ValueError(f"不支持的表达式类型：{type(node).__name__}")


def calculate_expression(expression: str) -> Union[int, float]:
    """安全地计算数学表达式（使用 AST 替代 eval，更安全）"""
    try:
        tree = ast.parse(expression.strip(), mode='eval')
        result = _eval_ast_node(tree.body)
        return result
    except SyntaxError as e:
        raise ValueError(f"表达式语法错误：{e}")
    except Exception as e:
        raise ValueError(f"表达式计算错误：{e}")


def main():
    """主函数 - 演示计算功能"""
    print("=" * 50)
    print("优化版数字计算逻辑")
    print("=" * 50)
    
    a, b = 10, 5
    print(f"\n【基本运算】数字：a = {a}, b = {b}\n")
    
    operations = [
        ("加法", f"{a} + {b}", add(a, b)),
        ("减法", f"{a} - {b}", subtract(a, b)),
        ("乘法", f"{a} * {b}", multiply(a, b)),
        ("除法", f"{a} / {b}", divide(a, b)),
        ("幂运算", f"{a} ** {b}", power(a, b)),
        ("取模", f"{a} % {b}", modulo(a, b)),
        ("平方根", f"√{a}", square_root(a)),
    ]
    
    for name, expr, result in operations:
        print(f"{name:8s}: {expr:15s} = {result}")
    
    numbers = [10, 20, 30, 40, 50]
    print(f"\n【平均值】{numbers} 的平均值 = {average(numbers)}")
    
    print("\n【表达式计算】")
    expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 ** 2",
        "100 / 4 + 5",
        "(-5) ** 2",
        "17 % 5",
        "2 ** 3 ** 2",
    ]
    
    for expr in expressions:
        try:
            result = calculate_expression(expr)
            print(f"  {expr:20s} = {result}")
        except ValueError as e:
            print(f"  {expr:20s} 错误：{e}")
    
    print("\n【错误处理示例】")
    error_cases = [
        ("除以零", "10 / 0"),
        ("负数开方", lambda: square_root(-4)),
        ("空列表平均", lambda: average([])),
    ]
    
    for name, case in error_cases:
        try:
            if callable(case):
                case()
            else:
                calculate_expression(case)
            print(f"  {name}: 未捕获到错误")
        except ValueError as e:
            print(f"  {name}: 捕获错误 - {e}")


if __name__ == "__main__":
    main()
