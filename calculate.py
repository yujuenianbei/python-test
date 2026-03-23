"""
优化的数字计算模块

提供基本的算术运算功能，包含类型检查、错误处理和扩展运算符支持。
"""

from typing import Union, Dict, Callable
from decimal import Decimal, getcontext
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 设置小数精度
getcontext().prec = 10

Number = Union[int, float, Decimal]


class CalculationError(Exception):
    """自定义计算异常类"""
    pass


def _validate_numbers(*args) -> None:
    """验证输入是否为有效的数字类型"""
    for i, arg in enumerate(args):
        if not isinstance(arg, (int, float, Decimal)):
            raise CalculationError(
                f"参数 {i + 1} 必须是数字类型 (int, float, Decimal)，"
                f"当前类型为: {type(arg).__name__}"
            )


def add(a: Number, b: Number) -> Number:
    """
    执行加法运算
    
    参数:
        a: 第一个数字
        b: 第二个数字
    
    返回:
        两数之和
    
    异常:
        CalculationError: 当输入不是有效数字时
    """
    _validate_numbers(a, b)
    result = a + b
    logger.debug(f"{a} + {b} = {result}")
    return result


def subtract(a: Number, b: Number) -> Number:
    """
    执行减法运算
    
    参数:
        a: 被减数
        b: 减数
    
    返回:
        两数之差
    
    异常:
        CalculationError: 当输入不是有效数字时
    """
    _validate_numbers(a, b)
    result = a - b
    logger.debug(f"{a} - {b} = {result}")
    return result


def multiply(a: Number, b: Number) -> Number:
    """
    执行乘法运算
    
    参数:
        a: 第一个乘数
        b: 第二个乘数
    
    返回:
        两数之积
    
    异常:
        CalculationError: 当输入不是有效数字时
    """
    _validate_numbers(a, b)
    result = a * b
    logger.debug(f"{a} * {b} = {result}")
    return result


def divide(a: Number, b: Number, use_decimal: bool = False) -> Number:
    """
    执行除法运算
    
    参数:
        a: 被除数
        b: 除数
        use_decimal: 是否使用 Decimal 类型进行高精度计算
    
    返回:
        两数之商
    
    异常:
        CalculationError: 当除数为零或输入不是有效数字时
    """
    _validate_numbers(a, b)
    
    if b == 0:
        raise CalculationError("除数不能为零")
    
    if use_decimal:
        result = Decimal(str(a)) / Decimal(str(b))
    else:
        result = a / b
    
    logger.debug(f"{a} / {b} = {result}")
    return result


def power(base: Number, exponent: Number) -> Number:
    """
    执行幂运算
    
    参数:
        base: 底数
        exponent: 指数
    
    返回:
        base 的 exponent 次幂
    
    异常:
        CalculationError: 当输入不是有效数字时
    """
    _validate_numbers(base, exponent)
    result = base ** exponent
    logger.debug(f"{base} ^ {exponent} = {result}")
    return result


def modulo(a: Number, b: Number) -> Number:
    """
    执行取余运算
    
    参数:
        a: 被除数
        b: 除数
    
    返回:
        余数
    
    异常:
        CalculationError: 当除数为零或输入不是有效数字时
    """
    _validate_numbers(a, b)
    
    if b == 0:
        raise CalculationError("取余运算中除数不能为零")
    
    result = a % b
    logger.debug(f"{a} % {b} = {result}")
    return result


def integer_divide(a: Number, b: Number) -> Number:
    """
    执行整除运算
    
    参数:
        a: 被除数
        b: 除数
    
    返回:
        商的整数部分
    
    异常:
        CalculationError: 当除数为零或输入不是有效数字时
    """
    _validate_numbers(a, b)
    
    if b == 0:
        raise CalculationError("整除运算中除数不能为零")
    
    result = a // b
    logger.debug(f"{a} // {b} = {result}")
    return result


# 运算符映射表
OPERATIONS: Dict[str, Callable] = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    'pow': power,
    '%': modulo,
    '//': integer_divide,
}


