// 优化的数字计算逻辑

/**
 * 支持的二元运算符枚举
 */
export enum BinaryOperator {
    ADD = '+',
    SUBTRACT = '-',
    MULTIPLY = '*',
    DIVIDE = '/',
    MODULO = '%',
    POWER = '^'
}

/**
 * 支持的一元运算符枚举
 */
export enum UnaryOperator {
    NEGATE = 'neg',
    ABSOLUTE = 'abs',
    SQRT = 'sqrt',
    SQUARE = 'square'
}

/**
 * 计算结果接口
 */
export interface CalculationResult {
    value: number;
    operation: string;
    success: boolean;
    error?: string;
}

/**
 * 加法运算
 * @param a - 第一个数字
 * @param b - 第二个数字
 * @returns 两数之和
 */
export function add(a: number, b: number): number {
    return a + b;
}

/**
 * 减法运算
 * @param a - 被减数
 * @param b - 减数
 * @returns 两数之差
 */
export function subtract(a: number, b: number): number {
    return a - b;
}

/**
 * 乘法运算
 * @param a - 第一个数字
 * @param b - 第二个数字
 * @returns 两数之积
 */
export function multiply(a: number, b: number): number {
    return a * b;
}

/**
 * 除法运算
 * @param a - 被除数
 * @param b - 除数
 * @returns 两数之商，如果除数为0则抛出错误
 */
export function divide(a: number, b: number): number {
    if (b === 0) {
        throw new Error('除数不能为0');
    }
    return a / b;
}

/**
 * 取模运算
 * @param a - 被除数
 * @param b - 除数
 * @returns 两数之余
 */
export function modulo(a: number, b: number): number {
    if (b === 0) {
        throw new Error('除数不能为0');
    }
    return a % b;
}

/**
 * 幂运算
 * @param base - 底数
 * @param exponent - 指数
 * @returns 底的指数次幂
 */
export function power(base: number, exponent: number): number {
    return base ** exponent;
}

/**
 * 平方根运算
 * @param a - 数字
 * @returns 平方根，如果为负数则抛出错误
 */
export function sqrt(a: number): number {
    if (a < 0) {
        throw new Error('不能对负数开平方');
    }
    return Math.sqrt(a);
}

/**
 * 绝对值运算
 * @param a - 数字
 * @returns 绝对值
 */
export function abs(a: number): number {
    return Math.abs(a);
}

/**
 * 取反运算
 * @param a - 数字
 * @returns 相反数
 */
export function negate(a: number): number {
    return -a;
}

/**
 * 平方运算
 * @param a - 数字
 * @returns 平方值
 */
export function square(a: number): number {
    return a ** 2;
}

/**
 * 执行二元计算
 * @param a - 第一个数字
 * @param b - 第二个数字
 * @param operator - 运算符
 * @returns 计算结果
 */
export function calculateBinary(a: number, b: number, operator: BinaryOperator | string): number {
    switch (operator) {
        case BinaryOperator.ADD:
        case '+':
            return add(a, b);
        case BinaryOperator.SUBTRACT:
        case '-':
            return subtract(a, b);
        case BinaryOperator.MULTIPLY:
        case '*':
            return multiply(a, b);
        case BinaryOperator.DIVIDE:
        case '/':
            return divide(a, b);
        case BinaryOperator.MODULO:
        case '%':
            return modulo(a, b);
        case BinaryOperator.POWER:
        case '^':
            return power(a, b);
        default:
            throw new Error(`不支持的运算符：${operator}`);
    }
}

/**
 * 执行一元计算
 * @param a - 数字
 * @param operator - 运算符
 * @returns 计算结果
 */
export function calculateUnary(a: number, operator: UnaryOperator | string): number {
    switch (operator) {
        case UnaryOperator.NEGATE:
        case 'neg':
            return negate(a);
        case UnaryOperator.ABSOLUTE:
        case 'abs':
            return abs(a);
        case UnaryOperator.SQRT:
        case 'sqrt':
            return sqrt(a);
        case UnaryOperator.SQUARE:
        case 'square':
            return square(a);
        default:
            throw new Error(`不支持的一元运算符：${operator}`);
    }
}

