#include<stdio.h> 
#include<stdlib.h> 
struct node 
{ 
    int data1,data2,data3; 
    struct node* next1;
struct node* next2; 
}*head1=NULL,*head2=NULL,*tail1=NULL,*tail2=NULL;

void insert1(int d1)
{
struct node* nn1;
nn1=(struct node*)malloc(sizeof(struct node));
nn1->data1=d1;
nn1->next1=NULL;
if(head1==NULL)
{
head1=nn1;
tail1=nn1;
}
else
{
tail1->next1=nn1;
tail1=nn1;
}
}


void insert2(int d2)
{
struct node* nn2;
nn2=(struct node*)malloc(sizeof(struct node));
nn2->data2=d2;
nn2->next2=NULL;
if(head2==NULL)
{
head2=nn2;
tail2=nn2;
}
else
{
tail2->next2=nn2;
tail2=nn2;
}
}





void inte()
{
	struct node* t1=head1;
	struct node* t2=head2;
	while(t1!=NULL)
	{
		t2=head2;
		while(t2!=NULL)
		{
			if(t1->data1==t2->data2)
			{
				printf("%d	",t2->data2);
				break;
			}
			else
				t2=t2->next2;
		}
	t1=t1->next1;
	}
}
void uni()
{
	struct node* t1=head1;
	struct node* t2=head2;
	while(t1->next1!=NULL)
	{
		printf("%d	",t1->data1);
		t1=t1->next1;
	}
	printf("%d	",t1->data1);
	int c=0;
	while(t2!=NULL)
	{
		t1=head1;
		while(t1!=NULL)
		{
			if(t1->data1==t2->data2)
			{
				c++;
				break;
			}
			else
				{
				t1=t1->next1;
				}
			if(c==0){
				printf(" %d	",t2->data2);
				break;
				}
			c=0;
		}
	t2=t2->next2;
	}
}
					
void main()
{
	int i,data,data2,n,n1,j,chi;
	printf("\nEnter the n value for head1\n");
	scanf("%d",&n);
	printf("\nEnter the data 1,data2 one by one\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&data);
		insert1(data);
	}
	printf("\nEnter the n value for head2\n");
	scanf("%d",&n1);
	printf("\nEnter the data2 one by one\n");
	for(j=0;j<n1;j++)
	{
		scanf("%d",&data2);
		insert2(data2);
	}
	while(1)
	{
		printf("\nEnter your choice 1for union\n 2 For intersection");
		scanf("%d",&chi);
		switch(chi)
		{
			case 1:
				uni();
				break;
			case 2:
				inte();
				break;
			default:
				printf("\nThankyou\n");
				
		}
	}
//inte();
}

