#include <stdio.h>

//最大公因数
int gcd(int m,int n )
{
    // int k = m%n;
    // if(k==0) return n;

    // return gcd(n,k);
    int k = m%n;
    while(k!=0){       
        m=n;
        n=k;
        k= m%n;
    };
    return n;
}

int lcm(int m,int n)
{
    return m*n/gcd(m,n);
}

int main()
{
    int m,n;

    scanf("%d%d",&m,&n);

    printf("gcd:%d\nlcm:%d\n",gcd(m,n),lcm(m,n));
    
    return 0;
}
