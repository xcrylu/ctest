#include <stdio.h>


void transpose3x3(int matrix[3][3])
{
    for(int i = 0 ;i<3;i++){
        for(int j=0;j<3;j++){
            int t= matrix[i][j];
            matrix[i][j]=matrix[j][i];
            matrix[j][i] = t;
        }
    }
}

void inputData(int matrix[3][3])
{
    for(int i = 0 ;i<3;i++){
        for(int j=0;j<3;j++){
            scanf("%d",&matrix[i][j]);
        }
    }
}

void outputData(int matrix[3][3])
{
    for(int i = 0 ;i<3;i++){
        for(int j=0;j<3;j++){
            printf("%10d",matrix[i][j]);
        }
        printf("\n");
    }
}


int main()
{
    int a[3][3];

    inputData(a);
    transpose3x3(a);
    outputData(a);

    return 0;
}
