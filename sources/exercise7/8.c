#include <stdio.h>
 
#define M 80
 
int letter = 0, number = 0, space = 0, other = 0;
 
void fun(char a[M]) {
	int i;
	for(i = 0; a[i] != '\0'; i++) {
		if((a[i] >= 'a' && a[i] <= 'z') || (a[i] >= 'A' && a[i] <= 'Z'))	letter++;
		else if(a[i] >= '0' && a[i] <= '9')	number++;
		else if(a[i] == ' ')	space++;
		else	other++;
	}
}
 
int main() {
	char a[M];
	printf("\n请输入一个字符串：");
	//gets(a);
    scanf("%s",a);
	
	fun(a);
	
	printf("\n%s\n字母：%d，数字：%d，空格：%d，其他字符：%d\n", a, letter, number, space, other);
	
	return 0;
}
