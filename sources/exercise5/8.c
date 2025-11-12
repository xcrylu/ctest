#include <stdio.h>
#include <math.h>

// 输出100到200之间的素数，每行输出5个

int main() {
    int count = 0; // 计数，控制每行输出5个
    for (int num = 100; num <= 200; num++) { // 外层循环：遍历100-200
        int is_prime = 1;
        // 内层循环：判断是否为素数
        for (int i = 2; i <= sqrt(num); i++) {
            if (num % i == 0) {
                is_prime = 0;
                break;
            }
        }
        if (is_prime) {
            printf("%d ", num);
            count++;
            if (count % 5 == 0) { // 每5个换行
                printf("\n");
            }
        }
    }
    printf("\n");
    return 0;
}
