#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.
int max(int num1, int num2)
{
    return (num1 > num2 ) ? num1 : num2;
}


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int m=0,o=0;
  int p=0;
  for(int i=1;i<n;i++)
  {
      for(int j=i+1;j<=n;j++)
      {
          if((i&j)<k)
          {
              m=max(m,i&j);
          }
          if((i|j)<k)
          {
              p=max(p,i|j);

          }
          if((i^j)<k)
          {
              o=max(o,i^j);
          }
      }
  }
  printf("%d\n%d\n%d",m,p,o);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
