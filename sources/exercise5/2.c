#include <stdio.h>
#include <math.h> // 用于sqrt函数

// 判断一个整数是否为素数

int main() {
    int n, is_prime = 1;
    scanf("%d", &n);
    if (n <= 1) {
        is_prime = 0;
    } else {
        // 只需检查到sqrt(n)，若存在因数必小于等于sqrt(n)
        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) {
                is_prime = 0;
                break;
            }
        }
    }
    printf("%s\n", is_prime ? "Prime" : "Not prime");
    return 0;
}
