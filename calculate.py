"""
简单的数字计算逻辑模块
包含基本的数学运算功能
"""


def add(a: float, b: float) -> float:
    """加法运算"""
    return a + b


def subtract(a: float, b: float) -> float:
    """减法运算"""
    return a - b


def multiply(a: float, b: float) -> float:
    """乘法运算"""
    return a * b


def divide(a: float, b: float) -> float:
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def power(base: float, exponent: float) -> float:
    """幂运算"""
    return base ** exponent


def modulo(a: float, b: float) -> float:
    """取模运算"""
    if b == 0:
        raise ValueError("模数不能为零")
    return a % b


def calculate(expression: str) -> float:
    """
    计算简单的数学表达式
    
    参数:
        expression: 字符串形式的数学表达式，如 "2 + 3"
    
    返回:
        计算结果
    """
    try:
        # 安全的表达式计算
        allowed_chars = set('0123456789+-*/.() ')
        if not all(c in allowed_chars for c in expression):
            raise ValueError("表达式包含非法字符")
        
        return eval(expression)
    except Exception as e:
        raise ValueError(f"计算错误: {str(e)}")


if __name__ == "__main__":
    # 测试示例
    print("=== 简单数字计算逻辑测试 ===\n")
    
    # 基本运算测试
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 × 7 = {multiply(6, 7)}")
    print(f"20 ÷ 4 = {divide(20, 4)}")
    print(f"2³ = {power(2, 3)}")
    print(f"17 mod 5 = {modulo(17, 5)}")
    
    print("\n=== 表达式计算 ===")
    expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "100 / 5 + 10",
        "2 ** 3 + 1"
    ]
    
    for expr in expressions:
        result = calculate(expr)
        print(f"{expr} = {result}")
