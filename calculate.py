#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的数字计算器
支持加、减、乘、除、幂运算和取模运算
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """加法运算"""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """减法运算"""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """乘法运算"""
    return a * b


def divide(a: Number, b: Number) -> Union[Number, str]:
    """除法运算，包含除零检查"""
    if b == 0:
        return "错误：除数不能为零"
    return a / b


def power(a: Number, b: Number) -> Number:
    """幂运算"""
    return a ** b


def modulo(a: Number, b: Number) -> Union[Number, str]:
    """取模运算，包含除零检查"""
    if b == 0:
        return "错误：除数不能为零"
    return a % b


def calculate_all(a: Number, b: Number) -> dict:
    """执行所有运算并返回结果字典"""
    return {
        "加法": add(a, b),
        "减法": subtract(a, b),
        "乘法": multiply(a, b),
        "除法": divide(a, b),
        "幂运算": power(a, b),
        "取模": modulo(a, b),
    }


def main():
    """主程序入口"""
    num1 = 10
    num2 = 3
    
    print(f"数字: {num1} 和 {num2}")
    print("-" * 30)
    
    results = calculate_all(num1, num2)
    for operation, result in results.items():
        print(f"{operation}: {result}")


if __name__ == "__main__":
    main()
