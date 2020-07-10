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

void delete_begin()
{
if(head==NULL)
printf("EMPTY LINKED LIST");
else
{
struct node *delnode;
delnode=head;
head=head->next;
delnode->next=NULL;
free(delnode);
}
}

void displayList()
{
    struct node *temp;
    if(head == NULL)
    {
        printf("List is empty.");
    }
    else
    {
        temp = head;
        while(temp != NULL)
        {
            printf("Data = %d\n", temp->data);
            temp = temp->next;                 
        }
    }
}
void main()
{
	struct node *temp,*p;
	int n,i,data;
	printf("Print no of nodes\n");
	scanf("%d",&n);
	printf("enter the data one by one\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&data);
		insert_end(data);
	}
	p=head;
	head=head->next;
	p->next=NULL;
	while(head!=NULL)
	{
		temp=head;
		head=head->next;
		temp->next=p;
		p=temp;
	}
	head=p;
	displayList();
}
