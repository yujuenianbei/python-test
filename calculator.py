"""
简单的数字计算器模块
支持加、减、乘、除四则运算
"""

from typing import Callable, Dict
from functools import lru_cache


@lru_cache(maxsize=128)
def add(a: float, b: float) -> float:
    """加法运算"""
    return a + b


@lru_cache(maxsize=128)
def subtract(a: float, b: float) -> float:
    """减法运算"""
    return a - b


@lru_cache(maxsize=128)
def multiply(a: float, b: float) -> float:
    """乘法运算"""
    return a * b


def divide(a: float, b: float) -> float:
    """
    除法运算
    
    Args:
        a: 被除数
        b: 除数
        
    Returns:
        商
        
    Raises:
        ZeroDivisionError: 当除数为零时
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为零")
    return a / b


class Calculator:
    """计算器类，封装基本运算功能"""
    
    OPERATIONS: Dict[str, Callable[[float, float], float]] = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    @classmethod
    def calculate(cls, a: float, b: float, operator: str) -> float:
        """
        根据运算符执行计算
        
        Args:
            a: 第一个操作数
            b: 第二个操作数
            operator: 运算符 (+, -, *, /) 或操作名称 (add, subtract, multiply, divide)
            
        Returns:
            计算结果
            
        Raises:
            ValueError: 当运算符不支持时
            ZeroDivisionError: 当除数为零时
        """
        if operator not in cls.OPERATIONS:
            raise ValueError(
                f"不支持的运算符: {operator}\n"
                f"支持的运算符: {', '.join(cls.OPERATIONS.keys())}"
            )
        
        return cls.OPERATIONS[operator](a, b)
    
    @staticmethod
    def batch_calculate(operations: list) -> list:
        """
        批量执行计算
        
        Args:
            operations: 包含 (a, b, operator) 元组的列表
            
        Returns:
            计算结果列表
        """
        results = []
        for a, b, op in operations:
            try:
                result = Calculator.calculate(a, b, op)
                results.append({'operation': f"{a} {op} {b}", 'result': result, 'error': None})
            except Exception as e:
                results.append({'operation': f"{a} {op} {b}", 'result': None, 'error': str(e)})
        return results


if __name__ == "__main__":
    print("=" * 50)
    print("简单计算器示例")
    print("=" * 50)
    
    # 单个计算示例
    examples = [
        (5, 3, '+'),
        (10, 4, '-'),
        (6, 7, '*'),
        (20, 4, '/'),
        (15, 0, '/'),  # 测试除零错误
        (5, 3, '^')   # 测试不支持的运算符
    ]
    
    for a, b, op in examples:
        try:
            result = Calculator.calculate(a, b, op)
            print(f"{a} {op} {b} = {result}")
        except Exception as e:
            print(f"{a} {op} {b} 出错: {e}")
    
    print("\n" + "=" * 50)
    print("批量计算示例")
    print("=" * 50)
    
    batch_ops = [
        (10, 5, '+'),
        (10, 5, '-'),
        (10, 5, '*'),
        (10, 5, '/'),
        (10, 0, '/')
    ]
    
    results = Calculator.batch_calculate(batch_ops)
    for item in results:
        if item['error']:
            print(f"{item['operation']} 出错: {item['error']}")
        else:
            print(f"{item['operation']} = {item['result']}")
