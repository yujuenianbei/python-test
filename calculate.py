#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的数字计算逻辑示例
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


def calculate(a, b, operator):
    """
    根据操作符执行相应的计算
    
    参数:
        a: 第一个数字
        b: 第二个数字
        operator: 操作符 (+, -, *, /)
    
    返回:
        计算结果
    """
    operators = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    if operator not in operators:
        raise ValueError(f"不支持的操作符：{operator}")
    
    return operators[operator](a, b)


if __name__ == "__main__":
    # 测试示例
    print("简单计算器示例")
    print("-" * 30)
    
    num1 = 10
    num2 = 5
    
    print(f"{num1} + {num2} = {calculate(num1, num2, '+')}")
    print(f"{num1} - {num2} = {calculate(num1, num2, '-')}")
    print(f"{num1} * {num2} = {calculate(num1, num2, '*')}")
    print(f"{num1} / {num2} = {calculate(num1, num2, '/')}")
