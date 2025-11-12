#include <stdio.h>

// 计算n x n矩阵主对角线和副对角线元素之和

int main() {
    int n, sum = 0;
    scanf("%d", &n);
    int mat[5][5];
    // 输入矩阵
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &mat[i][j]);
        }
    }
    // 累加主对角线（i==j）和副对角线（i+j==n-1）
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j || i + j == n - 1) {
                sum += mat[i][j];
            }
        }
    }
    printf("%d\n", sum);
    return 0;
}
