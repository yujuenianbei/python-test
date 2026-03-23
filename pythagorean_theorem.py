"""
勾股定理计算器
勾股定理：在直角三角形中，两条直角边的平方和等于斜边的平方
公式：a² + b² = c²
其中 a 和 b 是直角边，c 是斜边
"""

import math


def calculate_hypotenuse(a, b):
    """
    已知两条直角边，计算斜边
    
    参数:
        a: 直角边1
        b: 直角边2
    
    返回:
        斜边长度
    """
    if a <= 0 or b <= 0:
        raise ValueError("直角边长度必须为正数")
    
    c = math.sqrt(a**2 + b**2)
    return c


def calculate_leg(leg, hypotenuse):
    """
    已知一条直角边和斜边，计算另一条直角边
    
    参数:
        leg: 已知的直角边
        hypotenuse: 斜边
    
    返回:
        另一条直角边长度
    """
    if leg <= 0 or hypotenuse <= 0:
        raise ValueError("边长必须为正数")
    
    if hypotenuse <= leg:
        raise ValueError("斜边必须大于直角边")
    
    other_leg = math.sqrt(hypotenuse**2 - leg**2)
    return other_leg


def verify_pythagorean_theorem(a, b, c):
    """
    验证三个边长是否符合勾股定理
    
    参数:
        a, b: 直角边
        c: 斜边
    
    返回:
        布尔值，表示是否符合勾股定理（允许小的浮点误差）
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # 使用小的容差值来处理浮点数精度问题
    tolerance = 1e-9
    return abs(a**2 + b**2 - c**2) < tolerance


# 示例使用
if __name__ == "__main__":
    print("=== 勾股定理计算器 ===\n")
    
    # 示例1：已知两条直角边，求斜边
    a, b = 3, 4
    c = calculate_hypotenuse(a, b)
    print(f"示例1：已知直角边 a={a}, b={b}")
    print(f"斜边 c = √({a}² + {b}²) = √{a**2 + b**2} = {c}")
    print()
    
    # 示例2：已知一条直角边和斜边，求另一条直角边
    leg, hyp = 5, 13
    other_leg = calculate_leg(leg, hyp)
    print(f"示例2：已知直角边={leg}, 斜边={hyp}")
    print(f"另一条直角边 = √({hyp}² - {leg}²) = √{hyp**2 - leg**2} = {other_leg}")
    print()
    
    # 示例3：验证勾股定理
    test_cases = [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (6, 8, 10)
    ]
    
    print("示例3：验证勾股定理")
    for a, b, c in test_cases:
        is_valid = verify_pythagorean_theorem(a, b, c)
        status = "✓ 符合" if is_valid else "✗ 不符合"
        print(f"  ({a}, {b}, {c}): {status}")
