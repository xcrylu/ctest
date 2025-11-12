#include <stdio.h>

// 输出杨辉三角的前n行

int main() {
    int n;
    scanf("%d", &n);
    int triangle[10][10] = {0}; // 存储杨辉三角元素
    // 初始化杨辉三角
    for (int i = 0; i < n; i++) {
        triangle[i][0] = 1; // 每行第一个元素为1
        triangle[i][i] = 1; // 每行最后一个元素为1
        // 计算中间元素（从第2行开始）
        for (int j = 1; j < i; j++) {
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
        }
    }
    // 打印杨辉三角
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            printf("%d ", triangle[i][j]);
        }
        printf("\n");
    }
    return 0;
}
