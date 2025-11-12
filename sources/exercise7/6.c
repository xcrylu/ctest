#include <stdio.h>
#include <string.h>
 
#define M 80
 
void fun(char a[M], char res[M]) {
	int i, j = 0;
	for(i = 0; a[i] != '\0'; i++) {
		if(a[i] == 'a' || a[i] == 'A' || a[i] == 'e' || a[i] == 'E' || a[i] == 'i' || 
		a[i] == 'I' || a[i] == 'o' || a[i] == 'O' || a[i] == 'u' || a[i] == 'U') {
			res[j++] = a[i];
		}
	}
	res[j] = '\0';
}
 
int main() {
	char a[M], res[M];
	int n;
	printf("请输入一个字符串：");
	scanf("%s", a);
	
	fun(a, res);
	
	printf("\n所有元音字母：%s", res);
	
	return 0;
}
