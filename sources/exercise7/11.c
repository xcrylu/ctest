#include <stdio.h>
#include <math.h>
 
#define M 10
#define N 5
 
void f1(int a[M][N]) {
	int i, j;
	float average[M], sum;
	
	for(i = 0; i < M; i++) {
		sum = 0.0;
		for(j = 0; j < N; j++) {
			sum += a[i][j];
		}
		average[i] = sum / N;
	}
	
	printf("\n\n每个学生的平均分\n");
	for(i = 0; i < M; i++) {
		printf("--学生%d：%.2f\n", i + 1, average[i]);
	}
}
 
void f2(int a[M][N]) {
	int i, j;
	float average[M], sum;
	
	for(j = 0; j < N; j++) {
		sum = 0.0;
		for(i = 0; i < M; i++) {
			sum += a[i][j];
		}
		average[j] = sum / M;
	}
	
	printf("\n\n每门课程的平均分\n");
	for(i = 0; i < N; i++) {
		printf("--课程%d：%.2f\n", i + 1, average[i]);
	}
}
 
void f3(int a[M][N]) {
	int i, j, max = a[0][0], m, n;
	
	for(i = 0; i < M; i++) {
		for(j = 0; j < N; j++) {
			if(max < a[i][j]) {
				max = a[i][j];
				m = i + 1;
				n = j + 1;
			}
		}
	}
	
	printf("\n\n--最高分：%d\t学生%d\t课程%d\n", max, m, n);
}
 
void f4(int a[M][N]) {
	int i, j, average[M];
	float s, sum = 0.0, sumx = 0.0, res;
	
	for(i = 0; i < M; i++) {
		s = 0.0;
		for(j = 0; j < N; j++) {
			s += a[i][j];
		}
		average[i] = s / N;
		sum += average[i];
		sumx += average[i] * average[i];
	}
	
	res = sumx / M - pow(sum / M, 2);
	
	printf("\n\n--平均分方差：%.2f\n", res);
}
 
int main() {
//	int a[M][N] = {87,88,92,67,78,88,86,87,98,90,76,75,65,65,78,67,87,60,90,67,77,78,85,64,56,76,89,94,65,76,78,75,64,67,77,77,76,56,87,85,84,67,78,76,89,86,75,64,69,90}, i, j;
	int a[M][N], i, j;
	
	printf("请分别输入10名学生的5门课成绩\n\n");
	for(i = 0; i < M; i++) {
		printf("--学生%d\n", i + 1);
		for(j = 0; j < N; j++) {
			printf("课程%d：", j + 1);
			scanf("%d", &a[i][j]);
		}
		printf("\n");
	}
	
	f1(a);
	f2(a);
	f3(a);
	f4(a);
	
	return 0;
}
