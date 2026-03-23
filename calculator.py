# 简单的数字计算逻辑

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
    """根据运算符执行计算"""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    if operator not in operations:
        raise ValueError(f"不支持的运算符: {operator}")
    
    return operations[operator](a, b)

# 示例使用
if __name__ == "__main__":
    print("简单计算器示例:")
    print(f"5 + 3 = {calculate(5, 3, '+')}")
    print(f"10 - 4 = {calculate(10, 4, '-')}")
    print(f"6 * 7 = {calculate(6, 7, '*')}")
    print(f"20 / 4 = {calculate(20, 4, '/')}")
