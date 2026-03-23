"""
勾股定理计算模块

提供基于勾股定理 (a² + b² = c²) 的直角三角形边长计算功能。
支持已知两边求第三边，并包含输入验证和异常处理。
"""

import math
from typing import Optional, Union


class PythagoreanCalculator:
    """勾股定理计算器类"""

    @staticmethod
    def validate_side(value: Union[int, float], name: str = "边长") -> float:
        """
        验证边长是否为有效的正数
        
        Args:
            value: 待验证的边长值
            name: 边长名称（用于错误提示）
            
        Returns:
            转换为 float 的有效边长
            
        Raises:
            TypeError: 当输入不是数字类型时
            ValueError: 当输入不是正数时
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name}必须是数字类型，当前类型为: {type(value).__name__}")
        
        value = float(value)
        
        if value <= 0:
            raise ValueError(f"{name}必须是正数，当前值为: {value}")
        
        if math.isinf(value) or math.isnan(value):
            raise ValueError(f"{name}必须是有限的实数，当前值为: {value}")
        
        return value

    @classmethod
    def calculate_hypotenuse(cls, a: Union[int, float], b: Union[int, float]) -> float:
        """
        已知两条直角边，计算斜边长度
        
        公式: c = √(a² + b²)
        
        Args:
            a: 第一条直角边长度
            b: 第二条直角边长度
            
        Returns:
            斜边长度
            
        Raises:
            TypeError: 当输入不是数字类型时
            ValueError: 当输入不是正数时
        """
        a = cls.validate_side(a, "直角边a")
        b = cls.validate_side(b, "直角边b")
        
        return math.sqrt(a ** 2 + b ** 2)

    @classmethod
    def calculate_leg(cls, hypotenuse: Union[int, float], 
                     other_leg: Union[int, float]) -> float:
        """
        已知斜边和一条直角边，计算另一条直角边长度
        
        公式: a = √(c² - b²)
        
        Args:
            hypotenuse: 斜边长度
            other_leg: 已知的另一条直角边长度
            
        Returns:
            未知的直角边长度
            
        Raises:
            TypeError: 当输入不是数字类型时
            ValueError: 当输入不是正数，或斜边不大于已知直角边时
        """
        c = cls.validate_side(hypotenuse, "斜边")
        b = cls.validate_side(other_leg, "已知直角边")
        
        if c <= b:
            raise ValueError(
                f"斜边({c})必须大于直角边({b})，否则无法构成直角三角形"
            )
        
        return math.sqrt(c ** 2 - b ** 2)

    @classmethod
    def calculate(cls, a: Optional[Union[int, float]] = None,
                  b: Optional[Union[int, float]] = None,
                  c: Optional[Union[int, float]] = None) -> dict:
        """
        智能计算：根据已知的两个边长，自动计算第三个边长
        
        Args:
            a: 直角边a（可选）
            b: 直角边b（可选）
            c: 斜边c（可选）
            
        Returns:
            包含所有三条边长的字典，格式为:
            {'a': float, 'b': float, 'c': float, 'calculation_type': str}
            
        Raises:
            ValueError: 当提供的已知条件不足或过多，或数据不合法时
        """
        # 统计已知的边长数量
        known_sides = {
            'a': a if a is not None else None,
            'b': b if b is not None else None,
            'c': c if c is not None else None
        }
        
        known_count = sum(1 for v in known_sides.values() if v is not None)
        
        if known_count != 2:
            raise ValueError(
                f"必须且只能提供两条边的长度，当前提供了 {known_count} 条"
            )
        
        result = {}
        
        # 情况1: 已知两条直角边，求斜边
        if a is not None and b is not None:
            result['a'] = cls.validate_side(a, "直角边a")
            result['b'] = cls.validate_side(b, "直角边b")
            result['c'] = cls.calculate_hypotenuse(a, b)
            result['calculation_type'] = '已知两直角边求斜边'
        
        # 情况2: 已知直角边a和斜边，求直角边b
        elif a is not None and c is not None:
            result['a'] = cls.validate_side(a, "直角边a")
            result['c'] = cls.validate_side(c, "斜边")
            result['b'] = cls.calculate_leg(c, a)
            result['calculation_type'] = '已知直角边a和斜边求直角边b'
        
        # 情况3: 已知直角边b和斜边，求直角边a
        elif b is not None and c is not None:
            result['b'] = cls.validate_side(b, "直角边b")
            result['c'] = cls.validate_side(c, "斜边")
            result['a'] = cls.calculate_leg(c, b)
            result['calculation_type'] = '已知直角边b和斜边求直角边a'
        
        return result


def main():
    """主函数：演示勾股定理计算器的使用"""
    print("=" * 60)
    print("勾股定理计算器演示")
    print("=" * 60)
    
    calculator = PythagoreanCalculator()
    
    # 示例1: 经典勾股数 3-4-5
    print("\n【示例1】已知两条直角边 (a=3, b=4)，求斜边:")
    try:
        result = calculator.calculate(a=3, b=4)
        print(f"  结果: a={result['a']}, b={result['b']}, c={result['c']}")
        print(f"  计算类型: {result['calculation_type']}")
    except Exception as e:
        print(f"  错误: {e}")
    
    # 示例2: 已知斜边和一条直角边
    print("\n【示例2】已知直角边 (a=5) 和斜边 (c=13)，求另一条直角边:")
    try:
        result = calculator.calculate(a=5, c=13)
        print(f"  结果: a={result['a']}, b={result['b']}, c={result['c']}")
        print(f"  计算类型: {result['calculation_type']}")
    except Exception as e:
        print(f"  错误: {e}")
    
    # 示例3: 使用小数
    print("\n【示例3】使用小数计算 (a=1.5, b=2.5)，求斜边:")
    try:
        result = calculator.calculate(a=1.5, b=2.5)
        print(f"  结果: a={result['a']}, b={result['b']}, c={result['c']:.4f}")
        print(f"  计算类型: {result['calculation_type']}")
    except Exception as e:
        print(f"  错误: {e}")
    
    # 示例4: 错误处理 - 斜边小于直角边
    print("\n【示例4】错误演示 - 斜边小于直角边 (a=10, c=5):")
    try:
        result = calculator.calculate(a=10, c=5)
        print(f"  结果: {result}")
    except Exception as e:
        print(f"  预期错误: {e}")
    
    # 示例5: 错误处理 - 输入负数
    print("\n【示例5】错误演示 - 输入负数 (a=-3, b=4):")
    try:
        result = calculator.calculate(a=-3, b=4)
        print(f"  结果: {result}")
    except Exception as e:
        print(f"  预期错误: {e}")
    
    # 示例6: 错误处理 - 已知条件不足
    print("\n【示例6】错误演示 - 只提供一条边 (a=3):")
    try:
        result = calculator.calculate(a=3)
        print(f"  结果: {result}")
    except Exception as e:
        print(f"  预期错误: {e}")
    
    print("\n" + "=" * 60)
    print("演示结束")
    print("=" * 60)


if __name__ == "__main__":
    main()
