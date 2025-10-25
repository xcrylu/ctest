#include <stdio.h>

// 输出所有不超过100的勾股数三元组,即a^2 + b^2 = c^2且a<b<c

int main() {
    // 三重循环保证a < b < c，且均≤100
    for (int a = 1; a <= 100; a++) {
        for (int b = a + 1; b <= 100; b++) {
            for (int c = b + 1; c <= 100; c++) {
                if (a*a + b*b == c*c) { // 勾股定理
                    printf("%d %d %d\n", a, b, c);
                }
            }
        }
    }
    return 0;
}
