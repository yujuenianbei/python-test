#!/bin/bash

# 3+7 计算脚本

# 方法1: 直接使用expr
result1=$(expr 3 + 7)
echo "方法1 (expr): 3 + 7 = $result1"

# 方法2: 使用$(( ))算术扩展
result2=$((3 + 7))
echo "方法2 (算术扩展): 3 + 7 = $result2"

# 方法3: 使用bc计算器
result3=$(echo "3 + 7" | bc)
echo "方法3 (bc): 3 + 7 = $result3"

# 方法4: 使用let命令
let "result4 = 3 + 7"
echo "方法4 (let): 3 + 7 = $result4"

echo ""
echo "最终结果: 3 + 7 = $result2"
