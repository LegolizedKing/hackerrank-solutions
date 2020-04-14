#include<stdio.h>
#include<string.h>
#define SIZE 9
void selectionsort(char a[][SIZE],int n)
{
	int i,j,small;
	char temp[SIZE];
	for(i=0;i<n-1;i++)
	{
		small=i;
		strcpy(temp,a[i]);
		for(j=i+1;j<n;j++)
		{
			if(strcmp(temp,a[j])>0)
			{
				strcpy(temp,a[j]);
				small=j;
			}
		}
		if(small!=i)
		{
			char t[SIZE];
			strcpy(t,a[i]);
			strcpy(a[i],a[small]);
			strcpy(a[small],t);
		}
	}
}
int main()
{
	char arr[][SIZE]={"World!","Kottayam","dream","Help!"};
	int n=sizeof(arr)/sizeof(arr[0]);
	int i;
	printf("The array is:\n");
	for(i=0;i<n;i++)
		printf("%s ",arr[i]);
	selectionsort(arr,n);
	printf("\nSorted array is:\n");
	for(i=0;i<n;i++)
		printf("%s ",arr[i]);
	return 0;
}