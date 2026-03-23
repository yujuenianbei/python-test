"""
优化的数字计算逻辑模块
提供安全、高效的数学运算功能
"""

import ast
import operator
from typing import Union, List
from functools import reduce


# 定义支持的运算符映射
SUPPORTED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


class CalculationError(Exception):
    """自定义计算异常类"""
    pass


def _safe_eval_node(node: ast.AST) -> Union[int, float]:
    """
    安全地评估 AST 节点
    
    参数:
        node: AST 节点
        
    返回:
        计算结果
        
    异常:
        CalculationError: 当遇到不支持的节点类型时
    """
    if isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise CalculationError(f"不支持的常量类型: {type(node.value)}")
    elif isinstance(node, ast.BinOp):
        left = _safe_eval_node(node.left)
        right = _safe_eval_node(node.right)
        op_type = type(node.op)
        
        if op_type not in SUPPORTED_OPERATORS:
            raise CalculationError(f"不支持的运算符: {op_type.__name__}")
        
        # 特殊处理除法和取模的零检查
        if op_type in (ast.Div, ast.FloorDiv, ast.Mod) and right == 0:
            raise CalculationError("除数不能为零")
        
        try:
            return SUPPORTED_OPERATORS[op_type](left, right)
        except OverflowError:
            raise CalculationError("数值溢出")
        except Exception as e:
            raise CalculationError(f"运算错误: {str(e)}")
    
    elif isinstance(node, ast.UnaryOp):
        operand = _safe_eval_node(node.operand)
        op_type = type(node.op)
        
        if op_type not in SUPPORTED_OPERATORS:
            raise CalculationError(f"不支持的一元运算符: {op_type.__name__}")
        
        return SUPPORTED_OPERATORS[op_type](operand)
    
    elif isinstance(node, ast.Expression):
        return _safe_eval_node(node.body)
    
    else:
        raise CalculationError(f"不支持的表达式类型: {type(node).__name__}")


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    加法运算
    
    参数:
        a: 第一个操作数
        b: 第二个操作数
        
    返回:
        两数之和
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    减法运算
    
    参数:
        a: 被减数
        b: 减数
        
    返回:
        两数之差
    """
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    乘法运算
    
    参数:
        a: 第一个操作数
        b: 第二个操作数
        
    返回:
        两数之积
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    除法运算
    
    参数:
        a: 被除数
        b: 除数
        
    返回:
        两数之商
        
    异常:
        CalculationError: 当除数为零时
    """
    if b == 0:
        raise CalculationError("除数不能为零")
    return a / b


def floor_divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    地板除法运算（向下取整）
    
    参数:
        a: 被除数
        b: 除数
        
    返回:
        两数之商（向下取整）
        
    异常:
        CalculationError: 当除数为零时
    """
    if b == 0:
        raise CalculationError("除数不能为零")
    return a // b


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    幂运算
    
    参数:
        base: 底数
        exponent: 指数
        
    返回:
        base 的 exponent 次幂
        
    异常:
        CalculationError: 当结果溢出时
    """
    try:
        result = base ** exponent
        if isinstance(result, complex) or (isinstance(result, float) and 
            (result != result or abs(result) == float('inf'))):
            raise CalculationError("无效的幂运算结果")
        return result
    except OverflowError:
        raise CalculationError("数值溢出")


