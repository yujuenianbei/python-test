"""
勾股定理计算器
用于计算直角三角形的边长：a² + b² = c²
"""

import math
from typing import Optional, Union


def calculate_hypotenuse(a: float, b: float) -> float:
    """
    已知两条直角边，计算斜边
    
    Args:
        a: 直角边1的长度
        b: 直角边2的长度
        
    Returns:
        斜边的长度
        
    Raises:
        ValueError: 当边长不是正数时
        TypeError: 当输入不是数字时
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("边长必须是数字")
    if a <= 0 or b <= 0:
        raise ValueError("边长必须是正数")
    
    return math.sqrt(a**2 + b**2)


def calculate_leg(hypotenuse: float, leg: float) -> float:
    """
    已知斜边和一条直角边，计算另一条直角边
    
    Args:
        hypotenuse: 斜边的长度
        leg: 已知直角边的长度
        
    Returns:
        另一条直角边的长度
        
    Raises:
        ValueError: 当边长不是正数或斜边不大于已知直角边时
        TypeError: 当输入不是数字时
    """
    if not isinstance(hypotenuse, (int, float)) or not isinstance(leg, (int, float)):
        raise TypeError("边长必须是数字")
    if hypotenuse <= 0 or leg <= 0:
        raise ValueError("边长必须是正数")
    if hypotenuse <= leg:
        raise ValueError("斜边必须大于任意一条直角边")
    
    return math.sqrt(hypotenuse**2 - leg**2)


def pythagorean_calculator(
    a: Optional[float] = None,
    b: Optional[float] = None,
    c: Optional[float] = None
) -> dict:
    """
    通用的勾股定理计算器
    提供三个参数中的任意两个，计算第三个
    
    Args:
        a: 直角边1（可选）
        b: 直角边2（可选）
        c: 斜边（可选）
        
    Returns:
        包含所有三条边长度的字典
        
    Raises:
        ValueError: 当提供的参数数量不是2个或参数值无效时
    """
    provided = sum(1 for x in [a, b, c] if x is not None)
    
    if provided != 2:
        raise ValueError(f"必须且只能提供两个边长值，当前提供了 {provided} 个")
    
    # 验证所有提供的值都是正数
    for name, value in [('a', a), ('b', b), ('c', c)]:
        if value is not None:
            if not isinstance(value, (int, float)):
                raise TypeError(f"{name} 必须是数字")
            if value <= 0:
                raise ValueError(f"{name} 必须是正数")
    
    result = {'a': a, 'b': b, 'c': c}
    
    if c is None:
        # 已知 a 和 b，求 c
        result['c'] = calculate_hypotenuse(a, b)
    elif a is None:
        # 已知 b 和 c，求 a
        result['a'] = calculate_leg(c, b)
    else:
        # 已知 a 和 c，求 b
        result['b'] = calculate_leg(c, a)
    
    # 保留6位小数
    result = {k: round(v, 6) if v is not None else None for k, v in result.items()}
    
    return result


if __name__ == "__main__":
    print("=" * 50)
    print("勾股定理计算器 (a² + b² = c²)")
    print("=" * 50)
    
    # 示例1：已知两条直角边，求斜边
    print("\n【示例1】已知直角边 a=3, b=4，求斜边 c")
    try:
        result = pythagorean_calculator(a=3, b=4)
        print(f"结果: a={result['a']}, b={result['b']}, c={result['c']}")
        print(f"验证: {result['a']}² + {result['b']}² = {result['a']**2 + result['b']**2}, c² = {result['c']**2}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 示例2：已知斜边和一条直角边，求另一条直角边
    print("\n【示例2】已知斜边 c=13, 直角边 a=5，求直角边 b")
    try:
        result = pythagorean_calculator(a=5, c=13)
        print(f"结果: a={result['a']}, b={result['b']}, c={result['c']}")
        print(f"验证: {result['a']}² + {result['b']}² = {result['a']**2 + result['b']**2}, c² = {result['c']**2}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 示例3：经典勾股数 5-12-13
    print("\n【示例3】已知直角边 b=12, 斜边 c=13，求直角边 a")
    try:
        result = pythagorean_calculator(b=12, c=13)
        print(f"结果: a={result['a']}, b={result['b']}, c={result['c']}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 示例4：错误处理 - 参数不足
    print("\n【示例4】错误演示：只提供一个参数")
    try:
        result = pythagorean_calculator(a=5)
    except Exception as e:
        print(f"错误: {e}")
    
    # 示例5：错误处理 - 斜边不大于直角边
    print("\n【示例5】错误演示：斜边小于直角边（不合法）")
    try:
        result = pythagorean_calculator(a=10, c=5)
    except Exception as e:
        print(f"错误: {e}")
    
    # 示例6：浮点数计算
    print("\n【示例6】浮点数计算：a=1.5, b=2.5")
    try:
        result = pythagorean_calculator(a=1.5, b=2.5)
        print(f"结果: a={result['a']}, b={result['b']}, c={result['c']}")
    except Exception as e:
        print(f"错误: {e}")
    
    print("\n" + "=" * 50)
