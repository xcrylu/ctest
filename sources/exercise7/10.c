#include <stdio.h>
#include <string.h>
 
#define M 80
 
void fun(char a[M]) {
	int i, j;
	char t;
	for(i = 0; a[i] != '\0'; i++) {
		for(j = 0; j < strlen(a) - i; j++) {
			if(a[j] > a[j + 1]) {
				t = a[j];
				a[j] = a[j + 1];
				a[j + 1] = t;
			}
		}
	}
}
 
int main() {
	char a[M];
	printf("\n请输入一个字符串：");
	// gets(a);
    scanf("%s",a);
	
	fun(a);
	
	printf("\nafter: %s\n", a);
	
	return 0;
}
