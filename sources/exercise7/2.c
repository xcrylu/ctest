#include <stdio.h>
#include <math.h>

int isPrime(int n)
{
    int res = 1;
    for(int i=2;i<=sqrt(n);i++){
        if(n%i == 0 ) {
            res =0;
            break;
        }
    }
    return res;
}

int main()
{
    int n;
    scanf("%d",&n);
    printf("%s\n",isPrime(n)?"素数":"非素数");
    return 0;
}