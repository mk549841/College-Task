#include<stdio.h>
#include<string.h>
void pusp(char var);
void pop ();
void display();
int top=-1;
int stack[100];

void main()
{
int  i;
char a[100];
scanf("%s",&a);
for(i=0;i<strlen(a);i++)
{
if ((a[i]=='(')||(a[i]=='{')||(a[i]=='['))
{
push(a[i]);
}
else if (((a[i]==')')||(a[i]=='}')||(a[i]==']')))
{
pop();
}
}
display();
}

void push(char var)
{
stack[top]=var;
top++;
}

void pop()
{
top--;
}
void display()
{
if (top==-1)
{
printf("Its valid ");
}
else 
{
printf("Its invalid");
}
}