#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    int result=0;
    scanf("%d\n%d", &a, &b);
  	// Complete the code.
    char arr[11][6]={"one","two","three","four","five","six","seven","eight","nine","even","odd"};
    for(int i=a;i<=b;i++)
    {
        result=i<=9?i-1:9+(i%2);
        printf("%s\n",arr[result]);
    }
    return 0;
}


