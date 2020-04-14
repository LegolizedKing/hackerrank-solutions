#include<stdio.h>
#include<string.h>
int main()
{	int len;	
	char arr[]="Monday v/s friday!";
	char * token=strtok(arr," ");
	while(token!=NULL)
	{   len=strlen(token);
		printf("%s %d\n",token,len);
		token=strtok(NULL," ");
	}	
		
	return 0;
}