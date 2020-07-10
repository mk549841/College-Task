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
void displayList()
{
int c=0;
    struct node *temp;
    if(head == NULL)
        printf("List is empty.");
    else
    {
        temp = head;
        while(temp!= NULL)
	{
            temp = temp->next;
	    c++;
	}               
	printf("The lenght of linked list is..= %d\n", c+1);
    }
}
void main()
{
int i,n,data;
printf("Enter the n th value \n");
scanf("%d",&n);
printf("Enter data\n");
for(i=0;i<n;i++)
{
scanf("%d",&data);
insert_end(data);
}
displayList();
}
















