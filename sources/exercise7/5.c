#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void mystrcat(char str1[], char str2[])
{
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    for(int i = 0; i <= len2; i++){
        str1[len1+i] = str2[i];
    }
}

int main(int argc, char* argv[])
{
    char s1[1000]={0};
    char s2[500]={0};

    scanf("%s",s1);
    scanf("%s",s2);

    mystrcat(s1,s2);

    printf("%s\n",s1);

    return 0;
}