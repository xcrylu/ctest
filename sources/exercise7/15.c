#include <stdio.h>
 
int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
 
int fun(int y, int m, int d) {
	int i, flag = 0, res = 0;
	
	if((y % 4 == 0 && y % 100 != 0) || (y % 400 == 0))	flag = 1;
	
	for(i = 1; i < m; i++) {
		res += month[i];
	}
	
	res += d;
	
	if(flag == 1 && m > 2)	res++;
	
	return res;
}
 
int main() {
	int y, m, d, flag = 0, res;
	
	printf("\n请输入年月日：");
	scanf("%d%d%d", &y, &m, &d);
	while(1) {
		if(m < 1 || m > 12 || d < 1)	flag = 1;
		if(m == 2 && d > 29)	flag = 1;
		if((m == 4 || m == 6 || m == 9 || m == 11) && d > 30)	flag = 1;
		else if(d > 31)	flag = 1;
		if(flag == 1) {
			printf("\n输入有误，请重新输入年月日：");
			scanf("%d%d%d", &y, &m, &d);
			flag = 0;
			continue;
		}
		break;
	}
	
	res = fun(y, m, d);
	
	printf("\n%d/%d/%d ----→ 第%d天\n", y, m, d, res);
	
	return 0;
}
