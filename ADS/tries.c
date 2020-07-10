#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct tries
{
	int endflag;
	struct tries *alphabets[26];

}*root=NULL;
void insert(struct tries *tree,char* str)
{
	int i,j;
	for(i=0;i<strlen(str);i++)
	{
		if(tree->alphabets[str[i]-'a']==NULL)
		{
			struct tries* newnode=(struct tries*)malloc(sizeof(struct tries));
			for(j=0;j<26;j++)
			{
				newnode->alphabets[j]=NULL;
			}
			newnode->endflag=0;
			tree->alphabets[str[i]-'a']=newnode;
			tree=newnode;
		}
		else
		{
			tree=tree->alphabets[str[i]-'a'];
		}
	}
	tree->endflag=1;
}
int display(struct tries *tree)
{
	int i;
	if(tree->endflag==1)
	{
		return;
	}
	else
	{
		for(i=0;i<26;i++)
		{
			if(tree->alphabets[i]!=NULL)
			{
				printf("Element Searched=%c \n",'a'+i);
				display(tree->alphabets[i]);
			}
		}
	}
}
int search(struct tries *tree,char* search)
{
	int i,sum=0;
	for(i=0;i<strlen(search);i++)
	{
		if(tree->alphabets[search[i]-'a']!=NULL)
		{
			tree=tree->alphabets[search[i]-'a'];
		}
		else
			return 0;
	}
	if(tree->endflag==1)
	{
		sum+=1;
		printf("Count=%d \n",sum);
	}
	else
		return 0;
}
int main()
{
	int i,n;
	char search1[20];
	root=(struct tries*)malloc(sizeof(struct tries));
	for(i=0;i<26;i++)
	{
		root->alphabets[i]=NULL;
	}
	root->endflag=0;
	printf("No. of strings: ");
	scanf("%d",&n);
	char str[n][20];
	for(i=0;i<n;i++)
	{
		scanf("%s",str[i]);
		insert(root,str[i]);
	}
	printf("Enter the string to search: ");
	scanf("%s",search1);
	if(search(root,search1))
		printf("Element Found \n");
	else
		printf("Element Not Found \n");
	display(root);
}	
