#include <stdio.h>

int max(int array[],int start,int end)
{
    if (start == end) {
        return array[start];
    }
    else{
        int  maxvalue = max(array,start+1,end); 
        maxvalue = array[start]>maxvalue?array[start]:maxvalue;
    }
}

void getdata(int array[],int n)
{
    for(int i = 0; i < n; i++)
    {
       scanf("%d", &array[i]);
    }

}

int main(int argc,char* argv[])
{
    int a[4];//={100,53,35,63,32,71,35,232,12,32};
    getdata(a,4);

    printf("max=%d\n",max(a,0,4));
}