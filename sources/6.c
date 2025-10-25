#include <stdio.h>

// 输出9x9乘法表

int main() {
    for (int i = 1; i <= 9; i++) { // 控制行数（乘数）
        for (int j = 1; j <= i; j++) { // 控制每行的被乘数
            printf("%dx%d=%d", j, i, j * i);
            if (j != i) printf(" "); // 行末不加空格
        }
        printf("\n");
    }
    return 0;
}
