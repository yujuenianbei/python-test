#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "错误：除数不能为零"
    return x / y

def main():
    print("简单计算器")
    print("选择运算：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")

    choice = input("请输入选择 (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("无效的选择")
        return

    try:
        num1 = float(input("输入第一个数字: "))
        num2 = float(input("输入第二个数字: "))
    except ValueError:
        print("无效的数字输入")
        return

    if choice == '1':
        result = add(num1, num2)
        op = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        op = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        op = "*"
    elif choice == '4':
        result = divide(num1, num2)
        op = "/"

    print(f"{num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()
