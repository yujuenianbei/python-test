"""
勾股定理计算模块

提供基于勾股定理 (a² + b² = c²) 的各种计算功能：
- 已知两条直角边，求斜边
- 已知一条直角边和斜边，求另一条直角边
- 验证三边是否构成直角三角形
"""

import math
from typing import Union, Tuple, Optional
from dataclasses import dataclass


@dataclass
class TriangleResult:
    """三角形计算结果数据类"""
    side_a: float
    side_b: float
    hypotenuse: float
    is_right_triangle: bool
    area: float
    perimeter: float
    
    def __str__(self) -> str:
        return (
            f"直角三角形结果:\n"
            f"  直角边 a: {self.side_a:.4f}\n"
            f"  直角边 b: {self.side_b:.4f}\n"
            f"  斜边 c:   {self.hypotenuse:.4f}\n"
            f"  面积:     {self.area:.4f}\n"
            f"  周长:     {self.perimeter:.4f}\n"
            f"  是否为直角三角形: {self.is_right_triangle}"
        )


class PythagoreanCalculator:
    """勾股定理计算器"""
    
    # 浮点数比较的容差值
    TOLERANCE = 1e-9
    
    @staticmethod
    def validate_positive(value: Union[int, float], name: str = "value") -> float:
        """
        验证数值是否为正数
        
        Args:
            value: 要验证的数值
            name: 参数名称，用于错误提示
            
        Returns:
            转换后的浮点数
            
        Raises:
            ValueError: 当数值非正数时
            TypeError: 当数值类型不正确时
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} 必须是数字类型，得到 {type(value).__name__}")
        
        if value <= 0:
            raise ValueError(f"{name} 必须是正数，得到 {value}")
        
        return float(value)
    
    @classmethod
    def calculate_hypotenuse(cls, a: Union[int, float], b: Union[int, float]) -> float:
        """
        已知两条直角边，计算斜边
        
        公式: c = √(a² + b²)
        
        Args:
            a: 第一条直角边长度
            b: 第二条直角边长度
            
        Returns:
            斜边长度
            
        Raises:
            ValueError: 当边长非正数时
            TypeError: 当边长类型不正确时
            
        Examples:
            >>> PythagoreanCalculator.calculate_hypotenuse(3, 4)
            5.0
            >>> PythagoreanCalculator.calculate_hypotenuse(5, 12)
            13.0
        """
        a = cls.validate_positive(a, "直角边 a")
        b = cls.validate_positive(b, "直角边 b")
        
        return math.sqrt(a ** 2 + b ** 2)
    
    @classmethod
    def calculate_leg(cls, hypotenuse: Union[int, float], 
                     known_leg: Union[int, float]) -> float:
        """
        已知斜边和一条直角边，计算另一条直角边
        
        公式: unknown_leg = √(hypotenuse² - known_leg²)
        
        Args:
            hypotenuse: 斜边长度
            known_leg: 已知的直角边长度
            
        Returns:
            未知的直角边长度
            
        Raises:
            ValueError: 当边长非正数或斜边不大于直角边时
            TypeError: 当边长类型不正确时
            
        Examples:
            >>> PythagoreanCalculator.calculate_leg(5, 3)
            4.0
            >>> PythagoreanCalculator.calculate_leg(13, 5)
            12.0
        """
        hypotenuse = cls.validate_positive(hypotenuse, "斜边")
        known_leg = cls.validate_positive(known_leg, "已知直角边")
        
        if hypotenuse <= known_leg:
            raise ValueError(
                f"斜边 ({hypotenuse}) 必须大于直角边 ({known_leg})"
            )
        
        return math.sqrt(hypotenuse ** 2 - known_leg ** 2)
    
    @classmethod
    def is_right_triangle(cls, a: Union[int, float], 
                         b: Union[int, float], 
                         c: Union[int, float]) -> bool:
        """
        判断三条边是否能构成直角三角形
        
        检查是否满足 a² + b² = c² (考虑浮点数精度)
        
        Args:
            a: 第一条边
            b: 第二条边
            c: 第三条边（假设为斜边）
            
        Returns:
            如果能构成直角三角形返回 True，否则返回 False
            
        Examples:
            >>> PythagoreanCalculator.is_right_triangle(3, 4, 5)
            True
            >>> PythagoreanCalculator.is_right_triangle(5, 12, 13)
            True
            >>> PythagoreanCalculator.is_right_triangle(1, 1, 1)
            False
        """
        try:
            a = cls.validate_positive(a, "边 a")
            b = cls.validate_positive(b, "边 b")
            c = cls.validate_positive(c, "边 c")
        except (ValueError, TypeError):
            return False
        
        # 找出最长的边作为斜边
        sides = sorted([a, b, c])
        leg1, leg2, hyp = sides[0], sides[1], sides[2]
        
        # 检查勾股定理是否成立（考虑浮点数精度）
        left_side = leg1 ** 2 + leg2 ** 2
        right_side = hyp ** 2
        
        return abs(left_side - right_side) < cls.TOLERANCE
    
    @classmethod
    def calculate_triangle(cls, *, 
                          a: Optional[Union[int, float]] = None,
                          b: Optional[Union[int, float]] = None,
                          c: Optional[Union[int, float]] = None) -> TriangleResult:
        """
        根据已知的两边计算完整的三角形信息
        
        支持三种情况：
        1. 已知 a 和 b，计算 c
        2. 已知 a 和 c，计算 b
        3. 已知 b 和 c，计算 a
        
        Args:
            a: 直角边 a
            b: 直角边 b
            c: 斜边
            
        Returns:
            TriangleResult 对象，包含所有三角形信息
            
        Raises:
            ValueError: 当提供的参数数量不正确或数值无效时
            
        Examples:
            >>> result = PythagoreanCalculator.calculate_triangle(a=3, b=4)
            >>> result.hypotenuse
            5.0
        """
        provided = [x for x in [a, b, c] if x is not None]
        
        if len(provided) != 2:
            raise ValueError("必须且只能提供两个边的值")
        
        if any(x is not None and x <= 0 for x in [a, b, c]):
            raise ValueError("所有边长必须为正数")
        
        # 情况 1: 已知两条直角边，求斜边
        if a is not None and b is not None:
            hypotenuse = cls.calculate_hypotenuse(a, b)
            side_a, side_b = a, b
            
        # 情况 2: 已知直角边 a 和斜边，求直角边 b
        elif a is not None and c is not None:
            side_b = cls.calculate_leg(c, a)
            side_a, hypotenuse = a, c
            
        # 情况 3: 已知直角边 b 和斜边，求直角边 a
        elif b is not None and c is not None:
            side_a = cls.calculate_leg(c, b)
            side_b, hypotenuse = b, c
            
        else:
            raise ValueError("无效的边组合")
        
        # 计算面积和周长
        area = 0.5 * side_a * side_b
        perimeter = side_a + side_b + hypotenuse
        
        # 验证是否为直角三角形（应该是）
        is_right = cls.is_right_triangle(side_a, side_b, hypotenuse)
        
        return TriangleResult(
            side_a=side_a,
            side_b=side_b,
            hypotenuse=hypotenuse,
            is_right_triangle=is_right,
            area=area,
            perimeter=perimeter
        )
    
    @classmethod
    def generate_pythagorean_triples(cls, limit: int) -> list[Tuple[int, int, int]]:
        """
        生成指定范围内的所有勾股数三元组
        
        勾股数是指满足 a² + b² = c² 的三个正整数
        
        Args:
            limit: 生成的勾股数中最大边的上限
            
        Returns:
            包含所有勾股数三元组的列表，每个元组为 (a, b, c)
            
        Examples:
            >>> PythagoreanCalculator.generate_pythagorean_triples(20)
            [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)]
        """
        if limit < 5:
            return []
        
        triples = []
        
        for a in range(1, limit + 1):
            for b in range(a, limit + 1):  # b >= a 避免重复
                c_squared = a ** 2 + b ** 2
                c = int(math.sqrt(c_squared))
                
                if c > limit:
                    break
                
                if c * c == c_squared:
                    triples.append((a, b, c))
        
        return triples


# 便捷函数
def calc_hypotenuse(a: Union[int, float], b: Union[int, float]) -> float:
    """快捷计算斜边"""
    return PythagoreanCalculator.calculate_hypotenuse(a, b)


def calc_leg(hypotenuse: Union[int, float], known_leg: Union[int, float]) -> float:
    """快捷计算直角边"""
    return PythagoreanCalculator.calculate_leg(hypotenuse, known_leg)


def is_right_triangle(a: Union[int, float], b: Union[int, float], 
                     c: Union[int, float]) -> bool:
    """快捷判断是否为直角三角形"""
    return PythagoreanCalculator.is_right_triangle(a, b, c)


if __name__ == "__main__":
    # 示例用法
    print("=== 勾股定理计算器示例 ===\n")
    
    # 示例 1: 已知两条直角边求斜边
    print("示例 1: 已知直角边 3 和 4，求斜边")
    c = calc_hypotenuse(3, 4)
    print(f"斜边长度: {c}\n")
    
    # 示例 2: 已知斜边和一条直角边求另一条
    print("示例 2: 已知斜边 13 和直角边 5，求另一条直角边")
    b = calc_leg(13, 5)
    print(f"另一条直角边长度: {b}\n")
    
    # 示例 3: 验证是否为直角三角形
    print("示例 3: 验证 (5, 12, 13) 是否为直角三角形")
    result = is_right_triangle(5, 12, 13)
    print(f"结果: {result}\n")
    
    # 示例 4: 完整三角形计算
    print("示例 4: 完整三角形计算 (a=6, b=8)")
    triangle = PythagoreanCalculator.calculate_triangle(a=6, b=8)
    print(triangle)
    print()
    
    # 示例 5: 生成勾股数
    print("示例 5: 生成 50 以内的勾股数")
    triples = PythagoreanCalculator.generate_pythagorean_triples(50)
    for triple in triples:
        print(f"  {triple[0]}² + {triple[1]}² = {triple[2]}²")
