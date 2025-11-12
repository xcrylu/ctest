#include <stdio.h>
 
#define M 8
 
void fun(char a[M], int num) {
	int i = 0, n = num;
	while(n > 0) {
		a[i] = n % 10 + '0';
		n = n / 10;
		a[i + 1] = ' ';
		i += 2;
	}
	a[i - 1] = '\0';
}
 
int main() {
	char a[M];
	int num, i;
	printf("\n请输入一个4位数字：");
	scanf("%d", &num);
	while(num < 1000 || num > 9999) {
		printf("\n输入有误，请重新输入：");
		scanf("%d", &num);
	}
	
	fun(a, num);
	
	for(i = M - 1; i >= 0; i--) {
		printf("%c", a[i]);
	}
	
	return 0;
}
