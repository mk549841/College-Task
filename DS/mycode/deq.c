#include<stdio.h>
#include<stdlib.h>
int  q[100],max=5;
int f=-1;
int r=-1;
void enqr(int ele);
void deqf();
void enqf(int ele);
void deqr();
void display();


void main()
{
int ch,ele;
while(1)
{
printf("CHoice\n");
scanf("%d",&ch);
switch(ch){
case 1:
printf("enter the eleemtn \n");
scanf("%d",&ele);
enqr(ele);
break;
case 2:
deqf();
break;
case 3:
printf("enter the eleemtn \n");
scanf("%d",&ele);
enqf(ele);
break;
case 4:
deqr();
break;
case 5:
display();break;
default:
exit (0);
}
}
}

void enqr(int ele)
{
if(r==max-1)
printf("full");
else if((r==-1)&&(f==-1))
f=r=0;
else 
{
r++;
q[r]=ele;

}
display();
}

void deqf()
{
if(f==-1)
printf("empty");
else
{
printf("Deleted element %d\n",q[f]);
if(f==r)
f=r=-1;
else
f++;
}
display();
}

void enqf(int element)
{
if(f<=0)
printf("FULL");
else
q[f--]=element;
display();
}

void deqr()
{
if(r==-1)
printf("empty");
else
{
printf("delete  at rrear =%d \n",q[r]);
if(f==r)
f=r=-1;
else
r--;
display();
}
}
void display()
{
int i;
if((r==-1)||(f==-1))
printf("empty");
else
{
for(i=f;i<=r;i++)
printf("%d",q[i]);
printf("\n");
}
}
