/**
 * 执行计算（兼容二元和一元运算）
 * @param a - 第一个数字（一元运算时为唯一数字）
 * @param b - 第二个数字（二元运算时使用，一元运算时可省略）
 * @param operator - 运算符
 * @returns 计算结果
 */
export function calculate(a: number, b?: number, operator?: string): number {
    // 如果只提供一个参数，视为一元运算
    if (b === undefined || operator === undefined) {
        if (operator === undefined) {
            throw new Error('必须提供运算符');
        }
        return calculateUnary(a, operator);
    }
    
    // 否则视为二元运算
    return calculateBinary(a, b, operator);
}

/**
 * 安全执行计算（不抛出异常，返回结果对象）
 * @param a - 第一个数字
 * @param b - 第二个数字（可选）
 * @param operator - 运算符
 * @returns 计算结果对象
 */
export function safeCalculate(a: number, b?: number, operator?: string): CalculationResult {
    try {
        const result = calculate(a, b, operator);
        return {
            value: result,
            operation: `${a} ${operator || ''} ${b !== undefined ? b : ''}`.trim(),
            success: true
        };
    } catch (error) {
        return {
            value: NaN,
            operation: `${a} ${operator || ''} ${b !== undefined ? b : ''}`.trim(),
            success: false,
            error: error instanceof Error ? error.message : '未知错误'
        };
    }
}

// 示例使用
if (require.main === module) {
    console.log('=== 优化的数字计算示例 ===\n');
    
    const num1 = 10;
    const num2 = 5;
    
    console.log('--- 二元运算 ---');
    console.log(`${num1} + ${num2} = ${add(num1, num2)}`);
    console.log(`${num1} - ${num2} = ${subtract(num1, num2)}`);
    console.log(`${num1} * ${num2} = ${multiply(num1, num2)}`);
    console.log(`${num1} / ${num2} = ${divide(num1, num2)}`);
    console.log(`${num1} % ${num2} = ${modulo(num1, num2)}`);
    console.log(`${num1} ^ ${num2} = ${power(num1, num2)}`);
    
    console.log('\n--- 一元运算 ---');
    console.log(`sqrt(${num1}) = ${sqrt(num1)}`);
    console.log(`abs(-${num1}) = ${abs(-num1)}`);
    console.log(`negate(${num1}) = ${negate(num1)}`);
    console.log(`square(${num1}) = ${square(num1)}`);
    
    console.log('\n--- 使用 calculateBinary 函数 ---');
    console.log(`${num1} + ${num2} = ${calculateBinary(num1, num2, BinaryOperator.ADD)}`);
    console.log(`${num1} * ${num2} = ${calculateBinary(num1, num2, '*')}`);
    
    console.log('\n--- 使用 calculateUnary 函数 ---');
    console.log(`sqrt(${num1}) = ${calculateUnary(num1, UnaryOperator.SQRT)}`);
    console.log(`square(${num1}) = ${calculateUnary(num1, 'square')}`);
    
    console.log('\n--- 使用通用 calculate 函数 ---');
    console.log(`${num1} + ${num2} = ${calculate(num1, num2, '+')}`);
    console.log(`sqrt(${num1}) = ${calculate(num1, undefined, 'sqrt')}`);
    
    console.log('\n--- 使用 safeCalculate 安全计算 ---');
    const result1 = safeCalculate(10, 0, '/');
    console.log(`10 / 0:`, result1);
    
    const result2 = safeCalculate(-4, undefined, 'sqrt');
    console.log(`sqrt(-4):`, result2);
    
    const result3 = safeCalculate(16, undefined, 'sqrt');
    console.log(`sqrt(16):`, result3);
}
