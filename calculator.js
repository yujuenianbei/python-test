// 简单的数字计算逻辑

/**
 * 加法运算
 * @param {number} a - 第一个数字
 * @param {number} b - 第二个数字
 * @returns {number} 两数之和
 */
function add(a, b) {
    return a + b;
}

/**
 * 减法运算
 * @param {number} a - 被减数
 * @param {number} b - 减数
 * @returns {number} 两数之差
 */
function subtract(a, b) {
    return a - b;
}

/**
 * 乘法运算
 * @param {number} a - 第一个数字
 * @param {number} b - 第二个数字
 * @returns {number} 两数之积
 */
function multiply(a, b) {
    return a * b;
}

/**
 * 除法运算
 * @param {number} a - 被除数
 * @param {number} b - 除数
 * @returns {number} 两数之商，如果除数为0则抛出错误
 */
function divide(a, b) {
    if (b === 0) {
        throw new Error('除数不能为0');
    }
    return a / b;
}

/**
 * 取模运算
 * @param {number} a - 被除数
 * @param {number} b - 除数
 * @returns {number} 两数之余
 */
function modulo(a, b) {
    if (b === 0) {
        throw new Error('除数不能为0');
    }
    return a % b;
}

/**
 * 幂运算
 * @param {number} base - 底数
 * @param {number} exponent - 指数
 * @returns {number} 底的指数次幂
 */
function power(base, exponent) {
    return Math.pow(base, exponent);
}

/**
 * 执行计算
 * @param {number} a - 第一个数字
 * @param {number} b - 第二个数字
 * @param {string} operator - 运算符 (+, -, *, /, %, ^)
 * @returns {number} 计算结果
 */
function calculate(a, b, operator) {
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

// 导出模块（如果在 Node.js 环境中）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        add,
        subtract,
        multiply,
        divide,
        modulo,
        power,
        calculate
    };
}
