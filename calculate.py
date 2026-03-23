# 简单的数字计算逻辑

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

def power(base, exponent):
    """幂运算"""
    return base ** exponent

def modulo(a, b):
    """取模运算"""
    if b == 0:
        raise ValueError("模数不能为零")
    return a % b

# 示例使用
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
    print(f"{num1} ^ {num2} = {power(num1, num2)}")
    print(f"{num1} % {num2} = {modulo(num1, num2)}")
