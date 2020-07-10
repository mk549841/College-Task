#include<stdio.h>
int main()
{
int n,k,i,x,arr[100001],q,w,left,right,j;
scanf("%d %d",&n,&q);
arr[0]=0;
for(i=0;i<=n-1;i++)
{int count=0;
scanf("%d",&x);
while(x>0)
{
if(x%2==1)
{
count++;
}
x=x>>1;
}
arr[i+1]=arr[i]+count;
}
for(i=0;i<=q-1;i++)
{int min=10000000;int count=0;
scanf("%d",&x);
left=0;
right=0;
while(left<=n && right<=n)
{
if(arr[right]-arr[left]>=x)
{
//printf("%d %d\n",left,right);
count=right-left;
if(count<min && count>0)
{
min=count;
}
left++;
}
else
{
right++;
}
}
if(count==0)
{
min=-1;
}
if(min==10000000)
{
min=1;
}
printf("%d\n",min);
}
return 0;
}


























/*Given an array A[] consisting of  N non-negative integers. Now, you need to answer Q queries of the following type given an integer K in each query. You need to find the minimum length L of any sub array of A, such that if all elements of this sub array are represented in binary notation and concatenated to form a binary string, then no of 1's in the resulting string is at least K.  Write an implementation of the problem given.

Input Format: The first line of the input consists of two space-separated integers N and Q. The second line contains N space separated integers, where the ith integer denotes A[i]. Next Q lines contain a non-negative integer K.

Output Format: For each query out of the Q ones, print the answer on a new line. If for a particular query no valid sub array exists, then print -1 as the answer to that query. 
SAMPLE INPUT

4 3
1 2 4 8
1
2
3

SAMPLE OUTPUT

1
2
3*/


