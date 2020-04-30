#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    int digit,r,ans=0;
    digit=n;
    while(digit>0)
    {
        r=digit%10;
        ans=ans+r;
        digit=digit/10;
    }
    printf("%d",ans);
    return 0;
}