def calculate(a: Number, b: Number, operator: str, **kwargs) -> Number:
    """
    根据运算符执行相应的计算
    
    参数:
        a: 第一个数字
        b: 第二个数字
        operator: 运算符 (+, -, *, /, **, pow, %, //)
        **kwargs: 传递给具体运算函数的额外参数（如 use_decimal）
    
    返回:
        计算结果
    
    异常:
        CalculationError: 当运算符不支持或计算失败时
    """
    if operator not in OPERATIONS:
        supported_ops = ', '.join(OPERATIONS.keys())
        raise CalculationError(
            f"不支持的运算符：'{operator}'。支持的运算符：{supported_ops}"
        )
    
    try:
        operation_func = OPERATIONS[operator]
        return operation_func(a, b, **kwargs)
    except CalculationError:
        raise
    except Exception as e:
        raise CalculationError(f"计算失败：{str(e)}")


def calculate_expression(expression: str) -> Number:
    """
    计算简单的数学表达式字符串
    
    参数:
        expression: 数学表达式字符串（如 "10 + 20", "5 * 3"）
    
    返回:
        计算结果
    
    异常:
        CalculationError: 当表达式格式错误或计算失败时
    """
    import re
    
    # 匹配模式：数字 运算符 数字
    pattern = r'^\s*(-?\d+\.?\d*)\s*([\+\-\*/%]|\*\*|//)\s*(-?\d+\.?\d*)\s*$'
    match = re.match(pattern, expression)
    
    if not match:
        raise CalculationError(
            f"无效的表达式格式：'{expression}'。"
            f"请使用格式：'数字 运算符 数字'（如 '10 + 20'）"
        )
    
    a_str, operator, b_str = match.groups()
    
    try:
        # 尝试转换为 int，如果失败则转换为 float
        a = int(a_str) if '.' not in a_str else float(a_str)
        b = int(b_str) if '.' not in b_str else float(b_str)
    except ValueError as e:
        raise CalculationError(f"无法解析数字：{str(e)}")
    
    return calculate(a, b, operator)


if __name__ == "__main__":
    # 设置日志级别为 DEBUG 以查看详细计算过程
    logger.setLevel(logging.DEBUG)
    
    print("=" * 50)
    print("优化的数字计算模块示例")
    print("=" * 50)
    
    # 基本运算
    print("\n【基本运算】")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    
    # 扩展运算
    print("\n【扩展运算】")
    print(f"2 ^ 8 = {power(2, 8)}")
    print(f"17 % 5 = {modulo(17, 5)}")
    print(f"17 // 5 = {integer_divide(17, 5)}")
    
    # 使用通用计算函数
    print("\n【使用 calculate 函数】")
    test_cases = [
        (20, 30, '+'),
        (20, 30, '-'),
        (20, 30, '*'),
        (20, 30, '/'),
        (2, 10, '**'),
        (100, 7, '%'),
    ]
    
    for a, b, op in test_cases:
        result = calculate(a, b, op)
        print(f"{a} {op} {b} = {result}")
    
    # 高精度计算
    print("\n【高精度计算（使用 Decimal）】")
    result_normal = divide(1, 3)
    result_decimal = divide(1, 3, use_decimal=True)
    print(f"1 / 3 (普通) = {result_normal}")
    print(f"1 / 3 (高精度) = {result_decimal}")
    
    # 表达式计算
    print("\n【表达式字符串计算】")
    expressions = ["10 + 20", "100 / 4", "2 ** 10", "15 % 4"]
    for expr in expressions:
        result = calculate_expression(expr)
        print(f"'{expr}' = {result}")
    
    # 错误处理示例
    print("\n【错误处理示例】")
    try:
        divide(10, 0)
    except CalculationError as e:
        print(f"捕获异常：{e}")
    
    try:
        calculate(10, 5, '^')  # 不支持的运算符
    except CalculationError as e:
        print(f"捕获异常：{e}")
    
    try:
        add("10", 5)  # 类型错误
    except CalculationError as e:
        print(f"捕获异常：{e}")
    
    print("\n" + "=" * 50)
    print("演示完成！")
    print("=" * 50)
