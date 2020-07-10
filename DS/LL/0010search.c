#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;           
    struct node *next;  
}*head=NULL,*tail=NULL;
void insert_end(int data)
{
    struct node *newNode;
    newNode = (struct node*)malloc(sizeof(struct node));
    newNode->data=data;
    newNode->next=NULL;
    if(head == NULL)
    {
        head=newNode;
        tail=newNode;
	printf("NEW NODE CREATED\n");
    }
    else
    {
        tail->next=newNode;
        tail=newNode;
    }
}
void displayList(int e)
{
    struct node *temp;
    if(head == NULL)
        printf("List is empty.");
    else
    {
        temp = head;
        while(temp->next!= NULL)
	{
	    if(temp->data==e)
		printf("The element is %d is presented \n",temp->data);
	temp = temp->next;
	}               
    }
}
void main()
{
int i,n,data,ele;
printf("Enter the n th value \n");
scanf("%d",&n);
printf("Enter data\n");
for(i=0;i<n;i++)
{
scanf("%d",&data);
insert_end(data);
}
printf("Enter  the search element\n");
scanf("%d",&ele);
displayList(ele);
}
















