#include <stdio.h>
#include <string.h>
 
#define M 10
#define N 80
 
void f1(char name[M][N], int id[M]) {
	int i;
	
	printf("请分别输入10名职工的姓名和职工号\n\n");
	for(i = 0; i < M; i++) {
		printf("--职工%d\n", i + 1);
		printf("姓名：");
		scanf("%s", name[i]);
		printf("职工号：");
		scanf("%d", &id[i]);
		printf("\n");
	}
}
 
void f2(char name[M][N], int id[M]) {
	int i, j, t1;
	char t2[N];
	
	for(i = 0; i < M - 1; i++) {
		for(j = 0; j < M - i - 1; j++) {
			if(id[j] > id[j + 1]) {
				t1 = id[j];
				id[j] = id[j + 1];
				id[j + 1] = t1;
				
				strcpy(t2, name[j]);
				strcpy(name[j], name[j + 1]);
				strcpy(name[j + 1], t2);
			}
		}
	}
}
 
void f3(char name[M][N], int id[M], int keyword) {
	int l = 0, r = M - 1, mid;
	
	while(l <= r) {
		mid = (l + r) / 2;
		if(id[mid] == keyword) {
			printf("\n职工号%d对应的姓名为%s\n", keyword, name[mid]);
			return;
		} else if(id[mid] < keyword) {
			l = mid + 1;
		} else {
			r = mid - 1;
		}
		
	}
	printf("\n未找到职工号为%d的姓名\n", keyword);
}
 
int main() {
	char name[M][N] = {"Li","Zhang","Yang","Qian","Sun","Jiang","Zhao","Shen","Wang","Han"};
	int id[M]={3,1,27,7,8,12,6,23,2,26}, i, keyword;
	
//	f1(name, id);
	
	printf("\n\n-----------职工信息-----------\n");
	for(i = 0; i < M; i++) {
		printf("职工%d\t姓名：%s\t职工号：%d\n", i + 1, name[i], id[i]);
	}
	
	f2(name, id);
	
	printf("\n\n-------排序后的职工信息-------\n");
	for(i = 0; i < M; i++) {
		printf("职工%d\t姓名：%s\t职工号：%d\n", i + 1, name[i], id[i]);
	}
	
	printf("\n请输入要查找的职工号：");
	scanf("%d", &keyword);
	f3(name, id, keyword);
	
	return 0;
}
