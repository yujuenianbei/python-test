#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
勾股定理计算器
根据勾股定理：a² + b² = c²
可以计算直角三角形的任意一边
"""

import math


def calculate_hypotenuse(a, b):
    """已知两条直角边，计算斜边"""
    return math.sqrt(a ** 2 + b ** 2)


def calculate_leg(c, leg):
    """已知斜边和一条直角边，计算另一条直角边"""
    if c <= leg:
        raise ValueError("斜边必须大于直角边")
    return math.sqrt(c ** 2 - leg ** 2)


def main():
    print("=" * 50)
    print("勾股定理计算器")
    print("=" * 50)
    print("\n请选择计算类型：")
    print("1. 已知两条直角边，求斜边 (a² + b² = c²)")
    print("2. 已知斜边和一条直角边，求另一条直角边 (c² - a² = b²)")
    print("3. 验证三边是否构成直角三角形")
    print("0. 退出")
    
    while True:
        choice = input("\n请输入选项 (0-3): ").strip()
        
        if choice == "0":
            print("再见！")
            break
        
        elif choice == "1":
            try:
                a = float(input("请输入直角边 a 的长度: "))
                b = float(input("请输入直角边 b 的长度: "))
                if a <= 0 or b <= 0:
                    print("错误：边长必须为正数！")
                    continue
                c = calculate_hypotenuse(a, b)
                print(f"\n结果：斜边 c = {c:.6f}")
                print(f"验证：{a}² + {b}² = {a**2 + b**2:.6f}, {c}² = {c**2:.6f}")
            except ValueError as e:
                print(f"输入错误：{e}")
        
        elif choice == "2":
            try:
                c = float(input("请输入斜边 c 的长度: "))
                leg = float(input("请输入已知直角边的长度: "))
                if c <= 0 or leg <= 0:
                    print("错误：边长必须为正数！")
                    continue
                result = calculate_leg(c, leg)
                print(f"\n结果：另一条直角边 = {result:.6f}")
            except ValueError as e:
                print(f"输入错误：{e}")
        
        elif choice == "3":
            try:
                a = float(input("请输入第一条边: "))
                b = float(input("请输入第二条边: "))
                c = float(input("请输入第三条边: "))
                if a <= 0 or b <= 0 or c <= 0:
                    print("错误：边长必须为正数！")
                    continue
                
                # 找出最长边作为斜边
                sides = sorted([a, b, c])
                if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10:
                    print(f"\n✓ 这三条边可以构成直角三角形！")
                    print(f"  {sides[0]}² + {sides[1]}² = {sides[0]**2 + sides[1]**2:.6f}")
                    print(f"  {sides[2]}² = {sides[2]**2:.6f}")
                else:
                    print(f"\n✗ 这三条边不能构成直角三角形")
                    print(f"  {sides[0]}² + {sides[1]}² = {sides[0]**2 + sides[1]**2:.6f}")
                    print(f"  {sides[2]}² = {sides[2]**2:.6f}")
            except ValueError as e:
                print(f"输入错误：{e}")
        
        else:
            print("无效选项，请重新选择")


if __name__ == "__main__":
    main()
