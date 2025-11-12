#include <stdio.h>

// 求两个整数的最大公约数

int main() {
    int a, b, temp;
    scanf("%d %d", &a, &b);
    // 辗转相除法：用较大数除以较小数，余数替换较大数，直到余数为0
    while (b != 0) {
        temp = a % b;
        a = b;
        b = temp;
    }
    printf("%d\n", a);
    return 0;
}
