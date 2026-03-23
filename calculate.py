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
    根据运算符执行相应的计算
    
    参数:
        a: 第一个数字
        b: 第二个数字
        operator: 运算符 (+, -, *, /)
    
    返回:
        计算结果
    """
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    if operator not in operations:
        raise ValueError(f"不支持的运算符：{operator}")
    
    return operations[operator](a, b)


# 使用示例
if __name__ == "__main__":
    # 基本运算
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    
    # 使用通用计算函数
    print(f"\n使用 calculate 函数:")
    print(f"20 + 30 = {calculate(20, 30, '+')}")
    print(f"20 - 30 = {calculate(20, 30, '-')}")
    print(f"20 * 30 = {calculate(20, 30, '*')}")
    print(f"20 / 30 = {calculate(20, 30, '/')}")
