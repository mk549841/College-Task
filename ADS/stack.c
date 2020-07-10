#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define max 100
int top=-1;
char stack[max];



void push(char a)
{
if(top==max-1)
	printf("Stack is full");
else{ 
top++;
	stack[top]=a;
	//printf("%c\t",a);
	}
}
void pop()
{
char sa;
if(top==-1)
	printf("Stack is empty\n");
else{
	stack[top--];
}

}
void display()
{
if(top==-1)
	{
	printf("Stack is empty\n");
	}
else
{
	int i;
	for(i=0;i<=top;i++)
	{
		printf("%c\n",stack[i]);
	}
}
}
void main()
{
char a[100];
gets(a);
int i;
char temp;
int len=strlen(a);
for(i=0;i<=len;i++)
{
	if(stack[top]==a[i])
	{
		temp=a[i];
		pop();
	}
	if(temp==a[i])
		continue;
	else
		push(a[i]);

}
display();
}


