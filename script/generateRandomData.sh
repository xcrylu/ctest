#/bin/bash

# 说明：批量数据生成器
# 用法：./generateRandomData.sh n m > input.txt
# 输入参数： 
# 1： 参数多少组数据 n
# 2： 每组数据的数量和范围 m  min_1 max_1 min_2  max_2 ... min_m max_m  d ...
# 输出格式：
# 第一行：数据的个数 n
# 第二行：第一组数据
# 第三行：第二组数据
# ...
# 第 n+1 行：第 n 组数据
#
# 其中 n 是生成的数据数量，
# 每组数据有m，每个数据的范围是 [a,b] 
# 例如要生成 3 组数据，每组数据有 4 个，范围分别是 [1,10], [20,30], [100,200], [300,400]
# 则调用方式为：./generateRandomData.sh 3 4 1 10 20 30 100 200 300 400
# 输出格式为：
# 3
# 5 25 150 350
# 3 20 199 380
# 8 30 100 320

# 检查参数是否足够
if [ $# -lt 2 ]; then
    echo "用法：$0 数据组数n 每组数据数量m [min_1 max_1 min_2 max_2 ... min_m max_m]"
    exit 1
fi

n=$1
m=$2
shift 2  # 移除前两个参数（n和m），剩下的是范围参数

# 将所有范围参数（min和max）保存到数组中
ranges=("$@")

# 检查范围参数数量是否正确（必须是2*m个）
if [ ${#ranges[@]} -ne $((2 * m)) ]; then
    echo "错误：范围参数数量应为 $((2 * m)) 个（每个数据需要min和max）"
    exit 1
fi

# 输出数据组数n
echo $n

# 生成n组数据
for ((i=1; i<=n; i++)); do
    line=""  # 保存当前组的数据
    for ((j=1; j<=m; j++)); do
        # 从数组中取第j个数据的min和max（数组索引从0开始）
        # 第j个数据的min在数组中的索引是 2*(j-1)，max是 2*(j-1)+1
        min=${ranges[2*(j-1)]}
        max=${ranges[2*(j-1)+1]}
        
        # 计算随机数（确保min<=max）
        if [ $min -gt $max ]; then
            echo "错误：第 $j 个数据的min($min)大于max($max)"
            exit 1
        fi
        num=$((RANDOM % (max - min + 1) + min))
        
        # 拼接当前组的数据（避免末尾多空格）
        if [ -z "$line" ]; then
            line="$num"
        else
            line="$line $num"
        fi
    done
    echo "$line"  # 输出当前组数据
done

