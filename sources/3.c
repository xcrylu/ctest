#include <stdio.h>

// 反转一个整数

int main() {
    int x, reversed = 0, sign = 1;
    scanf("%d", &x);
    // 处理负数
    if (x < 0) {
        sign = -1;
        x = -x; // 转为正数处理
    }
    // 反转数字
    while (x != 0) {
        int digit = x % 10;
        reversed = reversed * 10 + digit;
        x /= 10;
    }
    printf("%d\n", reversed * sign);
    return 0;
}
