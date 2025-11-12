#include <stdio.h>
int main()
{
	void hanoi(int n,char source,char tmp,char destination);
	//对hanoi函数的声明 
	int m;
	printf("input the number of diskes:");
	scanf("%d",&m);
	printf("The step to move %d diskes:\n",m);
	hanoi(m,'A','B','C');
}
void hanoi(int n,char source,char tmp,char destination)	//定义hanoi函数
//将n个盘从one座借助two座,移到three座 
{	void move(char source,char destination);	//对move函数的声明 
	if(n==1)
		move(source,destination);
	else
	{	hanoi(n-1,source,destination,tmp);
		move(source,destination);
		hanoi(n-1,tmp,source,destination);
	}
}
void move(char source,char destination)		//定义move函数 
{	printf("%c->%c\n",source,destination); }
