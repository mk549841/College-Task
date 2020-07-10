#include<stdio.h>
int main()
{
	int a[10],i,j,n,b[10],sum=0;
	printf("Enter the n\n");
	scanf("%d",&n);
	printf("Enter the element one by one\n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	int max=0;
	for(i=0;i<n;i++)
	{
		sum=0;
		for(j=0;j<n;j++)
		{
			if(a[i]<=a[j])
			{
				sum=sum+a[i];
			}
			else
				sum=0;
			if(max<=sum)
				max=sum;
			
		}
	}
	printf("The sacks are %d\n",max);
	return 0;
}
