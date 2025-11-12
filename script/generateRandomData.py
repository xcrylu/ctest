import sys
import random

# 函数名： generate_random_data
# 参数：
#     n: 数据组数
#     m：每组数据个数
#     ranges: 每个数据的取值范围列表，格式为[(min1, max1), (min2, max2), ..., (minm, maxm)]
# 功能：生成n组随机数据，每组包含m个随机整数，且每个整数在对应的范围内
# 输出格式：
#     第一行输出数据组数n
#     接下来的n行，每行输出m个随机整数，整数之间用空格分隔  
# 示例调用：
#     generate_random_data(5, 3, [(1, 10), (20, 30), (100, 200)])
# 输出：
#     5
#     3 25 150
#     7 22 180
#     1 30 120
#     10 21 199
#     5 28 130

def generate_random_data(n, m, ranges):
    # 输出数据组数n
    if len(ranges) != m:
        raise ValueError(f"范围数量错误: 预期 {m} 个范围，但收到 {len(ranges)} 个范围")
    print(n)
    for _ in range(n):
        group = []
        for (min_val, max_val) in ranges:
            if(min_val > max_val):
                raise ValueError(f"范围错误: min({min_val}) 不能大于 max({max_val})")
            num = random.randint(min_val, max_val)
            group.append(str(num))
        print(" ".join(group))


def main():
    # 检查参数数量是否至少为2（n和m）
    if len(sys.argv) < 3:
        print("用法：python generate_random_data.py 数据组数n 每组数据数量m [min_1 max_1 min_2 max_2 ... min_m max_m]")
        sys.exit(1)

    try:
        # 解析n（数据组数）和m（每组数据数量）
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        # 校验n和m为正整数
        if n <= 0 or m <= 0:
            print("错误：n和m必须是正整数")
            sys.exit(1)
    except ValueError:
        print("错误：n和m必须是整数")
        sys.exit(1)

    # 解析范围参数（min和max）
    range_args = sys.argv[3:]
    # 校验范围参数数量是否为2*m（每个数据需要min和max）
    if len(range_args) != 2 * m:
        print(f"错误：范围参数数量应为 {2 * m} 个（每个数据需要1个min和1个max）")
        sys.exit(1)

    # 将范围参数转换为整数，并存储为[(min1, max1), (min2, max2), ..., (minm, maxm)]
    ranges = []
    for i in range(m):
        try:
            min_val = int(range_args[2 * i])
            max_val = int(range_args[2 * i + 1])
        except ValueError:
            print(f"错误：范围参数必须是整数（第{i+1}组范围参数错误）")
            sys.exit(1)
        # 校验min <= max
        if min_val > max_val:
            print(f"错误：第{i+1}组范围中，min({min_val})不能大于max({max_val})")
            sys.exit(1)
        ranges.append((min_val, max_val))

    # 输出数据组数n
    print(n)

    # 生成n组数据
    for _ in range(n):
        group = []
        # 每组生成m个随机数（对应m个范围）
        for (min_val, max_val) in ranges:
            # 生成[min_val, max_val]范围内的随机整数
            num = random.randint(min_val, max_val)
            group.append(str(num))
        # 用空格拼接当前组数据并打印
        print(" ".join(group))

if __name__ == "__main__":
    # main()
    generate_random_data(10, 3, [(1, 100), (200, 300), (4000, 5000)])