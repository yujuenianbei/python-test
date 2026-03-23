# 简单的数字计算逻辑

# 加法
def add(a, b):
    return a + b

# 减法
def subtract(a, b):
    return a - b

# 乘法
def multiply(a, b):
    return a * b

# 除法
def divide(a, b):
    if b == 0:
        return "错误：除数不能为零"
    return a / b

# 幂运算
def power(a, b):
    return a ** b

# 取模
def modulo(a, b):
    if b == 0:
        return "错误：除数不能为零"
    return a % b

# 主程序示例
if __name__ == "__main__":
    num1 = 10
    num2 = 3
    
    print(f"数字: {num1} 和 {num2}")
    print(f"加法: {add(num1, num2)}")
    print(f"减法: {subtract(num1, num2)}")
    print(f"乘法: {multiply(num1, num2)}")
    print(f"除法: {divide(num1, num2)}")
    print(f"幂运算: {power(num1, num2)}")
    print(f"取模: {modulo(num1, num2)}")