def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    取模运算
    
    参数:
        a: 被模数
        b: 模数
        
    返回:
        取模结果
        
    异常:
        CalculationError: 当模数为零时
    """
    if b == 0:
        raise CalculationError("模数不能为零")
    return a % b


def square_root(a: Union[int, float]) -> float:
    """
    平方根运算
    
    参数:
        a: 非负数
        
    返回:
        a 的平方根
        
    异常:
        CalculationError: 当输入为负数时
    """
    if a < 0:
        raise CalculationError("不能对负数开平方")
    return a ** 0.5


def absolute(a: Union[int, float]) -> Union[int, float]:
    """
    绝对值运算
    
    参数:
        a: 任意实数
        
    返回:
        a 的绝对值
    """
    return abs(a)


def negate(a: Union[int, float]) -> Union[int, float]:
    """
    取负运算
    
    参数:
        a: 任意实数
        
    返回:
        a 的相反数
    """
    return -a


def calculate(expression: str) -> Union[int, float]:
    """
    安全地计算数学表达式
    
    支持的运算符: +, -, *, /, //, %, **, 一元负号
    支持括号和数字（整数和浮点数）
    
    参数:
        expression: 字符串形式的数学表达式，如 "2 + 3 * 4"
        
    返回:
        计算结果
        
    异常:
        CalculationError: 当表达式无效或包含不支持的操作时
        
    示例:
        >>> calculate("2 + 3")
        5
        >>> calculate("(2 + 3) * 4")
        20
        >>> calculate("2 ** 3")
        8
    """
    if not expression or not isinstance(expression, str):
        raise CalculationError("表达式必须是非空字符串")
    
    # 移除空白字符
    expression = expression.strip()
    
    if not expression:
        raise CalculationError("表达式不能为空")
    
    try:
        # 解析表达式为 AST
        tree = ast.parse(expression, mode='eval')
        # 安全地评估 AST
        return _safe_eval_node(tree)
    except SyntaxError as e:
        raise CalculationError(f"语法错误: {str(e)}")
    except CalculationError:
        raise
    except Exception as e:
        raise CalculationError(f"计算错误: {str(e)}")


def calculate_expression_chain(expressions: List[str]) -> List[Union[int, float]]:
    """
    批量计算多个表达式
    
    参数:
        expressions: 表达式字符串列表
        
    返回:
        计算结果列表
        
    示例:
        >>> calculate_expression_chain(["1+1", "2*3", "10/2"])
        [2, 6, 5.0]
    """
    results = []
    for expr in expressions:
        results.append(calculate(expr))
    return results


if __name__ == "__main__":
    print("=" * 50)
    print("优化的数字计算逻辑模块测试")
    print("=" * 50)
    
    # 基本运算测试
    print("\n【基本运算测试】")
    test_cases = [
        ("加法", lambda: add(5, 3)),
        ("减法", lambda: subtract(10, 4)),
        ("乘法", lambda: multiply(6, 7)),
        ("除法", lambda: divide(20, 4)),
        ("地板除法", lambda: floor_divide(17, 5)),
        ("幂运算", lambda: power(2, 3)),
        ("取模", lambda: modulo(17, 5)),
        ("平方根", lambda: square_root(16)),
        ("绝对值", lambda: absolute(-5)),
        ("取负", lambda: negate(10)),
    ]
    
    for name, func in test_cases:
        try:
            result = func()
            print(f"{name}: {result}")
        except CalculationError as e:
            print(f"{name}: 错误 - {e}")
    
    # 表达式计算测试
    print("\n【表达式计算测试】")
    expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "100 / 5 + 10",
        "2 ** 3 + 1",
        "17 // 5",
        "17 % 5",
        "-5 + 3",
        "(-2) ** 2",
        "3.14 * 2",
        "((2 + 3) * (4 - 1)) / 3",
    ]
    
    for expr in expressions:
        try:
            result = calculate(expr)
            print(f"{expr:25} = {result}")
        except CalculationError as e:
            print(f"{expr:25} = 错误: {e}")
    
    # 错误处理测试
    print("\n【错误处理测试】")
    error_cases = [
        ("除以零", "10 / 0"),
        ("负数开方", "sqrt(-1)" if False else "手动测试"),
        ("非法字符", "2 + a"),
        ("空表达式", ""),
    ]
    
    for name, expr in error_cases:
        if expr == "手动测试":
            try:
                square_root(-1)
                print(f"{name}: 应该抛出异常")
            except CalculationError as e:
                print(f"{name}: 正确捕获 - {e}")
        else:
            try:
                result = calculate(expr)
                print(f"{name}: 应该抛出异常，但得到 {result}")
            except CalculationError as e:
                print(f"{name}: 正确捕获 - {e}")
    
    # 批量计算测试
    print("\n【批量计算测试】")
    batch_exprs = ["1+1", "2*3", "10/2", "2**4", "15%4"]
    results = calculate_expression_chain(batch_exprs)
    for expr, result in zip(batch_exprs, results):
        print(f"{expr:10} = {result}")
    
    print("\n" + "=" * 50)
    print("所有测试完成！")
    print("=" * 50)
