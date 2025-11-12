#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverseString(char* string)
{
    int n = strlen(string);
   
    for(int i= 0;i<n/2;i++){
        // printf("%x^",string[i]);
        char t = string[i];
        string[i] = string[n-1-i];
        string[n-1-i] = t;
    }
}

void outstring(char * string)
{
    int n = strlen(string);
    n=10;
   
    for(int i= 0;i<n;i++){
        printf("%x|",string[i]);       
    }
}

int main(int argc, char* argv[])
{
    char s[10000];

    // gets(s);//由于安全问题，,c99声明gets函数为过时，c11删除了gets函数
    fgets(s, sizeof(s), stdin);
    //fget会将换行符\n读入，下面手动删除末尾的换行符
    int n = strlen(s);
    s[n-1]='\0'; 

    reverseString(s);    
    
    // outstring(s);
    puts(s);

    return 0;
}