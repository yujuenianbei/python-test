#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单计算器 - 优化版
支持加减乘除运算，代码结构清晰，包含错误处理和类型提示
"""

from typing import Dict
from operator import add, sub, mul, truediv


class Calculator:
    """计算器类，封装四则运算逻辑"""
    
    def __init__(self):
        # 定义操作映射表
        self.operations: Dict[str, Dict] = {
            '1': {'name': '加法', 'symbol': '+', 'func': add},
            '2': {'name': '减法', 'symbol': '-', 'func': sub},
            '3': {'name': '乘法', 'symbol': '*', 'func': mul},
            '4': {'name': '除法', 'symbol': '/', 'func': self.safe_divide},
        }
    
    @staticmethod
    def safe_divide(a: float, b: float) -> float:
        """安全的除法运算，处理除零异常"""
        if b == 0:
            raise ZeroDivisionError("错误：除数不能为零")
        return a / b
    
    def get_number(self, prompt: str) -> float:
        """获取用户输入的数字，带错误处理"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ 输入无效，请输入数字")
    
    def display_menu(self) -> None:
        """显示操作菜单"""
        print("\n" + "=" * 30)
        print("🧮 简单计算器")
        print("=" * 30)
        for key, value in self.operations.items():
            print(f"{key}. {value['name']} ({value['symbol']})")
        print("q. 退出")
        print("=" * 30)
    
    def calculate(self, choice: str) -> None:
        """执行计算"""
        op = self.operations[choice]
        print(f"\n已选择：{op['name']}")
        
        num1 = self.get_number("请输入第一个数字: ")
        num2 = self.get_number("请输入第二个数字: ")
        
        try:
            result = op['func'](num1, num2)
            print(f"\n✅ 结果: {num1} {op['symbol']} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"\n❌ {e}")
    
    def run(self) -> None:
        """主运行循环"""
        while True:
            self.display_menu()
            choice = input("请选择操作 (1/2/3/4 或 q): ").strip().lower()
            
            if choice == 'q':
                print("👋 感谢使用，再见！")
                break
            
            if choice not in self.operations:
                print("❌ 无效选项，请重新选择")
                continue
            
            self.calculate(choice)
            
            # 询问是否继续
            cont = input("\n是否继续计算？(y/n): ").strip().lower()
            if cont != 'y':
                print("👋 感谢使用，再见！")
                break


def main():
    """程序入口"""
    calculator = Calculator()
    calculator.run()


if __name__ == "__main__":
    main()
