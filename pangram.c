#include<stdio.h>
#include<stdlib.h>
#define SIZE 50
int main()
{
		int count[26]={0};
		char a[SIZE];
		int i;
		printf("enter sentence:\n");
		fgets(a,SIZE,stdin);
		for(i=0;a[i]!='\0';i++)
		{
			if(a[i]==32)
				continue;
			if(a[i]>96)
				count[a[i]-97]+=1;
			else
				count[a[i]-65]+=1;

		}
		for(i=0;i<26;i++)
		{
			if(count[i]==0)
			{
				printf("Not a Pangram\n");
				exit(-1);
			}
		}
		printf("Is a pangram!!\n");
		return 0;
}