// 简单的数字计算逻辑

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
    return Math.pow(base, exponent);
}

/**
 * 执行计算
 * @param a - 第一个数字
 * @param b - 第二个数字
 * @param operator - 运算符 (+, -, *, /, %, ^)
 * @returns 计算结果
 */
export function calculate(a: number, b: number, operator: string): number {
    switch (operator) {
        case '+':
            return add(a, b);
        case '-':
            return subtract(a, b);
        case '*':
            return multiply(a, b);
        case '/':
            return divide(a, b);
        case '%':
            return modulo(a, b);
        case '^':
            return power(a, b);
        default:
            throw new Error(`不支持的运算符：${operator}`);
    }
}

// 示例使用
if (require.main === module) {
    console.log('=== 简单数字计算示例 ===\n');
    
    const num1 = 10;
    const num2 = 5;
    
    console.log(`${num1} + ${num2} = ${add(num1, num2)}`);
    console.log(`${num1} - ${num2} = ${subtract(num1, num2)}`);
    console.log(`${num1} * ${num2} = ${multiply(num1, num2)}`);
    console.log(`${num1} / ${num2} = ${divide(num1, num2)}`);
    console.log(`${num1} % ${num2} = ${modulo(num1, num2)}`);
    console.log(`${num1} ^ ${num2} = ${power(num1, num2)}`);
    
    console.log('\n使用 calculate 函数:');
    console.log(`${num1} + ${num2} = ${calculate(num1, num2, '+')}`);
    console.log(`${num1} * ${num2} = ${calculate(num1, num2, '*')}`);
}
