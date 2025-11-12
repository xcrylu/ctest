#include <stdio.h>

// 输出斐波那契数列的前n项

int main() {
    int n, a = 1, b = 1;
    scanf("%d", &n);
    if (n >= 1) printf("%d ", a);
    if (n >= 2) printf("%d ", b);
    // 从第3项开始计算并输出
    for (int i = 3; i <= n; i++) {
        int c = a + b;
        printf("%d ", c);
        a = b;
        b = c;
    }
    printf("\n");
    return 0;
}
