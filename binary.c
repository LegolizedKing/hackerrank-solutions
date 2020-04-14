#include<stdio.h>
#include<stdlib.h>
int binary(int a[],int b,int l,int ele)
{
	while(b<=l)
	{
		int mid=(b+l)/2;
		if(a[mid]==ele)
			return mid;
		else if(a[mid]<ele)
			b=mid+1;
		else if(a[mid]>ele)
			l=mid-1;
	}
	return -1;
}
int main()
{	int e,r;
	int arr[]={9,15,30,35,49,90,100};
	int n=sizeof(arr)/sizeof(arr[0]);
	printf("Enter element to be searched:\n");
	scanf("%d",&e);
	r=binary(arr,0,n-1,e);
	if(r!=-1)
		printf("Element found at index :%d",r);
	else
		printf("Element not found!!\n");
	return 0;
}