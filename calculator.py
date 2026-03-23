"""
简单的数字计算逻辑
包含基本的加减乘除运算
"""


def add(a, b):
    """加法运算"""
    return a + b


def subtract(a, b):
    """减法运算"""
    return a - b


def multiply(a, b):
    """乘法运算"""
    return a * b


def divide(a, b):
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def calculate(a, b, operator):
    """
    根据运算符执行相应的计算
    
    参数:
        a: 第一个数字
        b: 第二个数字
        operator: 运算符 (+, -, *, /)
    
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
        raise ValueError(f"不支持的运算符: {operator}")
    
    return operators[operator](a, b)


# 示例使用
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    
    print(f"{num1} + {num2} = {calculate(num1, num2, '+')}")
    print(f"{num1} - {num2} = {calculate(num1, num2, '-')}")
    print(f"{num1} * {num2} = {calculate(num1, num2, '*')}")
    print(f"{num1} / {num2} = {calculate(num1, num2, '/')}")
