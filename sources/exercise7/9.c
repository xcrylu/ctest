#include <stdio.h>
 
#define M 80
 
void fun(char a[M], char b[M]) {
	int i, j, count = 0, max = 0;
	for(i = 0; a[i] != '\0'; i++) {
		if((a[i] >= 'a' && a[i] <= 'z') || (a[i] >= 'A' && a[i] <= 'Z')){
			count++;
		}
		if((a[i] == ' ' && a[i + 1] != ' ') || (a[i] != ' ' && a[i + 1] == '\0')) {
			if(max < count) {
				max = count;
				j = i - max;
			}
			count = 0;
		}
	}
	for(i = 0; i < max; i++)	b[i] = a[j++];
	b[i]= '\0';
}
 
int main() {
	char a[M], b[M];
	printf("\n请输入一个字符串：");
	// gets(a);
    scanf("%s",a);
	
	fun(a, b);
	
	printf("\n%s\n", b);
	
	return 0;
}
