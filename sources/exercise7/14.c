#include <string.h>
#include <stdio.h>
 
void fun(int n, char *s) {
	if(n == 0)	return;
	fun(n / 10, s - 1);
	*s = n % 10 + '0';
}
 
int main() {
	int n,  num, c = 0;
	char str[80], *s = str;
	scanf("%d", &n);
	if(n < 0) {
		num = -n;
		n = -n;
		*s = '-';
		s++;
	} else
		num = n;
	do{
		num /= 10;
		c++;	
	} while(num);
	fun(n, s + c - 1);
	puts(str);
	return 0;
}
