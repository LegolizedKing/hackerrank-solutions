#include<stdio.h>
#include<stdlib.h>
struct Node {
	int item;
	struct Node * next;
};
int main()
{
	struct Node * head=NULL;
	struct Node * second=NULL;
	struct Node * third=NULL;
	head=(struct Node*)malloc(sizeof(struct Node));
	second=(struct Node*)malloc(sizeof(struct Node));
	third=(struct Node*)malloc(sizeof(struct Node));
	head->item=1;
	head->next=second;
	second->item=2;
	second->next=third;
	third->item=3;
	third->next= NULL;
	printf("%d\n",head->item);
	return 0;
}